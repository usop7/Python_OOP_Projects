"""This module showcases Auction House simulation that consists of
an Auction, an Auctioneer and a number of Bidders."""


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
        self.highest_current_bidder = None

