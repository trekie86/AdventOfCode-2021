with open("data.txt") as file:
    lines = file.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    if "forward" in line:
        for char in line.split():
            if char.isdigit():
                num = (int(char))
        horizontal += num
        add_depth = aim * num
        depth += add_depth

    if "down" in line:
        for char in line.split():
            if char.isdigit():
                num = (int(char))
        aim += num

    if "up" in line:
        for char in line.split():
            if char.isdigit():
                num = (int(char))
        aim -= num

total = horizontal * depth
print(total)
