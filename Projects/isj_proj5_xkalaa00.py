def gen_quiz(qpool, *indices, altcodes='ABCDEF', quiz=None):
    if quiz is None:
        quiz = []
    for i in indices:
        try:
            question, answers = qpool[i]
        except (IndexError, TypeError, ValueError) as err:
            print(f"Ignoring index {i} - {err}")
            continue
        answers = answers[:len(altcodes)]
        quiz.append((question, [f"{code}: {answer}" for code, answer in zip(altcodes, answers)]))
    return quiz
