# Function to split Bingo data into their own lists and add a tracker bool
def parse_line(line):
    numbers = []
    for item in line.split():
        numbers.append([int(item), 0])
    return numbers


# Open File with data
with open('data.txt') as data:
    all_data = data.readlines()

# Variables and Lists
bingo_numbers = []
bingo_cards = []
bingo_card = []
bingo = False
winning_num = 0

# Cut out line one and add to Bingo call numbers list
first_line = all_data[0].strip()
for num in first_line.split(","):
    bingo_numbers.append(int(num))

# Loop through Bingo Card data and add to nested lists
for element in all_data[2:]:
    element = element.strip()
    if element == "":
        temp_card = bingo_card
        if temp_card:
            bingo_cards.append(temp_card)
        bingo_card = []
        continue
    bingo_card.append(parse_line(element))
bingo_cards.append(temp_card)

# Loop through all the Bingo numbers and search the Bingo cards for matches
for each in bingo_numbers:
    # Loop through all cards
    for c in range(len(bingo_cards)):
        if bingo:
            break
        # Loop through all rows
        for b in range(5):
            if bingo:
                break
            # Loop through all digits
            for a in range(5):
                # If match found, flip tracking bool to true
                if each == bingo_cards[c][b][a][0]:
                    bingo_cards[c][b][a][1] = 1
    # Check for and stop when Bingo complete
                if (bingo_cards[c][b][0][1] + bingo_cards[c][b][1][1] + bingo_cards[c][b][2][1] + bingo_cards[c][b][3][1] + \
                        bingo_cards[c][b][4][1]) == 5 or (bingo_cards[c][0][a][1] + bingo_cards[c][1][a][1] + \
                        bingo_cards[c][2][a][1] + bingo_cards[c][3][a][1] + bingo_cards[c][4][a][1] == 5):
                    bingo = True
                    print("**********BINGO!***********")
                    winning_num = bingo_cards[c][b][a][0]
                    winning_card = c
                    break

# Add up uncalled numbers on winning card
uncalled = 0
for number_list in bingo_cards[winning_card]:
    print(number_list)
    for number in number_list:
        if number[1] == 0:
            # print("Uncalled: " + str(uncalled))
            # print("Number: " + str(number[0]))
            uncalled += number[0]

# Print final data
print("Last number called:")
print(winning_num)
print("Total of uncalled numbers on card:")
print(uncalled)
total = winning_num * uncalled
print("Total:")
print(total)
