from src.interface import show_menu, view_tasks, add_task_ui, delete_task_ui, search_tasks_ui

def main():
    while True:
        show_menu()
        choice = input("\nОберіть дію (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task_ui()
        elif choice == "3":
            delete_task_ui()
        elif choice == "4":
            search_tasks_ui()
        elif choice == "5":
            print("\nДо побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, введіть число від 1 до 5.")

if __name__ == "__main__":
    main()