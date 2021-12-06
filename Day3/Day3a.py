def most_frequent(List):
    return max(set(List), key = List.count)


def least_frequent(List):
    return min(set(List), key = List.count)


with open("data.txt") as file:
    lines = file.read().splitlines()

gamma = []
epsilon = []
digits = []
i = 0

while i < 12:
    for line in lines:
        line[i]
        digits.append(line[i])
    gamma.append(most_frequent(digits))
    digits.clear()
    i += 1

i = 0
while i < 12:
    for line in lines:
        line[i]
        digits.append(line[i])
    epsilon.append(least_frequent(digits))
    digits.clear()
    i += 1

gamma_rate_bi = ("".join([str(i) for i in gamma]))
gamma_rate_int = int(gamma_rate_bi, 2)
epsilon_rate_bi = ("".join([str(i) for i in epsilon]))
epsilon_rate_int = int(epsilon_rate_bi, 2)

total = gamma_rate_int * epsilon_rate_int

print(total)