from threading import main_thread

def parse_input(user_input):
    """Parse user input like command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Please provide correct arguments."
        except IndexError:
            return "Invalid number of arguments."
        except TypeError:
            return "Please provide a command."

    return inner

@input_error
def add_contact(arguments, contacts):
    name, phone = arguments    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(arguments, contacts):
    name, phone = arguments 
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    return contacts

def main():
    print("Welcome to the assistant bot!")
    contacts = {}  # словник для зберігання імен та номерів телефонів
    while True:
        command = input("Enter a command: ").strip().lower()
        if not command:
            print("Please provide a command.")
            continue

        action, *arguments = parse_input(command)

        if action in ["close", "exit"]:
            print("Good bye!")
            break

        if action == "hello":
            print("How can I help you?")

        elif action == "add":   
            result = add_contact(arguments, contacts)
            print(result)

        elif action == "change":
            result = change_contact(arguments, contacts)
            print(result)

        elif action == "phone":
            if len(arguments) == 1:
                result = show_phone(arguments[0], contacts)
                print(result)
            else:
                print("Invalid command. Usage: phone [name]")

        elif action == "all":
            result = show_all(contacts)
            print(result)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
