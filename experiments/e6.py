while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to do: ") + "\n"
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("../files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            # Option 2
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Enter a number of to do item: "))
            number = number - 1
            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter a number of to do complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Invalid input")

print('Bye')