"""This module contains the queue for CityOverheadTimes objects
and and produce/consumer threads to process the cities."""

import threading
import time
from city_processor import CityDatabase
from city_processor import ISSDataRequest
from city_processor import CityOverheadTimes


class CityOverheadTimeQueue:
    """This class is used to hold the calculated CityOverheadTimes objects
    in a Queue."""

    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_times: CityOverheadTimes) -> None:
        with self.access_queue_lock:
            self.data_queue.append(overhead_times)

    def get(self) -> CityOverheadTimes:
        with self.access_queue_lock:
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
            time.sleep(0.5)
            if len(self.queue) == 0:
                time.sleep(0.75)
            if len(self.queue) == 0:
                self.data_incoming = False


def main():
    db = CityDatabase('city_locations_test.xlsx')
    cities = db.city_db
    count = len(cities)
    queue = CityOverheadTimeQueue()

    # create 3 producer threads
    producer_thread = ProducerThread(cities[:count//3], queue)
    producer_thread2 = ProducerThread(cities[count//3:count//3*2], queue)
    producer_thread3 = ProducerThread(cities[count//3*2:], queue)

    consumer_thread = ConsumerThread(queue)
    producer_thread.start()
    producer_thread2.start()
    producer_thread3.start()
    producer_thread.join()
    consumer_thread.start()


if __name__ == '__main__':
    main()

