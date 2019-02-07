import random

balance = 0

#maybe make a dictionary here
def payout(hits):
    if hits == 1:
        return 4
    elif hits == 2:
        return 7
    elif hits == 3:
        return 100
    elif hits == 4:
        return 50000
    elif hits == 5:
        return 1000000
    elif hits == 6:
        return 25000000
    else:
        return 0

pick6 = []
for digit in range(6):
    pick6.append(random.randint(1,99))

print(f"The winning numbers are {pick6}")

for ticket in range(100000):
    current_ticket = []
    for digit in range(6):
        current_ticket.append(random.randint(1, 99))
    balance -= 2
    hits = 0
    #[i == j for i, j in zip(x_list, y_list)] from stackoverflow.com
    for i, j in zip(pick6, current_ticket):
        if i == j:
            hits += 1
    balance += payout(hits)

print(f"after scratching 100,000 tickets your balance is ${balance}")
