
def caching_fibonacci(): 
    cache = {}    # Локальна змінна зовнішньої функції

    def fibonacci(n):
        if n <= 0:
            return 0 # Базовий випадок: 0-те число Фібоначчі
        if n == 1:
            return 1 # Базовий випадок: 1-ше число Фібоначчі     
        # Використовує змінну cache із зовнішньої області видимості
        if n in cache:
            return cache[n]  # Повертаємо кешоване значення, у разі наявності
        
        # Якщо немає в кеші — обчислюємо рекурсивно та зберігаємо в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]      
    
    return fibonacci # Повертаємо внутрішню функцію 
 

fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610