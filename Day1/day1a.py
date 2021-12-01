with open("data.txt") as file:
    lines = file.readlines()

count = 0
previous = lines[0]

for line in lines:
    if int(line) > int(previous):
        count += 1
    previous = line

print(count)
