import os

DATA_FILE = "data/todo_list.txt"


def ensure_file_exists() -> None:
    """Проверяет существование директории и файла данных."""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            pass


def load_tasks() -> list[str]:
    """Читает список задач из текстового файла."""
    ensure_file_exists()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except (FileNotFoundError, IOError):
        print("Ошибка при чтении файла данных.")
        return []


def save_tasks(tasks: list[str]) -> None:
    """Сохраняет текущий список задач в текстовый файл."""
    ensure_file_exists()
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(f"{task}\n")
    except IOError:
        print("Ошибка при сохранении файла данных.")


def add_task_logic(task: str) -> str:
    """Добавляет новую задачу в список и сохраняет изменения."""
    if not task.strip():
        return "Ошибка: Текст задачи не может быть пустым!"

    tasks = load_tasks()
    tasks.append(task.strip())
    save_tasks(tasks)
    return f"Задача '{task}' успешно добавлена!"


def delete_task_logic(index: int) -> str:
    """Удаляет задачу по её порядковому номеру (начиная с 1)."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        return f"Задача '{removed}' успешно удалена!"
    return "Ошибка: Неверный номер задачи!"


def search_tasks_logic(keyword: str) -> list[str]:
    """Ищет задачи по ключевому слову (без учета регистра)."""
    tasks = load_tasks()
    keyword_lower = keyword.lower()
    return [task for task in tasks if keyword_lower in task.lower()]