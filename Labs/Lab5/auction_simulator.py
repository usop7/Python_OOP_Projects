"""This module showcases Auction House simulation that consists of
an Auction, an Auctioneer and a number of Bidders."""

import random


class Auction:
    """This class represents an Auction that starts the simulation."""

    def __init__(self, bidders, item, starting_price):
        """
        Initializes an Auction object.
        :param bidders: List
        :param item: String
        :param starting_price: float
        """
        self._bidders = bidders
        self._item = item
        self._starting_price = starting_price
        self._auctioneer = Auctioneer(self._bidders, self._starting_price)

    def start_auction(self):
        """Starts the auction."""
        self._auctioneer.start_new_bids()

    def print_bidders(self):
        """Print all bidders in name : highest bid format."""
        bidders = {bidder: bidder.highest_bid for bidder in self._bidders}
        print("\nHighest Bids Per Bidder")
        for bidder, price in bidders.items():
            print(f"Bidder: {bidder.name}\t Bid: {price}")

    def print_winner(self):
        """Print the bidder who won the auction."""
        winner = None
        winning_price = 0
        for bidder in self._bidders:
            if bidder.highest_bid > winning_price:
                winner = bidder.name
                winning_price = bidder.highest_bid
        print(f"\nThe winner of the auction is: {winner} at ${winning_price}")


class Auctioneer:
    """This class represents an Auctioneer which is responsible for
    maintaining a list of bidders and notifying them the new bid."""

    def __init__(self, bidders, starting_price):
        """
        Initializes an Auctioneer object.
        :param bidders: List
        """
        self._bidders = bidders
        self._highest_current_bid = starting_price
        self._highest_current_bidder = None

    def get_current_bid(self):
        return self._highest_current_bid

    def get_current_bidder(self):
        return self._highest_current_bidder

    current_bid = property(get_current_bid)

    current_bidder = property(get_current_bidder)

    def update_bid(self, bid_price, bidder):
        """Update the highest current bid price and highest bidder,
         and start a new bid in turn."""
        bidder_info = "Starting Bid"
        if self.current_bidder is not None:
            bidder_info = self.current_bidder.name
        print(f"{bidder.name} bidded {bid_price} in response to "
              f"{bidder_info}'s bid of {self.current_bid}!")
        self._highest_current_bid = bid_price
        self._highest_current_bidder = bidder
        self.start_new_bids()

    def start_new_bids(self):
        """Start a new bid by notifying all bidders except for the
        current highest bidder."""
        for bidder in self._bidders:
            if bidder != self._highest_current_bidder:
                bid_price = bidder(self)
                if bid_price > self.current_bid:
                    self.update_bid(bid_price, bidder)


class Bidder:
    """This class represents a bidder who places bids during an auction."""

    def __init__(self, name, budget, bid_increase_perc):
        """
        Initializes a Bidder object.
        :param name: String
        :param budget: float
        :param bid_increase_perc: float
        """
        self._name = name
        self._budget = budget
        self._bid_probability = random.random()
        self._bid_increase_perc = bid_increase_perc
        self._highest_bid = 0

    def get_name(self):
        return self._name

    def get_bid_probability(self):
        self._bid_probability = random.random()
        return self._bid_probability

    def get_highest_bid(self):
        return self._highest_bid

    def set_highest_bid(self, price):
        self._highest_bid = price

    name = property(get_name)

    highest_bid = property(get_highest_bid, set_highest_bid)

    bid_probability = property(get_bid_probability)

    def __call__(self, auctioneer):
        """
        Places a new bid with the auctioneer, after checking the budget and
        probability, and updates the its highest bid price.
        :param auctioneer: Auctioneer
        :return float
        """
        curr_bid = auctioneer.current_bid
        bid_price = curr_bid * self._bid_increase_perc
        if bid_price <= self._budget and self.get_bid_probability() > 0:
            self._highest_bid = bid_price
            return bid_price
        return 0


def main():
    """Prompts the user with auction info, and starts the auction."""

    bidders = []
    item_name = input("Please type the name of the item: ")
    valid = False
    starting_price = 0

    # Starting Price
    while not valid:
        try:
            starting_price = float(input("Please type the starting price: "))
        except TypeError as e:
            print("Please type decimal number.")
        else:
            valid = True

    # Number of bidders
    valid = False
    while not valid:
        try:
            num_of_bidders = int(input("Please type the number of bidders: "))
        except TypeError as e:
            print("Please type integer.")
        else:
            valid = True

    # Number of bidders
    valid = False
    num_of_bidders = 0
    while not valid:
        try:
            num_of_bidders = int(
                input("Please type the number of bidders: "))
        except TypeError as e:
            print("Please type an integer.")
        else:
            valid = True

    # Creating bidders
    num = 1
    valid = False
    while num <= int(num_of_bidders):
        print(f"Please provide the details of the bidder {num}")
        name = input("name: ")
        try:
            budget = float(input("budget: "))
        except TypeError as e:
            print("Please type an integer.")
        else:
            valid = True

        bid_increase_perc = input("bid increase percentage(greater than 1): ")
        bidders.append(Bidder(name, float(budget), (1 + random.random())))
        num += 1

    my_auction = Auction(bidders, item_name, float(starting_price))
    print(f"\nStarting Auction!!\n----------------------\n"
          f"Auctioning {name} starting at {starting_price}.")
    my_auction.start_auction()
    my_auction.print_winner()
    my_auction.print_bidders()


if __name__ == '__main__':
    main()





