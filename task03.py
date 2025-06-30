import sys
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Optional 


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Розбирає один рядок лог-файлу на складові: дата, час, рівень логування, повідомлення.

    Повертає пустий словник, якщо формат рядка неправильний.
    """
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3]
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Завантажує лог-файл і повертає список розібраних логів.
    Обробляє типові помилки при відкритті та читанні файлу.

    Використано:
    - Списковий вираз для застосування функції parse_log_line до кожного рядка.
    - Списковий вираз для фільтрації пустих словників (еквівалент filter).
    """
    logs = []
    try:
        path = Path(file_path)
        with path.open('r', encoding='utf-8') as file:
            logs = [parse_log_line(line) for line in file]  # списковий вираз (list comprehension)
            logs = [log for log in logs if log]  # списковий вираз (filter за допомогою list comprehension)
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except PermissionError:
        print(f"Помилка: Відсутній доступ до файлу '{file_path}'.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Помилка: Неможливо прочитати файл '{file_path}' через проблеми з кодуванням.")
        sys.exit(1)
    except Exception as e:
        print(f"Невідома помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує логи за вказаним рівнем.
    Обробляє можливі помилки у структурі логів.

    Використано:
    - Лямбда-функція для фільтрації логів за рівнем.
    - filter для відбору записів.
    """
    level = level.upper()
    try:
        # Використовуємо filter та lambda для фільтрації
        filtered = list(filter(lambda log: log['level'] == level, logs))  # filter + lambda
    except KeyError as e:
        print(f"Помилка: Відсутній ключ {e} у записах логів.")
        filtered = []
    except Exception as e:
        print(f"Невідома помилка при фільтрації логів: {e}")
        filtered = []
    return filtered


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Рахує кількість логів по кожному рівню.
    Обробляє можливі помилки у структурі логів.
    """
    counts = defaultdict(int)
    try:
        for log in logs:
            counts[log['level']] += 1
    except KeyError as e:
        print(f"Помилка: Відсутній ключ {e} у записах логів.")
    except Exception as e:
        print(f"Невідома помилка при підрахунку логів: {e}")
    return dict(counts)


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Виводить підрахунок логів за рівнями у вигляді таблиці.
    """
    print("\nПідрахунок логів за рівнем логування:")
    print("-" * 40)
    print(f"{'Рівень':<10} | {'Кількість':>10}")
    print("-" * 40)
    for level in ['INFO', 'ERROR', 'DEBUG', 'WARNING']:
        count = counts.get(level, 0)
        print(f"{level:<10} | {count:>10}")
    print("-" * 40)


def display_logs(logs: List[Dict[str, str]]) -> None:
    """
    Виводить деталі логів.
    Обробляє можливі помилки у структурі логів.
    """
    for log in logs:
        try:
            print(f"{log['date']} {log['time']} {log['level']:<7} {log['message']}")
        except KeyError as e:
            print(f"Помилка: Відсутній ключ {e} у записі лога.")
        except Exception as e:
            print(f"Невідома помилка при виводі логів: {e}")


def main():
    """
    Головна функція для запуску парсера логів.
    Використання:
        python log_parser.py <шлях_до_лог_файлу> [рівень_логування]
    """
    if len(sys.argv) < 2:
        print("Використання: python log_parser.py <шлях_до_лог_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter: Optional[str] = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if level_filter:
        # Використовуємо filter з лямбда-функцією безпосередньо тут для фільтрації логів
        filtered_logs = list(filter(lambda log: log['level'] == level_filter.upper(), logs))  # filter + lambda
        print(f"\nЛоги рівня {level_filter.upper()}:")
        print("-" * 40)
        display_logs(filtered_logs)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()





# def parse_log_line(line: str) -> dict:

#     parts = line.strip().split(maxsplit=3)
#     if len(parts) < 4:
#         return {}
#     return{
#         "date": parts[0],
#         "time": parts[1],
#         "level": parts[2].upper(),
#         "message": parts[3]
#     }

# def load_logs(file_path: str) -> list:
#     logs = []
#     try: 
#         path = Path(file_path)
#         with path.open('r', encoding='utf-8') as file:
#             logs = [parse_log_line(line) for line in file]
#             logs = [log for log in logs if log] 
#     except Exception as e:
#         print(f"Помилка при читанні файлу: {e}")
#         sys.exit(1)
#     return logs    

# def filter_logs_by_level(logs: list, level: str) -> list:

#     level = level.upper()
#     return list(filter(lambda log: log['level'] == level, logs))

# def count_logs_by_level(logs: list) -> dict:

#     counts = defaultdict(int)
#     for log in logs:
#         counts[log['level']] += 1
#     return dict(counts)

# def display_log_counts(counts: dict):

#     print("\nПідрахунок логів за рівнем логування:")
#     print("-" * 40)
#     print(f"{'Рівень':<10} | {'Кількість':>10}")
#     print("-" * 40)
#     for level in ['INFO', 'ERROR', 'DEBUG', 'WARNING']:
#         count = counts.get(level, 0)
#         print(f"{level:<10} | {count:>10}")
#     print("-" * 40)

# def display_logs(logs: list):
    
#     for log in logs:
#         print(f"{log['date']} {log['time']} {log['level']:<7} {log['message']}")

# def main():
#     if len(sys.argv) < 2:
#         print("Використання: python log_parser.py <шлях_до_лог_файлу> [рівень_логування]")
#         sys.exit(1)

#     file_path = sys.argv[1]
#     level_filter = sys.argv[2] if len(sys.argv) > 2 else None
#     logs = load_logs(file_path)

#     if level_filter:
#         filtered_logs = filter_logs_by_level(logs, level_filter)
#         print(f"\nЛоги рівня {level_filter.upper()}:")
#         print("-" * 40)
#         display_logs(filtered_logs)
#     else:
#         counts = count_logs_by_level(logs)
#         display_log_counts(counts)

# if __name__ == "__main__":
#     main()




