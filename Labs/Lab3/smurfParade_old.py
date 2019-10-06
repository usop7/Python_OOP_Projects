class Smurf:
    """This class ."""

    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def __str__(self):
        return f"{self.characteristic} {self.name}"


class SmurfParade:
    """This  class ."""

    def __init__(self, village, smurf_list):
        self.village = village
        self.smurf_list = smurf_list

    def __str__(self):
        smurf_list = ""
        for smurf in self.smurf_list:
            smurf_list += smurf.characteristic + " " + smurf.name + " "
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
        return SmurfParade(self.village, list(reversed(self.smurf_list)))


def main():
    parade = SmurfParade("vellage1",
                         [Smurf("leeseul", "smart"),
                          Smurf("michelle", "lovely"),
                          Smurf("doris", "shy")])

    print(f"\n1. parade: {parade}")
    print(f"\n2. len(parade): {len(parade)}")
    print(f"\n3. parade[0]:\n{parade[0]}")
    print(f"\n4. 'leeseul' in parade: {'leeseul' in parade}")
    print(f"\n5. 'leeseul' not in parade: {'leeseul' not in parade}")
    print(f"\nreversed(parade): {reversed(parade)}")


if __name__ == '__main__':
    main()
