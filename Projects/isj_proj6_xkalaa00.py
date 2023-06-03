#!/usr/bin/env python3

class Polynomial:

    # Konstruktor
    def __init__(self, *args, **kwargs):
        self.polynom = {}

        # Pokud byl predan jeden argument a je to list, vyuzijeme ho
        if len(args) == 1 and isinstance(args[0], list):
            vocab = args[0]
        else:
        # Pokud ne, vytvorime ho
            vocab = list(args)

        # Prochazi koeficienty a vytvari slovnik
        for i, value in enumerate(vocab):
            if value != 0:
                self.polynom[i] = value
        # Prochazi klice a hodnoty v kwargs a prida je k ostatnim koeficintum
        for key, value in kwargs.items():
            if value != 0:
                self.polynom[int(key[1:])] = value

        # Pokud je prazdny, prida 0
        if not self.polynom:
            self.polynom[0] = 0

    def __str__(self):
        terms = []

        # Prochazi klice a hodnoty a vytvari jednotlive cleny
        for key, value in sorted(self.polynom.items(), reverse=True):
            sign = "-" if value < 0 else "+"
            abs_coef = abs(value) if abs(value) > 1 or key == 0 else ""
            variable = "x" if key else ""
            exponent = f"^{key}" if key > 1 else ""
            term = f"{sign} {abs_coef}{variable}{exponent}"
            terms.append(term)

        # Vrati vysledny retezec
        result = " ".join(terms).strip(" +-") or "0"
        return result

    def __add__(self, other):
        result_dict = {}
        # Vytvori slovnik, ktery bude obsahovat soucty polynomu
        for key in set(self.polynom.keys()) | set(other.polynom.keys()):
            result_dict[f"x{key}"] = self.polynom.get(key, 0) + other.polynom.get(key, 0)
        return Polynomial(**result_dict)

    def __eq__(self, other):
        # Vrati true, pokud jsou dve instance stejne
        return self.polynom == other.polynom

    def __pow__(self, power):
        # Umocneni polynomu
        if power:
            var = self.polynom
        
        for _ in range(power - 1):
            result = {}

            # Projde klice a hodnoty prvniho a vynasobiho s druhym
            for first_key, first_value in self.polynom.items():
                for second_key, second_value in var.items():
                    result[first_key + second_key] = result.get(first_key + second_key, 0) + first_value * second_value
            var = result
        return Polynomial(**{f"x{k}": v for k, v in var.items()})
        

    def derivative(self):
        # Vypocita derivaci polynomu
        derived = {}
        for key, value in self.polynom.items():
            # Pokud je klic vetsi nez 0, vytvori se novy 
            if key > 0:
                result_key = f"x{key-1}"
                result_value = value * key
                derived[result_key] = result_value
        return Polynomial(**derived)

    def at_value(self, value_x, value_y=None):
        # Pokud y existuje, vypocita rozdil a vrati ho
        if value_y is not None:
            return self.at_value(value_y) - self.at_value(value_x)
        # Pokud ne, vypocita hodnotu polynomu pro hodnotu x
        result = 0
        for key, value in self.polynom.items():
            result += (value) * (value_x ** key)
        return result

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
    