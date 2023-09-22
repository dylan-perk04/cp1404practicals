MENU_DISPLAY = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("What is your name?: ")
print(MENU_DISPLAY)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU_DISPLAY)
    choice = input(">>> ").upper()
print("Finished.")
