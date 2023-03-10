todos = []

while True:
    user_action = input("Type add or show or q to quit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'q':
            break
        case _:
            print("Hey, you entered an invalid input.")

print("exited")