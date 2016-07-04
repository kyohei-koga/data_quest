# coding: UTF-8

f = open("dictionary.txt","r")
vocabulary = f.read()
print(vocabulary)

#Tokenizing the vocabulary
vocabulary = open("dictionary.txt","r").read()  #readはopenのインスタンスである
tokenized_vocabulary = vocabulary.split("\n")
print(tokenized_vocabulary[0:5])

#Replacing special characters
story_string = open("story.txt","r").read()

story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace("''","")
story_string = story_string.replace(";","")
story_string = story_string.replace("\n","")

print("\n")
print(story_string)

#Creating a function to clean tex
story_string = open("story.txt","r").read()
def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    #convert uppercase to lowercase letter
    cleaned_string = cleaned_string.lower()
    return (cleaned_string)
cleaned_story = clean_text(story_string)

#Multiple arguments improve function above
story_string = open("story.txt","r").read()
def clean_text(text_string,special_charactors):
    cleaned_string = text_string
    for string in special_charactors:
        cleaned_string = cleaned_string.replace(string,"")
    cleaned_string = cleaned_string.lower()
    return cleaned_string

clean_chars = [",", ".", "'", ";", "\n"]
cleaned_strory = clean_text(story_string,clean_chars)
print(cleaned_strory)

#Tokenizing the story
def tokenize(text_string,special_charactors):
    cleaned_story = clean_text(text_string, special_charactors) #reuse cleaned_story function
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story[:5])

#Finding misspelled words. see if all tokens found in vocaulary or not.
misspelled_words = []
tokenized_vocabulary = vocabulary.split("\n")
for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(tokenized_vocabulary[0:5])
print(misspelled_words[:5])
