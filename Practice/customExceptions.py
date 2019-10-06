class InvalidCharacterError(Exception):
    def __init__(self, invalid_chars):
        super().__init__(f"Error! Cannot have {invalid_chars} in "
                         f"character name")
        self.invalid_chars = invalid_chars


class Character():

    invalid_chars = ['!', '@', '_']
    def __init__(self, name):
        for i in Character.invalid_chars:
            if i in name:
                raise InvalidCharacterError(i)


def main():
    try:
        name = '!leeseul'
        c1 = Character(name)
    except InvalidCharacterError as e:
        print(e)
        if e.invalid_chars == '!':
            name.replace(e.invalid_chars, 'l')


if __name__ == "__main__":
    main()