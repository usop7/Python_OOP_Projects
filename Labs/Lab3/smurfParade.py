""" A short description about the module """


class Smurf:
    """This class represents a smurf as a Node with a name value."""

    def __init__(self, name, next_smurf=None):
        self.name = name
        self.next_smurf = next_smurf

    def __str__(self):
        """
        Returns a name.
        :returns: a String
        """
        return f"{self.name}"


class SmurfParade:
    """This  class represents a Linked List of smurfs(Nodes)."""

    def __init__(self, head=None):
        self.head = head

    def append(self, name):
        """
        Creates a new smurf with a given name and appends it to the end
        of the list.
        """
        new_smurf = Smurf(name)
        curr_smurf = self.head
        if curr_smurf is None:
            self.head = new_smurf
        else:
            while curr_smurf.next_smurf is not None:
                curr_smurf = curr_smurf.next_smurf
            curr_smurf.next_smurf = new_smurf

    def __str__(self):
        """
        Returns a list of smurfs' names.
        :returns: a List
        """
        smurf_list = ""
        curr_smurf = self.head
        while curr_smurf is not None:
            smurf_list += curr_smurf.name + " "
            curr_smurf = curr_smurf.next_smurf
        return smurf_list

    def __len__(self):
        """
        Returns the number of Smurfs in the list.
        :return: an int
        """
        count = 0
        curr_smurf = self.head
        while curr_smurf is not None:
            count += 1
            curr_smurf = curr_smurf.next_smurf
        return count

    def __contains__(self, item):
        """
        Returns True if the list has a smurf whose name equals
        to the parameter, item.
        :param item: a String
        :return: boolean
        """
        curr_smurf = self.head
        while curr_smurf is not None:
            if curr_smurf.name == item:
                return True
            curr_smurf = curr_smurf.next_smurf
        return False

    def __iter__(self):
        """
        Overrides iter method so that it can iterate smurfs in the list.
        :returns: iterable object"""
        smurf_list = []
        curr_smurf = self.head
        while curr_smurf is not None:
            smurf_list.append(curr_smurf)
            curr_smurf = curr_smurf.next_smurf
        return iter(smurf_list)

    def __getitem__(self, key):
        """
        Returns a Smurf whose index equals to the parameter, key.
        :param key: an int
        :return: a Smurf
        """
        index = 0
        curr_smurf = self.head
        while curr_smurf is not None:
            if index == key:
                return curr_smurf
            index += 1
            curr_smurf = curr_smurf.next_smurf
        return None

    def count(self, item):
        """
        Returns the number of smurfs whose name is same as the parameter, item.
        :param item: a String
        :return: an int
        """
        count = 0
        curr_smurf = self.head
        while curr_smurf is not None:
            if curr_smurf.name == item:
                count += 1
            curr_smurf = curr_smurf.next_smurf
        return count

    def index(self, item):
        """
        Returns the first index of Smurf in the smurf list whose name equals
        to the parameter item.
        :param item: a String
        :return: an int
        """
        index = 0
        curr_smurf = self.head
        while curr_smurf is not None:
            if curr_smurf.name == item:
                return index
            index += 1
            curr_smurf = curr_smurf.next_smurf
        return None

    def __reversed__(self):
        """
        Creates a reversed linked list and return it.
        :return: a SmurfParade
        """
        reversed_smurfs = []
        curr_smurf = self.head
        while curr_smurf is not None:
            reversed_smurfs.insert(0, curr_smurf)
            curr_smurf = curr_smurf.next_smurf
        return iter(reversed_smurfs)


def main():
    """Creates a SmurfParade object and tests its methods."""

    parade = SmurfParade()
    parade.append("Leeseul")
    parade.append("Christy")
    parade.append("Robert")
    parade.append("Justin")
    parade.append("Leeseul")
    parade.append("Eric")

    print(f"\n1. parade: {parade}")
    print(f"\n2. len(parade): {len(parade)}")
    print(f"\n3. parade[1]: {parade[1]}")
    print(f"\n4. parade[6]: {parade[6]}")
    print(f"\n5. 'Leeseul' in parade: {'Leeseul' in parade}")
    print(f"\n6. 'Rahul' in parade: {'Rahul' in parade}")
    print(f"\n7. parade.index('Robert'): {parade.index('Robert')}")
    print(f"\n8. parade.count('Leeseul'): {parade.count('Leeseul')}")
    print("\n9. Testing Iterator")
    for smurf in parade:
        print(f"\t{smurf}")

    print(f"\n10. reversed(parade): {reversed(parade)}")
    print("\n11. Testing Reversed Iterator")
    for smurf in reversed(parade):
        print(f"\t{smurf}")
    print(f"\n12. parade: {parade}")


if __name__ == '__main__':
    main()
