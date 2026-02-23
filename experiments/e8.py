while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

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
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new to do: ")
        todos[number] = new_todo + '\n'

        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

        message = f"ToDo {todo_to_remove} was removed from the list"

        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Invalid input")

    # case _:
    #     print("Invalid input")

print('Bye')