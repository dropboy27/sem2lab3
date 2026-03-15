from src.TaskSources.file_task import FileTaskSource
from src.TaskSources.task_generator import TaskGenerator
from src.TaskSources.api_task import ApiTaskSource
from src.recieve_tasks import receive
from src.exceptions.file_task_source_exceptions import TaskSourceError
from src.exceptions.task_exceptions import TaskError
from src.classes.task_queue import TaskQueue


def main() -> None:
    tasks = TaskQueue()
    while True:
        print("\n1 - Прочитать задачу из файла\n"
              "2 - Сгенерировать задачи\n"
              "3 - API заглушка\n"
              "4 - Увидеть задачи\n"
              "5 - фильтры\n"
              "6 - Выход\n")
        try:
            variant = int(input("Выберите пункт: "))
        except ValueError:
            print("Ошибка: введите число.")
            continue

        try:
            if variant == 1:
                filename = input("Укажите файл: ")
                src = FileTaskSource(filename)
                for t in receive(src):
                    tasks.add_task(t)

            elif variant == 2:
                num = int(input("Укажите количество задач: "))
                src = TaskGenerator(num)
                for t in receive(src):
                    tasks.add_task(t)

            elif variant == 3:
                num = int(input("Укажите количество задач для API: "))
                src = ApiTaskSource(tasks_count=num, simulate_delay=True)
                for t in receive(src):
                    tasks.add_task(t)

            elif variant == 4:
                if not tasks:
                    print("Нет задач")
                    continue
                print("1 - полное описание\n2 - краткое описание")
                try:
                    choice = int(input())
                except ValueError:
                    print("Ошибка: введите число")
                    continue

                if choice == 1:
                    for t in tasks:
                        print(t)
                elif choice == 2:
                    for t in tasks:
                        print(t.short_desc)
                else:
                    print("Неверный выбор")
            elif variant == 5:
                print("choose filter:\n"
                      "1 - filter by priority\n"
                      "2 - filter by status\n"
                      "3 - filter by id\n")
                choice = int(input())
                if choice == 1:
                    print("choose priority from 1 to 5")
                    priority = int(input())
                    if priority > 5 or priority < 1:
                        raise ValueError("Incorrect priority")
                    print(
                        f"1 - lower than {priority}\n 2 - higher than {priority}\n 3 - equal to {priority}")
                    condition = int(input())
                    for t in tasks.filter_by_priority(priority, condition):
                        print(t)
                elif choice == 2:
                    print("choose status from ('новая', 'в работе', 'завершена')")
                    status = input()
                    if status not in ('новая', 'в работе', 'завершена'):
                        raise ValueError("Incorrect status")
                    print(
                        f"1 - show all tasks with {status}\n 2 - show all tasks without {status}")
                    condition = int(input())
                    for t in tasks.filter_by_status(status, condition):
                        print(t)
                elif choice == 3:
                    print("choose id")
                    id = int(input())
                    print(
                        f"1 - lower than {id}\n 2 - higher than {id}\n 3 - equal to {id}")
                    condition = int(input())
                    for t in tasks.filter_by_id(id, condition):
                        print(t)
                else:
                    print("Неверный выбор")
            elif variant == 6:
                break

            else:
                print(f"Неверный пункт меню: {variant}")

        except TaskSourceError as e:
            print(f"Ошибка источника: {e}")
        except TaskError as e:
            print(f"Ошибка валидации задачи: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
