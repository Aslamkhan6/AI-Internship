import random


class GrammarGenerator:

    def __init__(self, max_variations_per_sentence=15):
        self.max_variations_per_sentence = max_variations_per_sentence

        # General prefixes that fit most sentences
        self.polite_prefix = [
            "",
            "please",
            "kindly",
            "can you please",
            "could you please",
            "i need help to",
            "help me",
            "hey",
        ]

        # Action prefixes (best paired with action verbs)
        self.action_prefix = [
            "i want to",
            "i need to",
            "i would like to",
            "i am trying to",
        ]

        self.suffix = [
            "",
            "please",
            "right now",
            "as soon as possible",
            "today",
            "for me",
            "thanks",
        ]

    def generate(self, sentence):
        """Generates grammatical variations of a given sentence pattern."""
        results = set()
        clean_sentence = sentence.strip().lower()

        # Decide prefix pool based on how the sentence starts
        prefixes = list(self.polite_prefix)

        # Only attach action prefixes if the sentence starts with an action verb
        action_verbs = (
            "check",
            "cancel",
            "track",
            "get",
            "reset",
            "change",
            "update",
            "find",
            "buy",
            "return",
            "claim",
            "speak",
        )
        if clean_sentence.startswith(action_verbs):
            prefixes.extend(self.action_prefix)

        for pre in prefixes:
            for suf in self.suffix:
                text = clean_sentence

                if pre:
                    text = f"{pre} {text}"
                if suf:
                    text = f"{text} {suf}"

                # Clean extra spaces
                normalized_text = " ".join(text.split())
                results.add(normalized_text)

        results_list = sorted(list(results))

        # Downsample if variations exceed limit
        if (
            self.max_variations_per_sentence
            and len(results_list) > self.max_variations_per_sentence
        ):
            random.seed(42)
            results_list = random.sample(
                results_list, self.max_variations_per_sentence
            )

        return results_list


if __name__ == "__main__":
    grammar = GrammarGenerator(max_variations_per_sentence=10)

    # Test Action Verb
    print("--- Action Verb Variations ---")
    for sample in grammar.generate("track my order")[:5]:
        print(f"- {sample}")

    # Test Question
    print("\n--- Question Variations ---")
    for sample in grammar.generate("where is my package")[:5]:
        print(f"- {sample}")