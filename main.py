todos = []

while True:
    user_action = input("Type add, show, edit, complete to remove a task, or quit to quit: ")
    user_action = user_action.strip()

    
    if ('add' in user_action):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        
    elif ('show' in user_action or 'display' in user_action):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}-{item}')
    elif ('quit' in user_action):
        break
    elif ('edit' in user_action):
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
        
    elif ('complete' in user_action):
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
    else:
        print("Hey, you entered an invalid input.")

print("exited")