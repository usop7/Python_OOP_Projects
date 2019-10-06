class UpperCaseIterator:
    def __init__(self, string):
        list_of_words = string.split()
        self.words = [word.upper() for word in list_of_words]
        self.index = 0

    def __next__(self):
        """
        Responsible for returning the next element in the container,
        otherwise if its at the end, it raises a StopIterator error.
        :return: word, string
        """
        if self.index == len(self.words):
            raise StopIteration()
        my_word = self.words[self.index]
        self.index += 1
        return my_word

    def __iter__(self):
        return self


class UpperCaseIterable:

    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return UpperCaseIterator(self.string)


def main():
    sentence = UpperCaseIterable("This is a sentence.")

    finished_iteration = False
    sentence_iterator = iter(sentence)
    while not finished_iteration:
        try:
            print(next(sentence_iterator))
        except StopIteration:
            finished_iteration = True

    """Smae Thing."""
    for word in sentence:
        print(word)


if __name__ == "__main__":
    main()

