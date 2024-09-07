import art1

print(art1.logo)

dec = True
bid = {}

def find_highest(bid_dict):
    highest_bid = 0
    winner = ""

    max(bid_dict)
    
    for i in bid_dict:
        bid_amnt = bid_dict[i]
        if bid_amnt > highest_bid :
            highest_bid = bid_amnt
            winner = i

    print(f"The winner is {winner} with a bid of ${highest_bid} ")


while dec:
    name = input("Enter your name ")
    price = float(input("What is your bid? "))
    bid[name] = price
    others = input("Are there any other bidders? : yes/no ").lower()
    if others == "no":
        dec = False
        find_highest(bid)
    elif others == "yes":
        print("\n"*30)
        
      




