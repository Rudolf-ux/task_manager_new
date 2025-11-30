import json


class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_from_file()

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f'Задача "{title}" добавлена.')

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f'Задача "{title}" отмечена как выполненная.')
                return

    def show_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Выполнено" if task.is_done else "Не выполнено"
            print(f"{i}. {task.title} - {status}")

    def save_to_file(self):
        data = []
        for task in self.tasks:
            data.append({
                'title': task.title,
                'is_done': task.is_done
            })

        with open('tasks.json', 'w') as f:
            json.dump(data, f)

    def load_from_file(self):
        try:
            with open('tasks.json', 'r') as f:
                data = json.load(f)

            for item in data:
                task = Task(item['title'])
                if item['is_done']:
                    task.mark_done()
                self.tasks.append(task)
        except FileNotFoundError:
            pass


def main():
    manager = TaskManager()

    while True:
        command = input("Введите команду: ")

        if command == "add":
            title = input("Введите название задачи: ")
            manager.add_task(title)

        elif command == "done":
            title = input("Введите название задачи: ")
            manager.mark_task_done(title)

        elif command == "show":
            manager.show_tasks()

        elif command == "exit":
            manager.save_to_file()
            print("Данные сохранены. Программа завершена.")
            break


if __name__ == "__main__":
    main()