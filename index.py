import argparse
from potnlp.transliterator import Transliterator, LWS_WNALP
from potnlp.tokenizer.potawatomi import PotawatomiTokenizer
from potnlp.normalizer.base import DataNormalizer
from potnlp.stem.base import PotawatomiLemmatizer

def parse_arguments():
    parser = argparse.ArgumentParser(description="Stem Word")
    parser.add_argument("-s", "--sentence", help="Sentence")
    parser.add_argument("-w", "--word", help="Word")
    return parser.parse_args()

def main():
    args = parse_arguments()
    normalizer = DataNormalizer()
    text = normalizer.normalize(text=args.sentence)
    translit = Transliterator(mapping=LWS_WNALP)
    processed = translit.transliterate(text)

    tokenizer = PotawatomiTokenizer()
    lemmatizer = PotawatomiLemmatizer()
    print(lemmatizer.lemmatize(tokenizer.tokenize(processed), args.word))
    
if __name__ == "__main__":
    main()