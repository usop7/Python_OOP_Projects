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
        """Print all biders in in name : highest bid format."""
        bidders = {bidder.name: bidder.highest_bid for bidder in self._bidders}
        print(bidders)


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
        current_bidder = "Starting Bid"
        if self.current_bidder is not None:
            current_bidder = self.current_bidder.name
        if bid_price > self._highest_current_bid:
            print(f"{bidder.name} bidded {bid_price} in response to "
                  f"{current_bidder}'s bid of {self.current_bid}!")
            self._highest_current_bid = bid_price
            self._highest_current_bidder = bidder
            self.start_new_bids()

    def start_new_bids(self):
        """Notify all bidders of the new bid price and bidder."""
        for bidder in self._bidders:
            if bidder != self._highest_current_bidder:
                bid_price = bidder(self)
                if bid_price > 0:
                    self.update_bid(bid_price, bidder)

    def __str__(self):
        return f"{self.current_bidder} - {self.current_bid}"


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

    def __str__(self):
        return f"{self.name} - {self._budget}"

    name = property(get_name)

    highest_bid = property(get_highest_bid, set_highest_bid)

    bid_probability = property(get_bid_probability)

    def __call__(self, auctioneer):
        """
        Places a new bid with the auctioneer, after checking the budget and
        probability, and updates the its highest bid price.
        :param auctioneer: Auctioneer
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
    while not valid:
        starting_price = input("Please type the starting price: ")
        if starting_price.isdecimal():
            valid = True

    valid = False
    num_of_bidders = 0
    while not valid:
        num_of_bidders = input("Please type the number of bidders: ")
        if num_of_bidders.isdigit():
            valid = True

    num = 1
    while num <= int(num_of_bidders):
        print(f"Please provide the details of the bidder {num}")
        name = input("name: ")
        budget = input("budget: ")
        bid_increase_perc = input("bid increase percentage(greater than 1): ")
        bidders.append(Bidder(name, float(budget), float(bid_increase_perc)))
        num += 1

    my_auction = Auction(bidders, item_name, float(starting_price))
    print(f"Starting Auction!!\n----------------------\n"
          f"Auctioning {name} starting at {starting_price}.")
    my_auction.start_auction()

    print(f"\nThe winner of the auction is")

    my_auction.print_bidders()



if __name__ == '__main__':
    main()





