while True:
    user_money = input("How much money would you like me to convert to change?\n$")
    try:
        user_money = round(float(user_money) * 100)
        break
    except ValueError:
        print("Please enter a number!")

quarters = user_money // 25
user_money %= 25

dimes = user_money // 10
user_money %= 10

nickles = user_money // 5
user_money %= 5

print(f"Your change is:\n{quarters} quarter(s)\n{dimes} dime(s)\n{nickles} nickle(s)\n{user_money} pennie(s)")
