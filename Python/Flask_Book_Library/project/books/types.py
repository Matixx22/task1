import string


class Name:
    def __init__(self, name):
        if name is None:
            raise Exception('Book name cannot be empty')

        blacklisted_chars = list(string.punctuation)
        blacklisted_chars.remove("'")
        blacklisted_chars.remove("&")
        blacklisted_chars.remove("!")

        for c in blacklisted_chars:
            if c in name:
                raise Exception('Book name cannot contain blacklisted characters')

        self.name = name
