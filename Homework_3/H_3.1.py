

def get_string_length(s: str) -> int:
    """Повертає довжину рядка."""
    return len(s)


def concatenate_strings(s1: str, s2: str) -> str:
    """Повертає об'єднаний рядок."""
    return s1 + s2


def square_number(n: float) -> float:
    """Повертає квадрат числа."""
    return n ** 2


def sum_two_numbers(a: float, b: float) -> float:
    """Повертає суму двох чисел."""
    return a + b


def divide_with_remainder(a: int, b: int) -> tuple[int, int]:
    """Виконує ділення двох int і повертає цілу частину та залишок."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder


def calculate_average(numbers: list[float]) -> float:
    """Обчислює середнє значення списку чисел."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def find_common_elements(list1: list, list2: list) -> list:
    """Повертає список спільних елементів обох списків."""
    return list(set(list1) & set(list2))


def print_dict_keys(d: dict) -> None:
    """Виводить всі ключі словника."""
    for key in d.keys():
        print(key)


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """Повертає новий словник, який є об'єднанням двох словників."""
    return dict1 | dict2


def union_sets(set1: set, set2: set) -> set:
    """Повертає об'єднання двох множин."""
    return set1.union(set2)


def is_subset(set1: set, set2: set) -> bool:
    """Перевіряє, чи є set1 підмножиною set2."""
    return set1.issubset(set2)


def check_even_odd(number: int) -> None:
    """Виводить 'Парне' або 'Непарне' залежно від числа."""
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Повертає новий список, що містить тільки парні числа."""
    return [num for num in numbers if num % 2 == 0]






check_even_odd_lambda = lambda num: "парне" if num % 2 == 0 else "не парне"




if __name__ == "__main__":
    print("--- 1. Рядки ---")
    print("Довжина 'Hello':", get_string_length("Hello"))
    print("Об'єднання:", concatenate_strings("Python ", "Pro"))

    print("\n--- 2. Числа ---")
    print("Квадрат 5:", square_number(5))
    print("Сума 4 + 7:", sum_two_numbers(4, 7))
    q, r = divide_with_remainder(10, 3)
    print(f"10 // 3 = {q}, залишок = {r}")

    print("\n--- 3. Списки ---")
    print("Середнє [10, 20, 30]:", calculate_average([10, 20, 30]))
    print("Спільні елементи:", find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

    print("\n--- 4. Словники ---")
    print("Ключі словника {'a': 1, 'b': 2}:")
    print_dict_keys({'a': 1, 'b': 2})
    print("Об'єднання словників:", merge_dictionaries({'a': 1}, {'b': 2}))

    print("\n--- 5. Множини ---")
    print("Об'єднання множин:", union_sets({1, 2}, {2, 3}))
    print("Чи є {1, 2} підмножиною {1, 2, 3}?:", is_subset({1, 2}, {1, 2, 3}))

    print("\n--- 6. Умови та цикли ---")
    print("Перевірка 4:")
    check_even_odd(4)
    print("Фільтр парних [1, 2, 3, 4, 5, 6]:", filter_even_numbers([1, 2, 3, 4, 5, 6]))

    print("\n--- 7. Лямбда-функція ---")
    print("Число 8:", check_even_odd_lambda(8))
    print("Число 7:", check_even_odd_lambda(7))