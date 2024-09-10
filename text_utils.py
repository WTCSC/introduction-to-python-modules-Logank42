def count_chars(text):
    return len(text)

def count_words(text):
    return len(text.split())

def count_sentences(text):

    x=0

    for character in text:
        if character in '.?!':
            x += 1
    return(x)

