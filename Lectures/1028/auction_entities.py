"""
Implements the observer pattern and simualates a simple auction.
"""
import random
from pympler import tracker


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            if self._highest_bidder != bidder:
                bidder(self)

    @property
    def current_bid(self):
        return self._highest_bid

    @property
    def highest_bidder(self):
        return self._highest_bidder

    def accept_bid(self, bid, bidder="Starting Bid"):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            self._highest_bid = bid
            self._highest_bidder = bidder
            self._notify_bidders()
        else:
            raise ValueError("Bid amount is less than the going rate.")


class Bidder:

    def __init__(self, name, money=100, threat_chance=0.35, bid_increase=1.1):
        self.name = name
        self.threat_chance = threat_chance
        self.money = money
        self.bid_increase = bid_increase
        self.highest_bid = 0

    def __call__(self, auctioneer):
        random_roll = random.random()
        if random_roll <= self.threat_chance and \
                (self.money >= auctioneer.current_bid * self.bid_increase):
            try:
                new_bid = auctioneer.current_bid * self.bid_increase
                print(f"{self} bidded {new_bid} in response to "
                      f"{auctioneer.highest_bidder}'s bid of "
                      f"{auctioneer.current_bid}!")
                self.highest_bid = new_bid
                auctioneer.accept_bid(new_bid, self)
            except ValueError:
                print(f"{self} attempted to bid {new_bid} but the bid was too "
                      f"low!")

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.auctioneer = Auctioneer()
        self.bidders = bidders
        for bidder in self.bidders:
            self.auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at {start_price}")
        self.auctioneer.accept_bid(start_price)
        print(f"The winner of the auction is: {self.auctioneer.highest_bidder}"
              f" at ${self.auctioneer.current_bid}")
        bidder_bids = {bidder.name: bidder.highest_bid for bidder in
                       self.bidders}
        for bidder,bid in bidder_bids.items():
            print(f"Bidder: {bidder}\tHighest Bid: {bid}")


def main():
    tr = tracker.SummaryTracker()
    print(random.random())
    user_input = None
    bidders = []

    # Hardcoding the bidders for the profiling demo.
    bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
    bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
    bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
    bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
    bidders.append(Bidder("Scott", 4000, random.random(), 2))

    # Ideally we would do something like this, probably generate the
    # threat and increase values though, I'm lazy.

    # while user_input != 'q':
    #     bidder_name = input("Enter bidder name: ")
    #     bidder_money = float(input("Enter bidder budget: "))
    #     bidder_threat = float(input("Enter bid probability (0-1): "))
    #     bidder_increase = float(input("Enter the percentage increase of the "
    #                                   "new bid: "))
    #     bidders.append(Bidder(bidder_name, bidder_money, bidder_threat,
    #                           bidder_increase))
    #     user_input = input("Continue? q for quit, y for yes")

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)
    print("-" * 50)
    tr.print_diff()


if __name__ == '__main__':
    main()
