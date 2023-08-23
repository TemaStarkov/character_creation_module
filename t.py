from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(numo):
    """Вычисляет квадратный корень."""
    return sqrt(numo)


def calc(numo):
    """Проверяет корректность числа."""
    if numo <= 0:
        return print('Нет')
    suma = calculate_square_root(numo)
    return print(f'Мы вычислили квадратный корень '
                 f'из введённого вами числа. Это будет: {suma}')


calc(25.5)
