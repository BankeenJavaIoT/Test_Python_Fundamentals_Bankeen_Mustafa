# Opdracht 4a

print("Opdracht 4a")

group_of_people = ['Alex', 'Elliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']
first_chars = [s[0] for s in group_of_people]

numbers = list(range(100))
sum = 0
for number in numbers:
    sum += number
print(f"the sum is: {sum}")

# Opdracht 4b

print("Opdracht 4b")

sample_items = [
    {"x": 10, "y": 85},
    {"x": 20, "y": 75},
    {"x": 30, "y": 65},
    {"x": 40, "y": 55},
    {"x": 50, "y": 45},
    {"x": 60, "y": 35}
]

x_limit = 33
y_limit = 44

# using list-comprehension fashion
list_comprehension = [item for item in sample_items if item["x"] > x_limit and item["y"] > y_limit]
print(list_comprehension)

# using list-standard fashion
list_standard = list()
for item in sample_items:
    if item["x"] > x_limit and item["y"] > y_limit:
        list_standard.append(item)
print(list_standard)

# Opdracht 4c

print("Opdracht 4c")

ten_by_ten = [list(range(10))] * 10
print(ten_by_ten)
