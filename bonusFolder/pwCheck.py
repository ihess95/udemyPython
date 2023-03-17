def pwCheck(pw):
    if (len(pw)>8 and any(char.isdigit() for char in pw) and any(char.isupper() for char in pw)):
        print("Strong")
    elif(len(pw)>8 or any(char.isdigit() for char in pw) or any(char.isupper() for char in pw)):
        print("Medium")
    else:
        print("Weak")

pwCheck(input("Input your password: "))