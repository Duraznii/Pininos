def read_todo_list(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def write_todo_list(file_path, items):
    with open(file_path, "w") as file:
        file.writelines(items)

def add_item(file_path, item):
    items = read_todo_list(file_path)
    items.append(item + "\n")
    write_todo_list(file_path, items)

def remove_item(file_path, item):
    items = read_todo_list(file_path)
    items = [i for i in items if i.strip() != item]
    write_todo_list(file_path, items)

def main():
    file_path = "/Users/mac/Desktop/Python-course/Mis-to-do"
    while True:
        action = input("Do you want to add or remove an item? (add/remove/exit): ").strip().lower()
        if action == "add":
            item = input("Enter the item to add: ").strip()
            add_item(file_path, item)
        elif action == "remove":
            item = input("Enter the item to remove: ").strip()
            remove_item(file_path, item)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please enter 'add', 'remove', or 'exit'.")

if __name__ == "__main__":
    main()