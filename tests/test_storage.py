import unittest
import os
from src.storage import add_task_logic, delete_task_logic, search_tasks_logic, load_tasks, save_tasks

class TestTodoStorage(unittest.TestCase):

    def setUp(self):
        """Виконується перед кожним тестом. Створює чистий список для перевірки."""
        self.test_tasks = ["Купити молоко", "Прочитати книгу", "Здати лабораторну"]
        save_tasks(self.test_tasks)

    def tearDown(self):
        """Виконується після кожного тесту. Очищає тестові дані."""
        if os.path.exists("data/todo_list.txt"):
            try:
                os.remove("data/todo_list.txt")
            except IOError:
                pass

    def test_add_task(self):
        """Тест логіки додавання нової задачі."""
        result = add_task_logic("Написати реферат")
        # Виправлено під реальну відповідь вашої програми
        self.assertIn("успішно додано", result)

        # Перевіряємо, чи з'явилася задача у файлі
        tasks = load_tasks()
        self.assertIn("Написати реферат", tasks)

    def test_add_empty_task(self):
        """Тест перевірки помилки при спробі додати порожню задачу."""
        result = add_task_logic("   ")
        # Шукаємо ключове слово, яке точно є у вашій відповіді
        self.assertIn("порожнім", result)

    def test_delete_task_invalid_index(self):
        """Тест перевірки помилки при видаленні за неіснуючим номером."""
        result = delete_task_logic(99)  # Такого номера немає
        # Перевіряємо на реальну помилку вашої програми
        self.assertIn("Неправильний номер", result)

    def test_delete_task_success(self):
        """Тест успішного видалення задачі за коректним номером."""
        initial_count = len(load_tasks())
        result = delete_task_logic(1)  # Видаляємо першу задачу ("Купити молоко")
        self.assertIn("успішно видалена", result)

        # Перевіряємо, що кількість задач зменшилась
        self.assertEqual(len(load_tasks()), initial_count - 1)

    def test_search_tasks_found(self):
        """Тест успішного пошуку задач за ключовим словом."""
        results = search_tasks_logic("книгу")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], "Прочитати книгу")

    def test_search_tasks_not_found(self):
        """Тест пошуку, якщо збігів немає."""
        results = search_tasks_logic("Ремонт")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()