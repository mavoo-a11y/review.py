import random 

def spin_row():
    symbols = ['🐼','🐨','🐻','🦁','🐯']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
  print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🐼':
            return bet * 2
        elif row[0] == '🐨':
            return bet * 5
        elif row[0] == '🐻':
            return bet * 10
        elif row[0] == '🦁':
            return bet * 20
        elif row[0] == '🐯':
            return bet * 30
        
    return 0
    
def main():
    balance = 100
    print("Welcome to Spin the wheel")
    print("Symbols: 🐼 🐨 🐻 🦁 🐯")

    while balance > 0:
      print(f"\nCurrent balance: ${balance}")
      bet = input("Place your bet amount: ")

      if not bet.isdigit():
         print("Invalid bet amount. Please enter the amount in numbers.") 
         continue

      bet = int(bet)

      if bet == 0:
          break

      if bet > balance:
         print("Insufficient balance. Please enter a lower amount.")
         continue

      if bet <= 0:
         print("Invalid bet amount.")
         continue

      balance -= bet

      row = spin_row()
      print("\nSpinning ....\n")
      print_row(row)

      payout = get_payout(row, bet)

      if payout ==0:
         print("No payout this time.")

         if payout > 0:
             print(f"Congratulations! You won ${payout}")
         else:
             print("Sorry, you lost this round.")

         balance += payout

      if balance == 0:
          break

      play_again = input("Do you want to play again? (Y/N): ").upper()

      if play_again != 'Y':
          break

    print(f"\n Game over! Your final balance is ${balance}")

if __name__ == '__main__':
    main()