"""This module """

import threading
import time
from city_processor import CityOverheadTimes
from city_processor import CityDatabase
from city_processor import ISSDataRequest
from city_processor import CityOverheadTimes
from city_processor import OverheadPassEvent


class CityOverheadTimeQueue:
    """This class is used to hold the calculated CityOverheadTimes objects
    in a Queue."""

    def __init__(self):
        self.data_queue = []

    def put(self, overhead_times: CityOverheadTimes) -> None:
        self.data_queue.append(overhead_times)

    def get(self) -> CityOverheadTimes:
        first = self.data_queue[0]
        del self.data_queue[0]
        return first

    def __len__(self) -> int:
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    """This thread class is responsible for looping over each city
    and pass it to the get_overhead_pass method."""

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """It loops over each city and pass it to the get_overhead_pass
        method, and add the city to the queue."""
        dr = ISSDataRequest()
        count = 0
        for city in self.cities:
            count += 1
            self.queue.put(dr.get_overhead_pass(city))
            if count % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):
    """This thread class is responsible for consuming data from the
    queue and printing it out to the console."""

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        """It gets an item from the queue and print it to the console
        and then sleep for 0.5 seconds, while data_incoming is true
        or the queue is not empty."""
        while self.data_incoming is True or len(self.queue) > 0:
            print(self.queue.get())
        if len(self.queue) == 0:
            time.sleep(0.75)


def main():
    q = CityOverheadTimeQueue()
    db = CityDatabase('city_locations.xlsx')
    queue = CityOverheadTimeQueue()
    producer_thread = ProducerThread(db.city_db, queue)
    consumer_thread = ConsumerThread(queue)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.start()


if __name__ == '__main__':
    main()

