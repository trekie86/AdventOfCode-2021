def most_frequent(data_list):
    print("---Get Most Frequent---")
    print("data_list:" + str(data_list))
    zeros = data_list.count(0)
    ones = data_list.count(1)
    print("zeros:" + str(zeros))
    print("ones:" + str(ones))
    if zeros > ones:
        print("return 0")
        return 0
    if ones >= zeros:
        print("return 1")
        return 1


def least_frequent(data_list):
    return min(set(data_list), key=data_list.count)


with open("data.txt") as file:
    lines = file.read().splitlines()

oxygen = []
co2 = []
digits = []
contenders = []
index = 5

# Find Most Frequent Digit
# Put Items with Most Frequent Digit in List
contenders = lines
print("contenders:" + str(contenders))
i = 0
while i < index:
    for contender in contenders:
        digits.append(int(contender[i]))
    oxygen.append(most_frequent(digits))
    digits.clear()
    print("i:" + str(i))
    print("Oxygen:" + str(oxygen))
    result = list(filter(lambda x: (x[i] == oxygen[i]), contenders))
    contenders = result
    print("Contenders:" + str(contenders))
    i += 1

# Find Least Common Digit
# Put Items with Least Frequent Digit in List
contenders = lines
print("contenders:" + str(contenders))
i = 0
while i < index:
    for contender in contenders:
        digits.append(contender[i])
    co2.append(least_frequent(digits))
    digits.clear()
    print("i:" + str(i))
    print("co2[]:" + co2[i])
    result = list(filter(lambda x: (x[i] == co2[i]), contenders))
    contenders = result
    print("Contenders:" + str(contenders))
    i += 1

oxygen_bi = ("".join([str(i) for i in oxygen]))
oxygen_int = int(oxygen_bi, 2)
co2_bi = ("".join([str(i) for i in co2]))
co2_int = int(co2_bi, 2)

life_support = oxygen_int * co2_int

print("Oxygen_Binary:" + str(oxygen_bi))
print("Oxygen_Int:" + str(oxygen_int))
print("CO2_Binary:" + str(co2_bi))
print("CO2_Int:" + str(co2_int))
print(life_support)
