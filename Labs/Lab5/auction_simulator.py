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

    def start_auction(self):
        """
        Creates an Auctioneer object and starts the auction.
        """



class Auctioneer:
    """This class represents an Auctioneer which is responsible for
    maintaining a list of bidders and notifying them the new bid."""

    def __init__(self, bidders):
        """
        Initializes an Auctioneer object.
        :param bidders: List
        """
        self._bidders = bidders
        self._highest_current_bid = 0
        self._highest_current_bidder = None

    def get_current_bid(self):
        return self._highest_current_bid

    current_bid = property(get_current_bid)

    def get_current_bidder(self):
        return self._highest_current_bidder

    current_bidder = property(get_current_bidder)

    def notify_bidders(self, new_bidder):
        """Notify all bidders of the new bid price and bidder."""
        for bidder in self._bidders:
            if bidder != new_bidder:
                bidder(self)



    def update_bid(self):
        """"""
        probability = 0
        new_bid = 0
        new_Bidder = None
        for bidder in self._bidders:
            if bidder != self.current_bidder:
                if bidder.bid_probability > probability:
                    new_bid = bidder.




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

    def get_bid_probability(self):
        self._bid_probability = random.random()
        return self._bid_probability

    bid_probability = property(get_bid_probability)

    def __call__(self, auctioneer):
        """
        Places a new bid with the auctioneer.
        :param auctioneer: Auctioneer
        """
        curr_bid = auctioneer.current_bid
        bid_price = curr_bid * self._bid_increase_perc
        if bid_price <= self._budget:
            return bid_price
        else:
            return 0


def main():
    """Prompts the user with auction info, and starts the auction."""

    bidders = []
    item_name = input("Please type the name of the item: ")
    valid = False
    while not valid:
        starting_price = input("Please type the starting price: ")
        if starting_price.isdigit():
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
        bidders.append(Bidder(name, budget, bid_increase_perc))

    my_auction = Auction(bidders, item_name, starting_price)





