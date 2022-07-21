from logo import logo

print(logo)

# create the dictionary
# person's name is the key
# person's bid is the value

auction_bids = {}

def addBid(name, bid):
    auction_bids[name] = bid

def find_highest_bid(auction_bids):
    name = ""
    highest_bid = 0
    for bid in auction_bids:
        if auction_bids[bid] > highest_bid:
            highest_bid = auction_bids[bid]
            name = bid
    return {'name': name, 'bid': highest_bid}

finish = False

while not finish:
    user_choice = input("Do you want to add a bid? 'yes'/'no'")
    if user_choice == 'yes':
        name = input("Type bidder's name: ")
        bid = int(input("How much was the bid: "))
        addBid(name, bid)
    elif user_choice == 'no':
        auction_winner = find_highest_bid(auction_bids)
        print(auction_winner)
        print(f"The highest bid belongs to {auction_winner['name']}, the bid was {auction_winner['bid']}")
        exit()
        

