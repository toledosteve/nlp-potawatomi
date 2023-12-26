from potnlp.tag.api import TaggerI
import re

class PotawatomiPOSTagger(TaggerI):
    def __init__(self, window_size=1):
        self.window_size = window_size
        self.rules = [
            (r".*o$", "DEM"),
            (r".*ing$", "VERB"),
            (r".*ly$", "ADV"),
            (r".*able$", "ADJ"),
            (r".*ful$", "ADJ"),
            (r".*ness$", "NOUN"),
            (r".*s$", "NOUN"),
        ]

    def tag(self, sentence):
        tagged_sentence = []

        for i, word in enumerate(sentence):
            tagged_word = self.apply_rules(word, sentence, i)
            tagged_sentence.append(tagged_word)

        return tagged_sentence

    def apply_rules(self, word, words, index):
        for rule, pos_tag in self.rules:
            if re.match(rule, word):
                context = self.get_context(words, index)
                if "da" in context:
                    pos_tag = "PV"  # Override as adverb if "not" is nearby
                return (word, pos_tag)
        return (word, "NOUN")

    def get_context(self, words, index):
        start = max(0, index - self.window_size)
        end = min(len(words), index + self.window_size + 1)
        context = words[start:end]
        return context
