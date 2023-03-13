todos = []

while True:
    user_action = input("Type add, show, edit or q to quit: ")
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
        case 'edit':
            try:
                to_edit = input('Which todo would you like to edit? ')
                edit = input(f'What would you like to change {todos[int(to_edit)-1]} to? ')
                todos[int(to_edit)-1] = edit
            except:
                print(f"That is not a valid task. Please choose a number between one and {len(todo)-1}")
            
        case _:
            print("Hey, you entered an invalid input.")

print("exited")