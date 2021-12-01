with open("data.txt") as file:
    lines = file.readlines()
list_of_nums = []

for line in lines:
    list_of_nums.append(line.strip())
count = len(list_of_nums) - 2
datatrips = []

i = 0

while i < count:
    datatrips.append(tuple([int(list_of_nums[0]), int(list_of_nums[1]), int(list_of_nums[2])]))
    i += 1
    del list_of_nums[0]

len1 = len(datatrips) - 1
l = 0
total = 1
previous = sum(datatrips[0])
sum1 = sum(datatrips[1])

while l < len1:
    if previous < sum1:
        total += 1
    previous = sum1
    del datatrips[0]
    sum1 = sum(datatrips[0])
    l += 1

print(total)
