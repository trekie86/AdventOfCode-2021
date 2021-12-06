# Most Frequent Digit
def most_frequent(data_list):
    # print("data_list:" + str(data_list))
    zeros = data_list.count(0)
    ones = data_list.count(1)
    # print("zeros:" + str(zeros))
    # print("ones:" + str(ones))
    if zeros > ones:
        return 0
    if ones >= zeros:
        return 1


# Least Frequent Digit
def least_frequent(data_list):
    # print("data_list:" + str(data_list))
    zeros = data_list.count(0)
    ones = data_list.count(1)
    # print("zeros:" + str(zeros))
    # print("ones:" + str(ones))
    if zeros <= ones:
        return 0
    if ones < zeros:
        return 1


# Open Data File
with open("data.txt") as file:
    lines = file.read().splitlines()
    # print("Lines:" + str(lines))

index = 12
oxygen = []
co2 = []
digits = []

# Get Oxygen
contenders = lines
i = 0
while i < index:
    # Get Fist Digits of Contenders
    for contender in contenders:
        digits.append(int(contender[i]))
    # print("Digits:" + str(digits))

    # Get Most Frequent Digit
    max_num = (most_frequent(digits))
    # print("Max_Num:" + str(max_num))

    # Clear List
    digits.clear()

    # print("Contenders:" + str(contenders))

    # Match Starting Digit to Contenders
    results = list(filter(lambda x: (x[i] == str(max_num)), contenders))
    # print("Results:" + str(results))
    contenders = results
    i += 1

oxygen_bi = ("".join([str(i) for i in results]))
oxygen_int = int(oxygen_bi, 2)
print("Oxygen_Binary:" + str(oxygen_bi))
print("Oxygen_Int:" + str(oxygen_int))

# Get CO2
contenders = lines
i = 0
while i < index:
    # Get Fist Digits of Contenders
    for contender in contenders:
        digits.append(int(contender[i]))
    # print("Digits:" + str(digits))

    # Get Most Frequent Digit
    min_num = (least_frequent(digits))
    # print("Max_Num:" + str(min_num))

    # Clear List
    digits.clear()

    # print("Contenders:" + str(contenders))

    # Match Starting Digit to Contenders
    results = list(filter(lambda x: (x[i] == str(min_num)), contenders))
    # print("Results:" + str(results))
    contenders = results
    i += 1
    if len(contenders) == 1:
        break

co2_bi = ("".join([str(i) for i in results]))
co2_int = int(co2_bi, 2)
print("CO2_Binary:" + str(co2_bi))
print("CO2_Int:" + str(co2_int))

life_support = oxygen_int * co2_int
print("Life_Support:" + str(life_support))