file1 = open('data.txt', 'r')
lines = file1.readlines()

count = 0
previous = lines[0]

for line in lines:
    if int(line) > int(previous):
        count += 1
    previous = line
print(count)
