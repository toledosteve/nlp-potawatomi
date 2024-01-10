class Utility:
    def __init__(self) -> None:
        pass
    
    def insert_weak_vowels(self, text: str):
        combined_chars = ['zh', 'kw', 'sh', 'ch']
        idx = 0
        index = 0
        output = []
        marker = []
        
        while index < len(text):
            found_combined = False

            # Check if the current and next characters form a combined character
            for combined in combined_chars:
                if text[index:index + len(combined)] == combined:
                    marker.append((combined, 'C'))
                    output.append(combined)
                    index += len(combined)
                    found_combined = True
                    break

            if not found_combined:
                if text[index] not in 'aeioé' and text[index] != ' ':
                    marker.append((text[index], 'C'))
                    output.append(text[index])
                elif text[index] == 'e':
                    marker.append(('e', '{WE}'))
                    output.append('e')
                elif text[index] == 'é':
                    marker.append(('é', '{L}'))
                    output.append('é')
                else:
                    marker.append((text[index], ''))
                    output.append(text[index])
                index += 1
                
            
            prev_char = marker[idx-1] if idx > 0 else ('', '')
            curr_char = marker[0+idx] if idx > 0 else marker[0]

            if (prev_char[1] == 'C' and curr_char[1] == 'C'):
                marker.insert(idx, ('E', '{WO}'))
                output.insert(idx, 'E')
            
            idx += 1
            
        return ''.join(output)