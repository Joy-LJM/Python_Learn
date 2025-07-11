# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import *
print(logo)


bidders={}
continue_bidding=True
while continue_bidding:
  name=input("What is your name?: ")
  bid=input("What is your bid?: $")
  should_continue=input("Are there any other bidders? Type 'Yes' or 'No': ").lower()

  bidders[name]=float(bid)
  if should_continue== 'yes':
    print("\n"*100)

  else:
    continue_bidding=False

    key=max(bidders,key=bidders.get) #{}.get用来从字典中按键取值
    print(f"The winner is {key} with a bid of ${ bidders[key]}")
    
    # method 2

    # max_bid=0
    # winner=""
    # for bidder in bidders:
    #   if(max_bid<bidders[bidder]):
    #     max_bid=bidders[bidder]
    #     winner=bidder
    # print(f"The winner is {winner} with a bid of ${max_bid}")



