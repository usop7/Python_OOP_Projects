"""This module """

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


def main():
    q = CityOverheadTimeQueue()
    db = CityDatabase('city_locations.xlsx')
    dr = ISSDataRequest()
    for city in db.city_db:
        q.put(dr.get_overhead_pass(city))
    print(q.get())


if __name__ == '__main__':
    main()

