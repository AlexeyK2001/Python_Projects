# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#         }
#     "Turkiye": {
#         "cities_visited": ["Alania", "Antalia", "Kemer", "Bodrum"],
#         "total_visits": 5
#     }
# }

#Nesting a dictionary in a list

# travel_log = [
#     {
#      "country: France", 
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12
#     },
#     {
#      "country: Turkiye", 
#      "cities_visited": ["Alania", "Antalia", "Kemer", "Bodrum"],
#      "total_visits": 5
#     },
# ]

# AUCTION
import os
def clear_terminal():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    global other_bids, max_bid, max_bid_name, bids
    other_bids = 'y'
    bids = {}
    max_bid = 0
    max_bid_name = ''
    while other_bids == 'y':
        name = input("Welcome to the secret auction program! \n What is your name?: ")
        bid_size = int(input("What is your bid?: $"))
        if bid_size > max_bid:
            max_bid = bid_size
            max_bid_name = name
        bids[name] = bid_size
        other_bids = input("Are there any other bidders? (Y/N) ").lower()
        clear_terminal()
start()
print(bids)
print(f"The winner of the auction is {max_bid_name}, with a bid of ${max_bid}. ")

    