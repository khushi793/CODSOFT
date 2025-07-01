import random
import string

class SecureKeyMaker:
    def __init__(self):
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def create_single_password(self, size=12, caps=True, nums=True, special=True):
        pool = self.lower
        must_include = [random.choice(self.lower)]

        if caps:
            pool += self.upper
            must_include.append(random.choice(self.upper))
        if nums:
            pool += self.numbers
            must_include.append(random.choice(self.numbers))
        if special:
            pool += self.symbols
            must_include.append(random.choice(self.symbols))

        while len(must_include) < size:
            must_include.append(random.choice(pool))

        random.shuffle(must_include)
        return ''.join(must_include)

    def batch_passwords(self, total=5, size=12, caps=True, nums=True, special=True):
        return [self.create_single_password(size, caps, nums, special) for _ in range(total)]

# ---------------- USER INTERFACE ----------------

def ask_user_preferences():
    print("=" * 55)
    print(" 🔐 Welcome to SecureKeyMaker - Password Generator")
    print("=" * 55)

    # Length input
    while True:
        try:
            length = int(input("Enter desired password length (8-50): "))
            if 8 <= length <= 50:
                break
            print("❗ Length must be between 8 and 50.")
        except ValueError:
            print("❗ Invalid number, try again.")

    # Character options
    caps = input("Include Uppercase letters? (y/n) [default: y]: ").strip().lower() != 'n'
    nums = input("Include Numbers? (y/n) [default: y]: ").strip().lower() != 'n'
    special = input("Include Special Characters? (y/n) [default: y]: ").strip().lower() != 'n'

    # Number of passwords
    while True:
        try:
            count = int(input("How many passwords to generate? (1-10): "))
            if 1 <= count <= 10:
                break
            print("❗ Choose between 1 and 10.")
        except ValueError:
            print("❗ Invalid number.")

    return length, caps, nums, special, count

def evaluate_strength(password):
    notes = []
    score = 0

    if len(password) >= 12:
        notes.append("✅ Strong length (12+)")
        score += 2
    elif len(password) >= 8:
        notes.append("✔️ Decent length (8+)")
        score += 1
    else:
        notes.append("❌ Too short")

    if any(c.islower() for c in password):
        notes.append("✔️ Has lowercase letters")
        score += 1
    if any(c.isupper() for c in password):
        notes.append("✔️ Has uppercase letters")
        score += 1
    if any(c.isdigit() for c in password):
        notes.append("✔️ Has numbers")
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        notes.append("✔️ Has special characters")
        score += 1

    if score >= 5:
        level = "🟢 Strong"
    elif score >= 3:
        level = "🟡 Medium"
    else:
        level = "🔴 Weak"

    print(f"Password Strength: {level}")
    for note in notes:
        print("  -", note)

def run_secure_key_maker():
    generator = SecureKeyMaker()
    while True:
        try:
            length, caps, nums, special, total = ask_user_preferences()
            print(f"\n🔄 Generating {total} password(s)...\n")

            passwords = generator.batch_passwords(total, length, caps, nums, special)
            print("=" * 55)
            print(" 🔑 Generated Passwords")
            print("=" * 55)

            for idx, pwd in enumerate(passwords, 1):
                print(f"\nPassword {idx}: {pwd}")
                evaluate_strength(pwd)

            again = input("\n🔁 Generate more passwords? (y/n): ").strip().lower()
            if again != 'y':
                print("\n👋 Thanks for using SecureKeyMaker. Stay safe!")
                break
        except KeyboardInterrupt:
            print("\n\n🛑 Interrupted. Exiting SecureKeyMaker.")
            break
        except Exception as err:
            print(f"⚠️ Unexpected Error: {err}")
            break

if __name__ == "__main__":
    run_secure_key_maker()
