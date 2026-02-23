def get_todos(filepath):
    filepath = "todo1.txt"
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos("../files/todos.txt")

        todos.append(todo + '\n')

        write_todos("../files/todos.txt", todos)
    elif user_action.startswith('show'):
        todos = get_todos("../files/todos.txt")

        # Option 1
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        #
        # for index, item in enumerate(new_todos):
        #     row = f"{index + 1}. {item}"
        #     print(row)

        # Option 2
        # new_todos = [item.strip('\n') for item in todos]
        #
        # for index, item in enumerate(new_todos):
        #     row = f"{index + 1}. {item}"
        #     print(row)

        # Option 3
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("../files/todos.txt")

            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo + '\n'

            write_todos("../files/todos.txt", todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos("../files/todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("../files/todos.txt", todos)

            message = f"ToDo {todo_to_remove} was removed from the list"

            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid input")

    # case _:
    #     print("Invalid input")

print('Bye')