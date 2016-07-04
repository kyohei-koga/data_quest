#codinf UTF-8
story_string = open("story.txt","r").read()
vocabulary = open("dictionary.txt","r").read()
clean_chars = [",", ".", "'", ";", "\n"]

def clean_text(text_string,special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string,"")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

# Optional arguments
def tokenize(text_string, special_characters, clean=False):
    if clean == True:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    else:
        list_text = text_string.split(" ")
        return(list_text)

clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story=tokenize(story_string,clean_chars,True)
#tokenized_vocabulary = tokenize(vocabulary,clean_chars)
tokenized_vocabulary = vocabulary.split("\n")
