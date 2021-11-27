import re

def palindrome_count(text_input):

    count = 0
    # take the text input, remove all special characters and numbers using regex, then change it all to lower case
    # and then put each word in the sentence into a list based on whitespace
    sentence_list = re.sub('[^A-Za-z]+', ' ', text_input.lower()).split()
    # iterate through sentence list and compare each word greater than one letter with its reverse version
    # if its a match, increment the count
    for word in sentence_list:
        if word == word[::-1] and len(word) > 1:
            count += 1

    return count
