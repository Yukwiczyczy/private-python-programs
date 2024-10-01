from words_removal import string_stop_words, string_oneletter
PUNCTUATIONS = ".,;:?!"

class TextModification():
    
    def __init__(self, text) -> None:
        self.text = text
        
    
    # Converting the text into lower-case text    
    def lower_case(self) -> str:
        original_text: str = self.text
        return original_text.casefold()
    

    # specific punctuation removal for the paragraph that contains at least 2 sentences.
    def punctuation_separation(self) -> list:
        original_text = self.lower_case()
        temp_substring = []
        substring = ""
        
        for char in original_text:
            substring += char
            if char in PUNCTUATIONS and original_text.split():
                temp_substring.append(substring)
                substring = ""
                
        return temp_substring
    
    
    def sentence_split(self) -> list:
        return_splitted_sentences = []
        sentences = self.punctuation_separation()
        
        for sentence in sentences:
             return_splitted_sentences.append(sentence.split())
    
        return return_splitted_sentences
    
    def word_removal(self) -> list:
        sentences = self.sentence_split()
        # print(sentences)
        
        new_sentences = []
        
        for sentence in sentences:
            group_word = []
            for word in sentence:
                if word not in string_oneletter and word not in string_stop_words:
                    group_word += [word]
                    # print(group_word)
                    
            new_sentences.append(group_word)

        return new_sentences
                
                
        def polarity_tagging(self) -> list:
            pass
 
                
        
        
        
        