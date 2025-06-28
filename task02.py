import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує дійсні числа (типу float) із тексту.
    Вважається, що дійсні числа чітко відокремлені пробілами.
    """
    pattern = r"(?<=\s)\d+\.\d+(?=\s)" # дійсні числа відокремлені пробілами з обох боків
    for number_str in re.findall(pattern, text):
        yield float(number_str) 

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює суму дійсних чисел, що генерує функція func з тексту.     
    :param text: Вхідний текст з числами
    :param func: Функція-генератор чисел (наприклад, generator_numbers)
    :return: Сума знайдених чисел
    """
    return sum(func(text))

# Тестовий текст з числами
text = (
    "Загальний дохід працівника складається з декількох " 
    "частин: 1000.01 як основний дохід, доповнений додатковими " 
    "надходженнями 27.45 і 324.00 доларів."
)
# Обчислення та вивід результату
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
