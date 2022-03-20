class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError(
                'Only object of type str can be added to the list.')
        super().append(string)
