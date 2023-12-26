from typing import List
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize.api import TokenizerI
import re

class PotawatomiTokenizer(TokenizerI):
    def tokenize(self, text: str) -> List[str]:
        CONJUNCT_PREVERBS = r'(?<!\w)(é|ga|wa)(gi|wi|je|tso|tse|dso)(?!\w)'
        INDEPENDENT_PREVERBS = r'(?<!\w)(n|g|w)(gi|wi|de|da|dagi)(?!\w)'
        text = re.sub(CONJUNCT_PREVERBS, r'\1-\2', text)
        text = re.sub(INDEPENDENT_PREVERBS, r'\1 \2', text)
        text = SpaceTokenizer().tokenize(text)
        # text = self.preverbTagger(text)
        # text = self.personMarkerTagger(text)
        # text = self.emphasizerTagger(text)
        # text = self.demonstrativeTagger(text)
        return text
    
    # def preverbTagger(self, text: List) -> List:
    #     f = open('corpus/index.pv')
    #     pv = f.read()
    #     modified = []
    #     preverbs = [item.split("|") for item in pv.splitlines()]

    #     for i in range(len(text)):
    #         found = False
    #         for pv in preverbs:
    #             if text[i] == pv[0]:
    #                 found = True
    #                 match = pv[1]
    #                 break
    #             else:
    #                 found = False
                    
        
    #         if (found):
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
            
    #     return modified
    
    # def personMarkerTagger(self, text: List) -> List:
    #     # assumes it's already gone through PV tagger
    #     f = open('corpus/index.pn')
    #     pn = f.read()
    #     modified = []
    #     tense = ['gi', 'wi', 'de', 'da']
    #     pronoun = [item.split("|") for item in pn.splitlines()]
        
    #     for i in range(len(text)):
    #         found = False
    #         for pn in pronoun:      
    #             if (text[i] == pn[0]) and (text[i+1][0] in tense):
    #                 found = True
    #                 match = pn[1]
    #                 break
    #             else:
    #                 found = False
                    
    #         if (found):        
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
                
    #     return modified

    # def emphasizerTagger(self, text: List) -> List:
    #     f = open('corpus/index.emph')
    #     e = f.read()
    #     modified = []
    #     tense = ['gi', 'wi', 'de', 'da', 'wa', 'ga']
    #     emph = [item.split("|") for item in e.splitlines()]
        
    #     for i in range(len(text)):
    #         found = False
    #         for e in emph:      
    #             if (text[i] == e[0]):
    #                 if text[i-1][0] not in tense:
    #                     found = True
    #                     match = e[1]
    #                     break
    #             else:
    #                 found = False
                    
    #         if (found):        
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
                
    #     return modified

    # def demonstrativeTagger(self, text: List) -> List:
    #     f = open('corpus/index.dem')
    #     d = f.read()
    #     modified = []
    #     dem = [item.split("|") for item in d.splitlines()]
        
    #     for i in range(len(text)):
    #         found = False
    #         for d in dem:      
    #             if (text[i] == d[0]):
    #                 found = True
    #                 match = d[1]
    #                 break
    #             else:
    #                 found = False
                    
    #         if (found):        
    #             modified.append((text[i], match))
    #         else:
    #             modified.append(text[i])
                
    #     return modified

        