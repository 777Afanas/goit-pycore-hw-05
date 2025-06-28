from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args 

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough parameters provided."
    return inner


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: You must provide a name and a new phone number."     
    name, new_phone = args
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    contacts[name] = new_phone
    return "Contact update." 

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: You must provide exactly one name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: Contact '{name}' not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ["Contacts list:"]
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)
   
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command:  ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break 
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")    

if __name__ == "__main__":
    main()