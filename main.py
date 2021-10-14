
master_password = "Allahuakbar"
input_password = input("What is the password:- ")


def view():
    with open("passwords.text", "r") as f:
        for pair in f.readlines():
            print(pair.rstrip())


def add():
    name = input("Name of account:- ")
    password = input("Password: ")
    with open("passwords.text", "a")as f:
        f.write(f"Name: {name}\nPassword: {password}\n")


if input_password == master_password:
    while True:
        process = input("Do you want to add a new password or view existing ones?(view/add)\n Press 'q' to quit: ").lower()
        if process == 'q':
            break
        if process == "add":
            add()
        elif process == "view":
            view()
else:
    print("Wrong password")
    quit()


