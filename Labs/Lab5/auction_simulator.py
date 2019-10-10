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
                if bidder.



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
        self._curr_bid = 0

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





