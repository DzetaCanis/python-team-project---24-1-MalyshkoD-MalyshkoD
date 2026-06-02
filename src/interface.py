from src.storage import load_tasks, add_task_logic, delete_task_logic, search_tasks_logic

def show_menu() -> None:
    print("\n--- TODO LIST MANAGER ---")
    print("1. Переглянути список задач")
    print("2. Додати задачу")
    print("3. Видалити задачу")
    print("4. Пошук за ключовим словом")
    print("5. Вийти")

def view_tasks() -> None:
    """Відображає поточні задачі користувачеві."""
    tasks = load_tasks()
    if not tasks:
        print("\nВаш список задач порожній.")
        return
    print("\nВаші задачі:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def add_task_ui() -> None:
    """Інтерфейс додавання задачі."""
    task_text = input("\nВведіть текст нової задачі: ")
    message = add_task_logic(task_text)
    print(message)

def delete_task_ui() -> None:
    """Інтерфейс видалення задачі з перевіркою введення."""
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        idx = int(input("\nВведіть номер задачі для видалення: "))
        message = delete_task_logic(idx)
        print(message)
    except ValueError:
        print("Помилка: Введіть коректне число!")

def search_tasks_ui() -> None:
    """Інтерфейс пошуку задач."""
    keyword = input("\nВведіть ключове слово для пошуку: ")
    if not keyword.strip():
        print("Помилка: Ключове слово не може бути порожнім!")
        return

    results = search_tasks_logic(keyword)
    if not results:
        print(f"Задач за запитом '{keyword}' не знайдено.")
        return
    print(f"\nЗнайдені задачі ({len(results)}):")
    for idx, task in enumerate(results, 1):
        print(f"{idx}. {task}")