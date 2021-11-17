# word_counter
# Gets word occurrence count and sort count in descending order
class word_counter:
    def __init__(self, tokens):
        self.tokens = tokens

    # Counts occurrences of each word from collection of text tokens
    # Returns Dictionary{str word, int count}
    def getCount(self):
        count = {}
        for token in self.tokens:
            if token in count:
                count[token] = count.get(token) + 1
            else:
                count[token] = 1
        return count

    # Sorts the provided dictionary by decreasing value
    # Returns a list of keys (str) corresponding to sorted value
    def sortCount(self, count):
        return sorted(count, key=count.get, reverse=True)
