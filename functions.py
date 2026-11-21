FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """reads todos from a file
    and returns the list of items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """writes todos in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")

