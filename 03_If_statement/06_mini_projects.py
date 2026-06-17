# password checker: Checks whether a password is weak and strong.

password = input("Enter password here: ")

if len(password) > 9:
    print("Password is strong")
else:
    print("Password is weak")

# Later you can upgrade this password checker.


# simple ATM Simulation
balance = 1000

print("ATM SIMULATION")
print("1. Check balance")
print("2. Deposit")
print("3. withdraw")

choice = int(input("Enter your choice here: "))

if choice == 1:
    print(f"Balance: ${balance}")

elif choice == 2:
    amount = int(input("Enter the amount here: ")
)
    balance += amount
    print("Balance deposited successfully")
    print(f"New balance: ${balance}")

elif choice == 3:
    amount = int(input("Enter the amount to be withdrawn: "))

    if amount <= balance:
        balance -= amount
        print(f"Remaining Balance: ${amount}")
        
    else:
        print("Insufficient balance!")
    
else:
    print("Invalid choice!")



# Number Guessing Game:

secret = 7

guess = int(input("Guess the number(1-9): "))

if guess == secret:
    print("You have guessed the number.")
elif guess >= secret:
    print("Guess low") 
elif guess < secret:
    print("Guess high")
else:
    pass
