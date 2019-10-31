"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""
import string


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = {}

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # convert a text file into a dictionary {word: word_count}
        word_counter = {}
        punctuation_str = ''.join(self.COMMON_PUNCTUATION)
        translator = str.maketrans('', '', punctuation_str)
        with open(src, mode='r', encoding='utf-8-sig') as book_file:
            for line in book_file:
                for word in line.split():
                    word = word.translate(translator).lower()
                    word_counter[word] = word_counter.get(word, 0) + 1
        self.text = word_counter

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        unique_words = [word for (word, count) in self.text.items() if count == 1]
        return unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-"*50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-"*50)
    for word in unique_words:
        print(word)
    print("-"*50)


if __name__ == '__main__':
    main()