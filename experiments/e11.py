def get_todos(filepath="files/todos.txt"):
    """
    Reads a text file and returns a list
    of to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """
    Writes a list of to-do items to a text file.
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit, augue sed tempor dictum, ante tortor mattis 
mauris, id viverra est leo eu risus. Proin semper sem vel leo sagittis rhoncus. Nam tempus aliquam tortor, volutpat 
elementum felis pharetra lobortis. Donec aliquam ante mi, nec tempus enim facilisis vulputate.
 Integer auctor eget nisl nec lobortis. Cras aliquam lacus ac tortor bibendum, vitae eleifend tortor vulputate. Etiam lobortis 
 libero 
in sodales lacinia. Duis tortor purus, porttitor eget dui et, rutrum facilisis est. Etiam eros enim, volutpat sit amet 
ultricies sit amet, cursus sit amet libero. Phasellus ut tincidunt dolor. Pellentesque vel egestas ex. Vivamus 
pellentesque efficitur nulla, in mattis mauris mattis tincidunt. Praesent tempor quam ut turpis molestie lacinia. 
Quisque efficitur auctor varius. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer efficitur consectetur 
nunc rutrum pellentesque. 
"""

print(text)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):
        todos = get_todos()

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

            todos = get_todos()

            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

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
