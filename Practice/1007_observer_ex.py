from enum import Enum


class TrafficLightStatus(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2
    INVALID = 3


class TrafficLightCore:

    def __init__(self):
        self._light = TrafficLightStatus.INVALID
        self._observers = []

    def attach_observer(self, callback):
        self._observers.append(callback)

    def execute_callbacks(self):
        for observer in self._observers:
            observer(self._light)

    @property
    def traffic_light(self):
        return self._light

    @traffic_light.setter
    def traffic_light(self, value):
        self._light = value
        self.execute_callbacks()


class CarObserver:

    def __init__(self):
        self.light_reactions = {
            TrafficLightStatus.YELLOW: "Slow Down",
            TrafficLightStatus.RED: "Stop",
            TrafficLightStatus.GREEN: "Go",
            TrafficLightStatus.INVALID: "I don't know what to do, freak out"
        }

    def react_to_light(self, traffic_light):
        print(self.light_reactions[traffic_light])


def main():
    car_list = [CarObserver(), CarObserver(), CarObserver()]
    traffic_light = TrafficLightCore()
    for car in car_list:
        traffic_light.attach_observer(car.react_to_light)

    traffic_light.traffic_light = TrafficLightStatus.YELLOW
    traffic_light.traffic_light = TrafficLightStatus.GREEN


if __name__ == '__main__':
    main()