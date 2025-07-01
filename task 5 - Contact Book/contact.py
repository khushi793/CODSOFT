# 📇 Refactored Contact Manager (List + Dictionary)

contact_list = []  # Stores individual contact dictionaries

# ➕ Add New Entry
def create_entry():
    full_name = input("Enter Full Name: ")
    mobile = input("Enter Phone Number: ")
    mail = input("Enter Email Address: ")
    location = input("Enter Address: ")

    entry = {
        "name": full_name,
        "phone": mobile,
        "email": mail,
        "address": location
    }
    contact_list.append(entry)
    print("✅ Contact successfully added!\n")

# 📃 Display All Contacts
def show_all_contacts():
    if not contact_list:
        print("⚠️ No contacts available.\n")
        return
    print("\n📋 Contact Directory:")
    for idx, entry in enumerate(contact_list, start=1):
        print(f"{idx}. {entry['name']} - {entry['phone']}")
    print()

# 🔍 Search Contacts
def find_entry():
    search_input = input("🔎 Enter name or number to search: ").lower()
    for entry in contact_list:
        if search_input in entry["name"].lower() or search_input in entry["phone"]:
            print("\n📌 Match Found:")
            print(f"Name   : {entry['name']}")
            print(f"Phone  : {entry['phone']}")
            print(f"Email  : {entry['email']}")
            print(f"Address: {entry['address']}\n")
            return
    print("❌ No match found.\n")

# 📝 Modify Contact
def edit_entry():
    name_to_edit = input("Enter the name of the contact to modify: ").lower()
    for entry in contact_list:
        if entry["name"].lower() == name_to_edit:
            print("✏️ Leave fields blank to keep current value.")
            entry["name"] = input(f"New Name ({entry['name']}): ") or entry["name"]
            entry["phone"] = input(f"New Phone ({entry['phone']}): ") or entry["phone"]
            entry["email"] = input(f"New Email ({entry['email']}): ") or entry["email"]
            entry["address"] = input(f"New Address ({entry['address']}): ") or entry["address"]
            print("✅ Contact updated!\n")
            return
    print("❌ Contact not found.\n")

# ❌ Delete Contact
def remove_entry():
    name_to_remove = input("Enter the name of the contact to delete: ").lower()
    for idx, entry in enumerate(contact_list):
        if entry["name"].lower() == name_to_remove:
            del contact_list[idx]
            print("🗑️ Contact deleted!\n")
            return
    print("❌ Contact not found.\n")

# 🧭 Main Menu Interface
def launch_menu():
    while True:
        print("📱 ====== CONTACT BOOK MENU ======")
        print("1️⃣  Add New Contact")
        print("2️⃣  Show All Contacts")
        print("3️⃣  Search Contact")
        print("4️⃣  Edit Contact")
        print("5️⃣  Delete Contact")
        print("6️⃣  Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            create_entry()
        elif choice == '2':
            show_all_contacts()
        elif choice == '3':
            find_entry()
        elif choice == '4':
            edit_entry()
        elif choice == '5':
            remove_entry()
        elif choice == '6':
            print("👋 Goodbye! Thanks for using Contact Book.")
            break
        else:
            print("❗ Invalid choice. Please select between 1 to 6.\n")

# ▶️ Start the Program
if __name__ == "__main__":
    launch_menu()
