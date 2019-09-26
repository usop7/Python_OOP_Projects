class Smurf:
    """This class ."""

    def __init__(self, name, next_smurf=None):
        self.name = name
        self.next_smurf = next_smurf

    def __str__(self):
        return f"{self.name}"


class SmurfParade:
    """This  class ."""

    def __init__(self, head=None):
        self.head = head

    def add(self, name):
        new_smurf = Smurf(name)
        curr_smurf = self.head
        if curr_smurf is None:
            self.head = new_smurf
        else:
            while curr_smurf.next_smurf is not None:
                curr_smurf = curr_smurf.next_smurf
            curr_smurf.next_smurf = new_smurf

    def __str__(self):
        smurf_list = ""
        curr_smurf = self.head
        while curr_smurf is not None:
            smurf_list += curr_smurf.name + " "
            curr_smurf = curr_smurf.next_smurf
        return smurf_list

    def __len__(self):
        count = 0
        curr_smurf = self.head
        while curr_smurf is not None:
            count += 1
            curr_smurf = curr_smurf.next_smurf
        return count

    def __contains__(self, item):
        curr_smurf = self.head
        while curr_smurf is not None:
            if curr_smurf.name == item:
                return True
            curr_smurf = curr_smurf.next_smurf
        return False

    def __iter__(self):
        smurf_list = []
        curr_smurf = self.head
        while curr_smurf is not None:
            smurf_list.append(curr_smurf)
            curr_smurf = curr_smurf.next_smurf
        return iter(smurf_list)

    def __getitem__(self, key):
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
        Returns the number of smurf whose name is same as an item.
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
        """Returns the first index of Smurf in the smurf list whose name equals to an item."""
        index = 0
        curr_smurf = self.head
        while curr_smurf is not None:
            if curr_smurf.name == item:
                return index
            index += 1
            curr_smurf = curr_smurf.next_smurf
        return None



def main():
    parade = SmurfParade()
    parade.add("leeseul")
    parade.add("christy")
    parade.add("robert")
    parade.add("justin")
    parade.add("eric")

    print(f"\n1. parade: {parade}")
    print(f"\n2. len(parade): {len(parade)}")
    print(f"\n3. parade[0]:\n{parade[0]}")
    print(f"\n4. 'leeseul' in parade: {'leeseul' in parade}")
    print(f"\n5. 'leeseul' not in parade: {'leeseul' not in parade}")
    print("\n------------Iteration Test-----------")
    for smurf in parade:
        print(smurf)
    print("------------End of Iteration-----------")

    #print(f"\nreversed(parade): {reversed(parade)}")



if __name__ == '__main__':
    main()
