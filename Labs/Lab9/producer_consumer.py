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

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        dr = ISSDataRequest()
        count = 0
        for city in self.cities:
            count += 1
            self.queue.put(dr.get_overhead_pass(city))
            if count % 5 == 0:
                time.sleep(1)


def main():
    q = CityOverheadTimeQueue()
    db = CityDatabase('city_locations.xlsx')
    queue = CityOverheadTimeQueue()
    producer_thread = ProducerThread(db.city_db, queue)
    producer_thread.start()
    producer_thread.join()
    print(*queue.data_queue, sep='')


if __name__ == '__main__':
    main()

