class Smurf:
    """This class ."""

    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def __str__(self):
        return f"Name: {self.name}\nCharacteristic: {self.characteristic}"


class SmurfParade:
    """This  class ."""

    def __init__(self, village, smurf_list):
        self.village = village
        self.smurf_list = smurf_list

    def __str__(self):
        smurf_list = ""
        for smurf in self.smurf_list:
            smurf_list += smurf.name + " "
        return f"{self.village} - {smurf_list}"

    def __len__(self):
        """Returns the number of smurf_list in the smurf list.
        :returns: an int"""
        return len(self.smurf_list)

    def __contains__(self, item):
        """Returns True if a given smurf name belongs to the smurf list.
        :param item: a String
        :returns: a boolean"""
        for smurf in self.smurf_list:
            if smurf.name == item:
                return True
        return False

    def __iter__(self):
        """Overriding this method so that it can iterate its smurf_list list."""
        return iter(self.smurf_list)

    def __getitem__(self, key):
        """
        Returns smurf object whose index equals the key in smurf list.
        :param key: an int
        :return: Smurf
        """
        index = 0
        for smurf in self.smurf_list:
            if index == key:
                return smurf
            index += 1
        return None

    def count(self, item):
        """
        Returns the number of smurf_list whose name is same as an item.
        :param item: a String
        :return: an int
        """
        count = 0
        for smurf in self.smurf_list:
            if smurf.name == item:
                count += 1
        return count

    def index(self, item):
        """Returns the first index of Smurf in the smurf list whose name equals to an item."""
        index = 0
        for smurf in self.smurf_list:
            index += 1
            if smurf.name == item:
                return index
        return None

    def __reversed__(self):
        """Returns a reversed list of smurf list."""
        return reversed(self.smurf_list)


def main():
    parade = SmurfParade("vellage1",
                         [Smurf("leeseul", 10),
                          Smurf("michelle", 20),
                          Smurf("doris", 15)])

    print(f"\nparade: {parade}")

    print(f"\nlen(parade): {len(parade)}")

    print(f"\nparade[0]:\n{parade[0]}")

    print(f"\nreversed(parade): {list(reversed(parade))}")


if __name__ == '__main__':
    main()
