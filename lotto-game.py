import random
import sys

wallet_amnt = 10

def lottoDraw(lst):
    winning_nums = random.sample(lst, 5)
    return winning_nums

def lottoPick():
    ticket_lst = []
    passing = False
    while True:
        if passing == True:
            break
        num1 = input("Enter your first number: ")
        test1 = checkNum(num1, ticket_lst)
        if test1 == True:
            ticket_lst.append(int(num1))
            while True:
                if passing == True:
                    break
                num2 = input("Enter your second number: ")
                test2 = checkNum(num2, ticket_lst)
                if test2 == True:
                    ticket_lst.append(int(num2))
                    while True:
                        if passing == True:
                            break
                        num3 = input("Enter your third number: ")
                        test3 = checkNum(num3, ticket_lst)
                        if test3 == True:
                            ticket_lst.append(int(num3))
                            while True:
                                if passing == True:
                                    break
                                num4 = input("Enter your fourth number: ")
                                test4 = checkNum(num4, ticket_lst)
                                if test4 == True:
                                    ticket_lst.append(int(num4))
                                    while True:
                                        num5 = input("Enter your fifth number: ")
                                        test5 = checkNum(num5, ticket_lst)
                                        if test5 == True:
                                            ticket_lst.append(int(num5))
                                            passing = True
                                            break
                                        else:
                                            print("Stupid. Try again.")
                                else:
                                    print("Stupid. Try again.")        
                        else:
                            print("Stupid. Try again.")   
                else:
                    print("Stupid. Try again.")
        else:
            print("Stupid. Try again.")
    return ticket_lst

def checkNum(num, ticket_lst):
    global wallet_amnt
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if num == "q":
        print(f"Wallet: ${wallet_amnt}")
        sys.exit()
    elif num in alpha:
        return False
    else:
        dig = int(num)
        if dig >= 1 and dig <= 50 and dig not in ticket_lst:
            return True
        else:
            print("Invalid number, please try again.")
            return False
    
def compareResults(ticket_lst, winning_nums):
    count = 0
    for num in winning_nums:
        for num2 in ticket_lst:
            if num == num2:
                count += 1
    if count == 0:
        print("You won nothing lol")
        winnings = 0
    elif count == 1:
        print("You won $4!")
        winnings = 4
    elif count == 2:
        print("You won $7!")
        winnings = 7
    elif count == 3:
        print("You won $50!")
        winnings = 50
    elif count == 4:
        print("You won $100!")
        winnings = 100
    elif count == 5:
        print("You won $100000!")
        winnings = 100000
    return winnings


def lottoGame():
    global wallet_amnt
    one_fifty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    print("\n")
    print("Lotto Number Picker")
    print("\n")
    print("Pick 5 numbers between 1-50. These cannot be changed once picked, so choose carefully.")
    print("To quit, enter q")
    print("\n")
    ticket = lottoPick()
    ticket_str = lst_to_string(ticket)
    print("\n")
    print(f"Your numbers are: {ticket_str}")
    winning_nums_lst = lottoDraw(one_fifty)
    winning_nums_str = lst_to_string(winning_nums_lst)
    print(f"The winning numbers are: {winning_nums_str}")
    print("\n")
    winnings = compareResults(ticket, winning_nums_lst)
    wallet_amnt += winnings
    print(f"Wallet: ${wallet_amnt}")
    print("\n")
    # hi
def walletCheck():
    global wallet_amnt
    if wallet_amnt < 2:
        print("lol u broke gg")
        print(f"Wallet: ${wallet_amnt}")
        sys.exit()

def lst_to_string(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    new_str = " ".join(lst)
    return new_str

def main():
    global wallet_amnt
    while True:
        answer = input("Would you like to play the lotto? Entry costs $2. (y/n): ")
        answer.lower()
        if answer == "y":
            walletCheck()
            wallet_amnt -= 2
            print(f"Wallet: ${wallet_amnt}")
            lottoGame()
        elif answer == "n":
            answer2 = input("You miss 100 percent of the shots you don't take. Do you really want to quit? (y/n): ")
            answer2.lower()
            if answer2 == "y":
                answer3 = input("Are you REALLY sure? (y): ")
                answer3.lower()
                if answer3 == "y":
                    print("Your the boss. See ya around...")
                    print(f"Wallet: ${wallet_amnt}")
                    sys.exit()
            elif answer2 == "n":
                print("Attaboy, that's the spirit!")
                walletCheck()
                wallet_amnt -= 2
                lottoGame()
                # hi

main()
