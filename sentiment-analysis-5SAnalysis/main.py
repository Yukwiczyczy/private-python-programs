from preprocessing import TextModification

sample_text = "Hello World. i think this is good. With another punctuation!"

text_modification = TextModification(sample_text)

print(text_modification.word_removal())