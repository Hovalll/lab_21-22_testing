import math

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0
    Возвращает кортеж с корнями или сообщение об ошибке
    """
    if a == 0:
        if b == 0:
            if c == 0:
                return "Бесконечное множество решений"
            else:
                return "Нет решений"
        else:
            return (-c / b,)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "Нет действительных корней"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
