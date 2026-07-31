import json
import itertools

from templates import TEMPLATES
from synonyms import SYNONYMS
from response import RESPONSES
from grammar import GrammarGenerator
from typo_generator import TypoGenerator


class DatasetGenerator:

    def __init__(self):

        self.intents = []

        self.grammar = GrammarGenerator()

        self.typo = TypoGenerator()

    # ---------------------------------------
    # Generate patterns
    # ---------------------------------------
    def generate_patterns(self, templates):

        generated_patterns = set()

        for template in templates:

            placeholders = []

            start = template.find("{")

            while start != -1:

                end = template.find("}", start)

                placeholders.append(
                    template[start + 1:end]
                )

                start = template.find("{", end)

            # -----------------------------
            # No placeholders
            # -----------------------------
            if len(placeholders) == 0:

                grammar_sentences = self.grammar.generate(template)

                for sentence in grammar_sentences:

                    generated_patterns.add(sentence)

                    typo_sentences = self.typo.generate(sentence)

                    for typo in typo_sentences:

                        generated_patterns.add(typo)

                continue

            # -----------------------------
            # Placeholder expansion
            # -----------------------------
            synonym_lists = []

            for placeholder in placeholders:

                synonym_lists.append(
                    SYNONYMS.get(
                        placeholder,
                        [placeholder]
                    )
                )

            combinations = itertools.product(
                *synonym_lists
            )

            for combo in combinations:

                sentence = template

                for placeholder, value in zip(
                        placeholders,
                        combo
                ):

                    sentence = sentence.replace(
                        "{" + placeholder + "}",
                        value,
                        1
                    )

                grammar_sentences = self.grammar.generate(
                    sentence
                )

                for g_sentence in grammar_sentences:

                    generated_patterns.add(
                        g_sentence
                    )

                    typo_sentences = self.typo.generate(
                        g_sentence
                    )

                    for typo in typo_sentences:

                        generated_patterns.add(
                            typo
                        )

        return sorted(list(generated_patterns))

    # ---------------------------------------
    # Build Dataset
    # ---------------------------------------
    def build_dataset(self):

        for tag in TEMPLATES:

            patterns = self.generate_patterns(
                TEMPLATES[tag]
            )

            responses = RESPONSES.get(tag, [])

            self.intents.append(

                {

                    "tag": tag,

                    "patterns": patterns,

                    "responses": responses

                }

            )

    # ---------------------------------------
    # Save Dataset
    # ---------------------------------------
    def save(self):

        with open(

            "dataset/intents.json",

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                {

                    "intents": self.intents

                },

                file,

                indent=4,

                ensure_ascii=False

            )

        print("\n====================================")

        print("Dataset Generated Successfully!")

        print("====================================")

        print(f"Total Intents : {len(self.intents)}")

        total_patterns = sum(

            len(intent["patterns"])

            for intent in self.intents

        )

        print(f"Total Patterns : {total_patterns}")

        print("Saved File : intents.json")

        print("====================================\n")


# ---------------------------------------
# Main
# ---------------------------------------

if __name__ == "__main__":

    generator = DatasetGenerator()

    generator.build_dataset()

    generator.save()