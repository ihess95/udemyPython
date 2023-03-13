todos = []

while True:
    user_action = input("Type add, show, edit, complete to remove a task, or q to quit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f'{index + 1}-{item}')
        case 'q':
            break
        case 'edit':
            try:
                with open('todos.txt', 'r') as file:
                    todos = file.readlines()
                to_edit = input('Which todo would you like to edit? ')
                edit = input(f'What would you like to change {todos[int(to_edit)-1]} to? ')
                todos[int(to_edit)-1] = f'{edit}\n'
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            except:
                print(f"That is not a valid task. Please choose a number between one and {len(todos)-1}")
            
        case 'complete':
            # try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            completed = input(f'Which task would you like to remove?')
            index = int(completed) -1
            print(f"You've deleted {todos[index]}.")
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            # except:
            #     print("Invalid index, please try again.")
        case _:
            print("Hey, you entered an invalid input.")

print("exited")