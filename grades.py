def points(grade, is_AP):
    score = 0
    if grade > 94:
        score = 4
    elif grade > 85:
        score = 3
    elif grade > 77:
        score = 2
    elif grade >= 70:
        score = 1
    else:
        score = 0
    if is_AP:
        score += 0.2
    return score


points(76, True)