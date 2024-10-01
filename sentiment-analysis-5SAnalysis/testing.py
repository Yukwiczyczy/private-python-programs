sample_text = "Hello World. I think this is good. what a nice day!"
PUNCTUATIONS = [".", ",", ";", ":", "?", "!"]

container = []
for punctuation in PUNCTUATIONS:
    if punctuation in sample_text:
        container += sample_text.split(punctuation)
        
print(container)