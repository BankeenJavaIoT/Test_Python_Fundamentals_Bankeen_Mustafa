

def list_manipulation(list, command, location, value=None):
    if command == "remove":
        if location == "end":
            return list.pop(-1)
        elif location == "beginning":
            return list.pop(0)
    elif command == "add":
        if location == "beginning":
            list.insert(0, value)
            return list
        elif location == "end":
            list.append(value)
            return list


print(list_manipulation([1, 2, 3], "remove", "end"))
print(list_manipulation([1, 2, 3], "remove", "beginning"))
print(list_manipulation([1, 2, 3], "add", "beginning", 20))
print(list_manipulation([1, 2, 3], "add", "end", 30))
