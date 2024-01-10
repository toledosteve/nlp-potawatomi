import argparse
from potnlp.transliterator import *
from potnlp.tokenizer.potawatomi import PotawatomiTokenizer
from potnlp.normalizer.base import DataNormalizer
# from potnlp.stem.base import PotawatomiLemmatizer
import re

def read_input_file(file_path: str):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            if re.match(r'^[^\n]+ – [^\n]+(\n)?$', line):
                data.append(line.split('–')[0].strip())
            else:
                data.append(line)
                
    return '\n'.join(data)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Stem Word")
    parser.add_argument("-f", "--file", help="File")
    parser.add_argument("-s", "--sentence", help="Sentence")
    parser.add_argument("-w", "--word", help="Word")
    parser.add_argument("-t", "--transliterate", help="Transliterate Mapping Option")
    parser.add_argument("-to", "--tokenize", help="Tokenizer")
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.file:
        text = read_input_file(args.file)
    elif args.sentence:
        text = args.sentence
        
    normalizer = DataNormalizer()
    text = normalizer.normalize(text=text)
    
    if args.transliterate:
        translit = Transliterator(mapping=MAPPINGS[args.transliterate])
        text = translit.transliterate(text)

    if args.tokenize:
        tokenizer = PotawatomiTokenizer()
        text = tokenizer.tokenize(text)
   
    print(text)
    
if __name__ == "__main__":
    main()