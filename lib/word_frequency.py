import string

def word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_frequency_dict = {}

    for word in words:
        word = word.strip(string.punctuation)
        if word in word_frequency_dict:
            word_frequency_dict[word] += 1
        else:
            word_frequency_dict[word] = 1

    return word_frequency_dict

# Test case
#sentence = "This is a test sentence. This sentence is a test."
#result = word_frequency(sentence)
#print(result)
