import math

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')

print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {your_number}')


print(message)
calc(25.5)
