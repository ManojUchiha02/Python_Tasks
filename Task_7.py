class BN_500():
    def __init__(self, amount):
        self.amount = amount
    def count(self):
        No_of_Notes = self.amount // 500
        return No_of_Notes
    def remaining(self):
        Amount_Remaining = self.amount % 500
        return Amount_Remaining
class BN_200():
    def count(self, remaining_a500):
        No_of_Notes = remaining_a500 // 200
        return No_of_Notes
    def remaining(self, remaining_a500):
        Amount_Remaining = remaining_a500 % 200
        return Amount_Remaining
class BN_50():
    def count(self, remaining_a200):
        No_of_Notes = remaining_a200 // 50
        return No_of_Notes
    def remaining(self, remaining_a200):
        Amount_Remaining = remaining_a200 % 50
        return Amount_Remaining

try:
    while True:
        user_choice = input("Do you want to enter amount for withdrawal? (Yes/No): ").strip().lower()
        if user_choice == 'no' or user_choice == 'exit':
            break
        elif user_choice == 'yes':
            amount = int(input("Enter required amount:"))
            BN500 = BN_500(amount)
            BN200 = BN_200()
            BN50 = BN_50()
            remaining_a500 = BN500.remaining()
            remaining_a200 = BN200.remaining(remaining_a500)
            BN50.remaining(remaining_a200)
            if BN50.remaining(remaining_a200) == 0:
                print(f"Number of 500 Notes: {BN500.count()}")
                print(f"Number of 200 Notes: {BN200.count(remaining_a500)}")
                print(f"Number of 50 Notes: {BN50.count(remaining_a200)}")
            else:
                print("Enter a valid amount in multiples of 50, 200, 500")
except ValueError:
    print("Please try again with valid number")
