class Smurf:
    """This class ."""

    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic


class SmurfParade:
    """This  class ."""

    def __init__(self, village, smurfs):
        self.village = village
        self.smurfs = smurfs

    def __str__(self):
        smurf_list = ""
        for smurf in self.smurfs:
            smurf_list += smurf.name + " "
        return f"{self.village}: {smurf_list}"

    def __len__(self):
        return len(self.smurfs)

    def __contains__(self, smurf_name):
        found = False
        for smurf in self.smurfs:
            if smurf.name == smurf_name:
                found = True
        return found

    def __iter__(self):
        return iter(self.smurfs)


def main():
    parade = SmurfParade("vellage1",
                         [Smurf("leeseul", 10),
                          Smurf("michelle", 20),
                          Smurf("doris", 15)])

    print(parade)


if __name__ == '__main__':
    main()
