def caching_fibonacci():
    cache = {}  # Створення порожнього словника для кешування результатів обчислень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевірка, чи вже є результат для n у кеші
            return cache[n]
        else:
            # Обчислення числа Фібоначчі за допомогою рекурсії
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result  # Збереження результату у кеші
            return result

    return fibonacci

# Приклад використання
fib = caching_fibonacci()  # Отримуємо функцію fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
