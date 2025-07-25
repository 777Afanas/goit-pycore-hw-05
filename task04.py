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
            return "Sorry, contact not found."
        except ValueError:
            return "Enter name and phone please."
        except IndexError:
            return "Enter all required parameters please."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:           
        raise IndexError     
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:           
        raise ValueError
    name, new_phone = args
    if name not in contacts:         
        raise KeyError
    contacts[name] = new_phone
    return "Contact update." 

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError         
    name = args[0]
    if name in contacts:
        return contacts[name]
    else: 
        raise KeyError         

@input_error
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