todos = []

while True:
    user_action = input("Type add, show, edit, complete to remove a task, or q to quit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            readFile = open('todos.txt', 'r')
            todos = readFile.readlines()
            readFile.close()

            todos.append(todo)


            writeFile = open('todos.txt', 'w')
            writeFile.writelines(todos)
            writeFile.close()
            
        case 'show' | 'display':
            readFile = open('todos.txt', 'r')
            todos = readFile.readlines()
            readFile.close()

            for index, item in enumerate(todos):
                print(f'{index + 1}-{item}')
        case 'q':
            break
        case 'edit':
            try:
                to_edit = input('Which todo would you like to edit? ')
                edit = input(f'What would you like to change {todos[int(to_edit)-1]} to? ')
                todos[int(to_edit)-1] = edit
            except:
                print(f"That is not a valid task. Please choose a number between one and {len(todo)-1}")
            
        case 'complete':
            try:
                completed = input('Which task would you like to remove? ')
                todos.pop(int(completed)-1)
            except:
                print("Invalid index, please try again.")
        case _:
            print("Hey, you entered an invalid input.")

print("exited")