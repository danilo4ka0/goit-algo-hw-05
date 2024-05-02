import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі числа у тексті за допомогою регулярного виразу
    pattern = r'\b\d+\.\d+\b'  # Враховуємо дійсні числа
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо знайдене число як дійсне

def sum_profit(text: str, func: Callable):
    total_sum = sum(func(text))  # Обчислюємо суму всіх чисел, які повертає генератор
    return total_sum

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
