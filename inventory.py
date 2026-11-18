import json

FILE_NAME = "inventory.json"


#laod saved parts
def load_inventory():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return{}

#save parts to a file 
def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)

#add a new part
def add_part(inventory):
    name = input("Enter part name:").strip().lower()

    if name == "":
        print("Part name cannot be empty") 
        return

    if name in inventory:
        print("This part already exists")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0 :
            print("Quantity cannot be negative ") 
            return
    except ValueError:
        print("PLease enter a vald number")
        return

    inventory[name] = quantity
    save_inventory(inventory) 
    print("Part added successfully")

#view all parts 

def view_parts(inventory):
    if not inventory:
        print("Inventory is empty")
        return

    print("\n--- Parts Inventory --- ")
    for name, quantity in inventory.items():
        print(f"{name}: {quantity}")

#search for a part

def search_part(inventory):
    name = input("Enter part name:").strip().lower()

    if name in inventory:
        print(f"{name}:{inventory[name]} available")

    else: 
        print("Part not found")
#update quantity
def update_part(inventory):
    name  = input("Enter part name:").strip.lower()
    if name not in inventory:
        print("Part not found")

        try:
            quantity = int(input("Enter new quantity:"))
            if quantity < 0:
                print("Quantitty cannot be negative")
        except ValueError:
              print("Invalid qauntity.")
              return

        inventory[name] = quantity
        save_inventory(inventory)
        inventory[name] = quantity
    save_inventory(inventory)
    print("Quantity updated!")


# Delete a part
def delete_part(inventory):
    name = input("Enter part name: ").strip().lower()

    if name in inventory:
        del inventory[name]
        save_inventory(inventory)
        print("Part deleted!")
    else:
        print("Part not found.")


# Main program
def main():
    inventory = load_inventory()

    while True:
        print("\n===== ROBOTICS PARTS INVENTORY =====")
        print("1. Add part")
        print("2. View all parts")
        print("3. Search part")
        print("4. Update quantity")
        print("5. Delete part")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_part(inventory)
        elif choice == "2":
            view_parts(inventory)
        elif choice == "3":
            search_part(inventory)
        elif choice == "4":
            update_part(inventory)
        elif choice == "5":
            delete_part(inventory)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main()
