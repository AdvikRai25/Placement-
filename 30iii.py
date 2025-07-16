import random
name1 = input(" Enter name of Player 1: ").strip().capitalize()
name2 = input(" Enter name of Player 2: ").strip().capitalize()

print("\n Computer has fixed 5 unique numbers between 1 and 10\n")

nums = []
while len(nums) < 5:
    num = random.randint(1, 10)
    if num not in nums:
        nums.append(num)

player1 = []
player2 = []
all_guessed = []

s1 = 0
s2 = 0

print("-----------------------------------------------------")
for i in range(3):
    print(f"--------------------- Round {i+1} ---------------------")


    while True:
        try:
            print(f"{name1}'s turn:")
            num = int(input("Enter a number between 1 and 10: "))
            if num < 1 or num > 10:
                print(" Number out of range! Try again.")
                continue
            if num in all_guessed:
                print(" This number has already been guessed! Try again.")
            else:
                all_guessed.append(num)
                if num in nums:
                    print(" CORRECT!")
                    player1.append(num)
                    s1 += 1
                else:
                    print(" WRONG!")
                break
        except ValueError:
            print(" Please enter a valid integer between 1 and 10.")
    print("-----------------------------------------------------")

    # Player 2's turn
    while True:
        try:
            print(f"{name2}'s turn:")
            num = int(input("Enter a number between 1 and 10: "))
            if num < 1 or num > 10:
                print(" Number out of range! Try again.")
                continue
            if num in all_guessed:
                print(" This number has already been guessed! Try again.")
            else:
                all_guessed.append(num)
                if num in nums:
                    print(" CORRECT!")
                    player2.append(num)
                    s2 += 1
                else:
                    print(" WRONG!")
                break
        except ValueError:
            print(" Please enter a valid integer between 1 and 10.")
    print("-----------------------------------------------------")

# Final Summary
print("\n===========  GAME SUMMARY ===========")
print("Numbers fixed by Computer:", nums)
print(f"{name1}'s guesses: {player1} | Score: {s1}")
print(f"{name2}'s guesses: {player2} | Score: {s2}")

if s1 > s2:
    print(f"\n {name1} is the WINNER!")
elif s2 > s1:
    print(f"\n {name2} is the WINNER!")
else:
    print("\n It's a DRAW!")
