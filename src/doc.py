class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __lt__(self, other):
        return len(self.string) < len(other.string)


# test_less_than()
# doc2 < doc1
# doc3 < doc1

# test_greater_than()
# doc1 > doc2
# doc1 > doc3

# doc1 = Doc("Technology")
# doc2 = Doc("Online")
# doc3 = Doc("Nature")
