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

    def print_auction_result(self):
        """Print the highest bid, and all the bid prices of bidders."""
        self._auctioneer.print_winner()
        self._auctioneer.print_bidders()


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

    def print_bidders(self):
        """Print all bidders."""
        bidders = {bidder: bidder.highest_bid for bidder in self._bidders}
        print("\nHighest Bids Per Bidder")
        for bidder, price in bidders.items():
            print(bidder)

    def print_winner(self):
        """Print the bidder with the highest bid price."""
        print(f"\nThe winner of the auction is: "
              f"{self.current_bidder} at ${self.current_bid}")


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

    def __str__(self):
        return f"Bidder: {self.name}\t Bid: {self.highest_bid}"


def main():
    """Prompts the user with auction info, and starts the auction."""

    # values to receive from a user
    bidders = []
    item_name = ""
    num_of_bidders = 0
    starting_price = 0

    errors = []
    is_valid = False
    while not is_valid:
        is_valid = True
        item_name = input("Please type the name of the item: ")

        # Starting price
        try:
            starting_price = float(input("Please type the starting price: "))
        except ValueError:
            errors.append("[Error] Starting price should be a decimal number.")
            is_valid = False

        # Number of bidders
        try:
            num_of_bidders = int(input("Please type the number of bidders: "))
        except ValueError:
            errors.append("[Error] Number of bidders should be an integer.")
            is_valid = False

        # print input errors
        for error in errors:
            print(error)

    # Creating bidders
    num = 1
    bidder_name = ""
    is_valid = False
    while num <= int(num_of_bidders) or is_valid is False:
        print(f"Please provide the details of the bidder {num}")
        name = input("name: ")
        try:
            budget = float(input("budget: "))
        except ValueError as e:
            print("[Error] Budget should be a decimal number")
        else:
            is_valid = True
            inc_rate = random.random()
            bidders.append(Bidder(name, float(budget), (1 + inc_rate)))
            num += 1

    # Create Auction with the input values and Start the auction
    my_auction = Auction(bidders, item_name, float(starting_price))
    print(f"\nStarting Auction!!\n----------------------\n"
          f"Auctioning {bidder_name} starting at {starting_price}.")
    my_auction.start_auction()

    # Print out the auction results
    my_auction.print_auction_result()


if __name__ == '__main__':
    main()





