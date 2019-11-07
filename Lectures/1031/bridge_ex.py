import abc

class IDevice(abc.ABC):

    def __init__(self):
        self.volume = 50
        self.channel = "a_channel"
        self.enabled = True

    @abc.abstractmethod
    def enable(self):
        pass

    @abc.abstractmethod
    def disable(self):
        pass

    @abc.abstractmethod
    def get_volume(self):
        pass

    @abc.abstractmethod
    def set_volume(self, percent):
        pass

    @abc.abstractmethod
    def get_channel(self):
        pass

    @abc.abstractmethod
    def set_channel(self):
        pass


class Radio(IDevice):

    def __init__(self):
        super().__init__()
        self.volume = 50
        self.channel = "a_channel"
        self.enabled = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def __str__(self):
        return f"Radio: {self.enabled} , {self.volume}, {self.channel}"



class TV(IDevice):

    def __init__(self):
        self.volume = 50
        self.channel = "a_channel"
        self.enabled = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def __str__(self):
        return f"TV: {self.enabled} , {self.volume}, {self.channel}"

class Remote:

    def __init__(self, device: IDevice):
        self.device = device

    def toggle_power(self):
        if self.device.enabled:
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(self.device.get_volume()*1.1)

    def volume_down(self):
        self.device.set_volume(self.device.get_volume()*0.9)

    def change_channel(self, new_channel):
        self.device.set_channel(new_channel)


def main():
    my_remote = Remote(TV())
    print(my_remote.device)
    my_remote.change_channel("Cartoon Network")
    print(my_remote.device)
    my_remote.toggle_power()
    print(my_remote.device)


if __name__ == '__main__':
    main()

