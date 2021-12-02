with open("data.txt") as file:
    lines = file.readlines()

start_horizontal = 0
start_depth = 0

for line in lines:
    if "forward" in line:
        for char in line.split():
            if char.isdigit():
                num = (int(char))
        start_horizontal += num

    if "down" in line:
        for char in line.split():
            if char.isdigit():
                num = (int(char))
        start_depth += num

    if "up" in line:
        for char in line.split():
            if char.isdigit():
                num = (int(char))
        start_depth -= num

total = start_horizontal * start_depth
print(total)
