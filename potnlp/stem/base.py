import re
from typing import List

class PotawatomiLemmatizer():
    def __init__(self):
        self._vowels = "aeéio"
        #(?<=\b(wa|ga|é|éwi|égi)\s)(\w+\s)*\w+(yan|yen|t|net|ygo|yak|yék|wat)\b
        
    def _end_in_vowel(self, word: str) -> bool:
        if word:
            return word[-1] in self._vowels
        return False
    
    def _is_conjunct(self, sentence: List, index, max_depth) -> bool:
        if index < 0 or index == max_depth:
            return False
        
        if re.match(r'^(ga|wa|éwi|égi|é|jé|gishpen)$', sentence[index]):
            return True
        
        return self._is_conjunct(sentence=sentence, index=index-1, max_depth=max_depth)
    
    def _is_imperative(self, sentence: List, index, max_depth) -> bool:
        if index < 0 or index == max_depth:
            return False
        
        if re.match(r'^(gégo)$', sentence[index]):
            return True
        
        return self._is_imperative(sentence=sentence, index=index-1, max_depth=max_depth)
    
    def _stem_animate_intransitive(self, sentence: str, target_word: str) -> str:
        pass
        # Step 1 - Determine which mode
        
        # Step 2 - Strip
        # AI Conjunct Verbs
        #v_stem_suffixes = sorted(["an", "en", "t", "net", "go", "ak", "ék", "wat"], key=len, reverse=True)

        # if target_word.endswith('m'):
        #     v_stem_suffixes = [suffix[:-1] + 'k' if suffix == 't' else suffix for suffix in v_stem_suffixes]
        # else:
        #     v_stem_suffixes = [('y' + suffix) if suffix not in ['t', 'wat', 'net'] else suffix for suffix in v_stem_suffixes]
            
        # print(v_stem_suffixes)
        
        # i = 0
        # lastFoundIdx = 0
        # is_verb = False
        # for w in sentence:
        #     for suffix in v_stem_suffixes:
        #         if w.endswith(suffix):
        #             if self._is_conjunct(sentence=sentence, index=i, max_depth=lastFoundIdx):
        #                 lastFoundIdx = i
        #                 is_verb = True
        #                 break;
        #             else:
        #                 break;
        #     i += 1
            
        # if (is_verb):
        #     pattern = rf"{'|'.join(map(re.escape, v_stem_suffixes))}"
        #     return re.sub(pattern=pattern, repl=r'', string=target_word)
        
        # return False
    
    def lemmatize(self, sentence: str, target_word: str):
        word = target_word.lower()
        sentence = sentence.lower().split()
        wlen = len(word)
        
        if wlen <= 2:
            return word

        # foundIdx = [idx for idx, w in enumerate(sentence) if w == word]
        # if foundIdx:
        #     lemma = self._stem_animate_intransitive(sentence=sentence[:int(foundIdx[0])+2], target_word=word)
        #     if lemma:
        #         if self._end_in_vowel(lemma):
        #             return lemma
        #         else:
        #             return lemma+"e"
                    
                    
        

            
            
        