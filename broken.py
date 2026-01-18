# broken_script.py
import time

print("\n✨ Welcome to the Error Factory ✨")
print("I am about to crash. The question is: How?")
print("----------------------------------------")
print("1. The Black Hole (ZeroDivisionError)")
print("2. The Void (IndexError)")
print("3. The Stranger (NameError)")
print("4. The Identity Crisis (TypeError)")
print("5. The Ghost (KeyError)")

choice = input("\nSelect your disaster (1-5): ")

print(f"\nRunning disaster #{choice}...")
time.sleep(0.5) # Dramatic pause

if choice == "1":
    # Math is hard
    result = 42 / 0

elif choice == "2":
    # Reaching into nothingness
    empty_list = ["me", "myself"]
    print(empty_list[10])

elif choice == "3":
    # Who is she?
    print(my_secret_variable)

elif choice == "4":
    # Mixing types like a maniac
    print("My age is: " + 25)

elif choice == "5":
    # Dictionary lookup fail
    user = {"name": "Vaishnavi", "role": "Hacker"}
    print(user["salary"])

else:
    print("You chose safety. Boring.")