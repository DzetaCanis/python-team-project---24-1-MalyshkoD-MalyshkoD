import os

DATA_FILE = "data/todo_list.txt"

def ensure_file_exists() -> None:
    """Перевіряє наявність каталогу та файлу даних"""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            pass
            
def load_tasks() -> list[str]:
    """Зчитує список завдань із текстового файлу"""
    ensure_file_exists()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except (FileNotFoundError, IOError):
        print("Помилка під час читання файлу даних")
        return []

def save_tasks(tasks: list[str]) -> None:
    """Зберігає поточний список завдань у текстовому файлі"""
    ensure_file_exists()
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(f"{task}\n")
    except IOError:
        print("Помилка під час збереження файлу даних")

def add_task_logic(task: str) -> str:
    """Добавляет новую задачу в список и сохраняет изменения"""
    if not task.strip():
        return ""Текст задачі не може бути порожнім!"

    tasks = load_tasks()
    tasks.append(task.strip())
    save_tasks(tasks)
    return f"Завдання '{task}' успішно додано!"

def delete_task_logic(index: int) -> str:
    """Видаляє завдання за його порядковим номером (починаючи з 1)"""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        return f"Завдання '{removed}' успішно видалена!"
    return "Неправильний номер завдання!"

def search_tasks_logic(keyword: str) -> list[str]:
    """Шукає завдання за ключовим словом (не враховуючи регістр)"""
    tasks = load_tasks()
    keyword_lower = keyword.lower()
    return [task for task in tasks if keyword_lower in task.lower()]
