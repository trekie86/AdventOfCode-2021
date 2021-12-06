def parse_line(line):
    numbers = []
    for item in line.split():
        numbers.append([int(item), 0])
    return numbers


with open('data.txt') as data:
    all_data = data.readlines()

bingo_numbers = []

first_line = all_data[0].strip()
del all_data[0]
for num in first_line.split(","):
    bingo_numbers.append(int(num))


bingo_cards = []
bingo_card = []

for element in all_data:
    element = element.strip()
    # print(element)
    if element == "":
        temp_card = bingo_card
        # print("Temp_Card:")
        # print(temp_card)
        if temp_card:
            bingo_cards.append(temp_card)
        bingo_card = []
        continue
    bingo_card.append(parse_line(element))

a = 0
b = 0
c = 0
i = 0
bingo = False
winning_num = 0

#print("Bingo Numbers:")
#print(bingo_numbers)
#print("Bingo Cards:")
#print(bingo_cards)

for each in bingo_numbers:
    while c < 2:
        if bingo:
            break
        a = 0
        b = 0
        while b < 5:
            if bingo:
                break
            a = 0
            while a < 5:
                print("Location: C:" + str(c) + " B:" + str(b) + " A:" + str(a))
                print("Searching for " + str(each))
                print("Current number is " + str(bingo_cards[c][b][a][0]))
                if each == bingo_cards[c][b][a][0]:
                    bingo_cards[c][b][a][1] = 1
                    print("Match")
                else:
                    print("No Match")
                print("Horizonal Line:")
                print(bingo_cards[c][b][0] + bingo_cards[c][b][1] + bingo_cards[c][b][2] + bingo_cards[c][b][3] + bingo_cards[c][b][4])
                print(bingo_cards[c][b][0][1] + bingo_cards[c][b][1][1] + bingo_cards[c][b][2][1] + bingo_cards[c][b][3][1] + bingo_cards[c][b][4][1])
                print("Vertical Line:")
                print(bingo_cards[c][0][a] + bingo_cards[c][1][a] + bingo_cards[c][2][a] + bingo_cards[c][3][a] + bingo_cards[c][4][a])
                print(bingo_cards[c][0][a][1] + bingo_cards[c][1][a][1] + bingo_cards[c][2][a][1] + bingo_cards[c][3][a][1] + bingo_cards[c][4][a][1])
                if bingo_cards[c][b][0][1] + bingo_cards[c][b][1][1] + bingo_cards[c][b][2][1] + bingo_cards[c][b][3][1] + bingo_cards[c][b][4][1] == 5 or bingo_cards[c][0][a][1] + bingo_cards[c][1][a][1] + bingo_cards[c][2][a][1] + bingo_cards[c][3][a][1] + bingo_cards[c][4][a][1] == 5:
                    bingo = True
                    print("**********BINGO!***********")
                    #print(bingo_cards[c])
                    winning_num = bingo_cards[c][b][a][0]
                    break
                a += 1
            b += 1
        c += 1
    a = 0
    b = 0
    c = 0
# print(bingo_cards[c])
uncalled = 0
for number_list in bingo_cards[c]:
    print(number_list)
    for number in number_list:
        if number[1] == 0:
            # print("Uncalled: " + str(uncalled))
            # print("Number: " + str(number[0]))
            uncalled += number[0]

print("Last number called:")
print(winning_num)
print("Total of uncalled numbers on card:")
print(uncalled)
total = winning_num * uncalled
print("Total:")
print(total)
