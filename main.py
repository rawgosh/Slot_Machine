import random

MAX_LINES = 3 #creating a global constant
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "1" : 4,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 3,
    "6" : 3,
    "7" : 5,
    "8" : 3,
    "9" : 5
}

symbol_value = {
    "1" : 4,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 3,
    "6" : 3,
    "7" : 5,
    "8" : 3,
    "9" : 5
} #value of a symbol to multiply

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #how many lines will it check
        symbol = columns[0][line] #first symbol of the row
        for column in columns:
            symbol_to_check = column[line] #symbol at the current row
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) #recors on which line the player won
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] #creating a list that hold the symbol
    for symbol, symbol_count in symbols.items(): # .items() -> gets the key and the value associated with the dictionary
        for _ in range(symbol_count): #underscore is an anonymous variable
            all_symbols.append(symbol) #adding the symbol to the list
    
    #columns = [[],[],[]] #this nested list represent the value in the column
    columns = [] #defining the columns list
    for _ in range(cols): #generating a column for every single column we have
        column = []
        current_symbols = all_symbols[:] #creating the copy of the list
        for _ in range(rows):
            value = random.choice(all_symbols) #random value from the list
            current_symbols.remove(value) #finds the first instance of the list and removes it
            column.append(value) #adding the value to the column
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #gives the index and item as we loop through
            if i != len(columns) - 1: #this runs until it is the maximum index
                print(column[row], end = " | ") #end tells the print what the line ends with
            else:
                print(column[row], end = "")
        
        print()

def deposit(): #responsible to take the amount deposited
    while True:
        amount = input("Enter an amount to deposit : $")
        if amount.isdigit(): #checks if the input is digit or not
            amount = int(amount) #converts ito integer
            if amount > 0:
                break #breaks from the while loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter an actual amount.")
    
    return amount #returns the amount 

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter lines in num.")
    
    return lines

def get_bet():
    while True:
        amount = input("Enter amount to bet on each line : $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a num.")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance: #checks if the bet is greater than the balance
            print(f"Not enough amount to bet. Your current balance is : ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    if winnings > 0: #runs only if the player has won
        print(f"You won ${winnings}.")
        print(f"You won on lines: ", *winning_lines) #unpack operator => passes every single line in which player won
    else:
        print(f"You lost ${total_bet}")
    return winnings - total_bet #reduces the balance on each loss

#everything gets used from main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You have ${balance} left.")

main()
