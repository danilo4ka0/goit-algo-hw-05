
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
try:
    result = add_contact(args, contacts)
except Exception as e:
    result = str(e)  # Отримання тексту помилки
while True:
    command = input("Enter a command: ")
    if command == "add":
        # Отримуємо аргументи для команди "add"
        args = input("Enter the argument for the command: ").split()
        try:
            result = add_contact(args, contacts)
        except Exception as e:
            result = str(e)  # Отримання тексту помилки
        print(result)
