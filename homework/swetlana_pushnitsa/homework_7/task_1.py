main_number = 7

while True:
    user_input = int(input("Enter a number from 1 to 10: "))
    if user_input != main_number:
        print("Try again")
    elif user_input == main_number:
        print("You win!")
        break
