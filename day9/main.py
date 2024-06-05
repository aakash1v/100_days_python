import art

print(art.logo)

other_user = True
bids={}

def find_highest_bidder(bidding_record):
    highest_bid =0
    winner = ""

    for bidder in bidding_record:
        bid = bidding_record[bidder]

        if bid >highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while(other_user):
    name = input("Enter your name :")
    price= int(input("Enter your bid price :$"))
    bids[name] = price

    choice = input("Is there any other user who want to bid")
    
    if choice.lower() not in ['yes','y','yeah','yep']:
        other_user = False


find_highest_bidder(bids)
