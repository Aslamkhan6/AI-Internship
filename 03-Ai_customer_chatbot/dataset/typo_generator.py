import random


class TypoGenerator:

    def __init__(self):

        pass

    def generate(self, sentence):

        patterns = set()

        patterns.add(sentence)

        words = sentence.split()

        # Remove one character
        for word in words:

            if len(word) > 3:

                index = random.randint(1, len(word) - 2)

                typo = word[:index] + word[index + 1:]

                patterns.add(
                    sentence.replace(word, typo, 1)
                )

        # Double one character
        for word in words:

            if len(word) > 2:

                index = random.randint(0, len(word) - 1)

                typo = (
                    word[:index]
                    + word[index]
                    + word[index:]
                )

                patterns.add(
                    sentence.replace(word, typo, 1)
                )

        # Replace common words
        replace = {

            "hello": "helo",
            "hi": "hii",
            "hey": "hy",
            "please": "plz",
            "thanks": "thx",
            "thank": "thnk",
            "good": "gud",
            "you": "u",
            "are": "r"

        }

        for word in words:

            if word.lower() in replace:

                patterns.add(
                    sentence.replace(
                        word,
                        replace[word.lower()],
                        1
                    )
                )

        return list(patterns)