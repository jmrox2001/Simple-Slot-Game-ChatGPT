import random

class SlotMachine:
    def __init__(self, symbols, bet_amount):
        self.symbols = symbols
        self.bet_amount = bet_amount
        self.balance = 0
        self.jackpot_multiplier = 0
        self.free_spins_count = 0
        # Define the default weights for each symbol
        self.default_weights = {"Cherry": 11, "Bar": 16, "Seven": 22, "Free Spin": 20}
        # Define the weights for symbols during free spins
        self.free_spin_weights = {"Cherry": 20, "Bar": 30, "Seven": 40, "Free Spin": 18}

    def spin(self):
        # Use random.choices with weights parameter to select symbols
        if self.free_spins_count > 0:
            weights = self.free_spin_weights.values()
        else:
            weights = self.default_weights.values()
        return [random.choices(self.symbols, weights=list(weights))[0] for _ in range(3)]

    def award_free_spins(self, spin_result):
        # Check if there are three "Free Spin" symbols
        if spin_result.count("Free Spin") == 3:
            print("Congratulations! You got 20 free spins and won 10x your bet!")
            self.free_spins_count += 20
            return self.bet_amount * 10  # Pay 10 times the current bet for achieving free spins
        else:
            return 0

def initialize_game():
    symbols_list = ["Cherry", "Bar", "Seven", "Free Spin"]
    custom_balance = int(input("Enter your starting balance: "))
    slot_machine = SlotMachine(symbols_list, 1)  # Minimum bet set to 1 point
    slot_machine.balance = custom_balance
    return slot_machine

def print_symbol(symbol):
    return f" {symbol} "

def display_spin_result(spin_result):
    print("Spin Result:")
    print("------------")
    print("|" + print_symbol(spin_result[0]) + "|" + print_symbol(spin_result[1]) + "|" + print_symbol(spin_result[2]) + "|")
    print("------------")

def main():
    slot_machine = initialize_game()

    while True:
        print(f"\nCurrent Balance: {slot_machine.balance} points | Current Bet: {slot_machine.bet_amount} points | Free Spins: {slot_machine.free_spins_count}")
        action = input("Type 'b' to change your bet, 'exit' to quit, or just press Enter to spin the slot machine: ").lower()

        if action == 'b':
            new_bet = int(input("Enter your new bet amount: "))
            if new_bet >= 1:
                slot_machine.bet_amount = new_bet
                print(f"Bet amount set to {new_bet} points.")
            else:
                print("Invalid bet amount. Please enter a value of 1 point or more.")

        elif action == 'exit':
            break

        elif not action:  # If the user just presses Enter
            if slot_machine.free_spins_count > 0:
                slot_machine.free_spins_count -= 1
                during_free_spins = True
            else:
                during_free_spins = False

            spin_result = slot_machine.spin()
            display_spin_result(spin_result)
            free_spin_winnings = slot_machine.award_free_spins(spin_result)

            # Only deduct the bet amount if it's not a free spin
            if not during_free_spins:
                slot_machine.balance += free_spin_winnings - slot_machine.bet_amount
            else:
                slot_machine.balance += free_spin_winnings  # Add free spin winnings directly

            if free_spin_winnings > 0:
                print(f"Congratulations! You won {free_spin_winnings} points!")
            else:
                print("Try again!")

            if slot_machine.balance <= 0:
                print("Out of points. Game over.")
                break

    print("Sorry! You Lost!")

if __name__ == "__main__":
    main()
