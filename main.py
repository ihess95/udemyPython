todos = []

while True:
    user_action = input("Type add or show or q to quit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'q':
            break

print("exited")