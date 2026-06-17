def is_leap_year(year):
    """
    Проверяет, является ли год високосным.
    Правила:
    - Год делится на 4
    - Но если делится на 100, то не високосный
    - Однако если делится на 400, то високосный
    """
    if not isinstance(year, int):
        return False
    
    if year <= 0:
        return False
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
