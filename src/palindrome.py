import re

def palindrome_count(text_input):

    count = 0

    # take the text input change it all to lower case and then put each word in the sentence into a list based on whitespace
    sentence_list = text_input.lower().split()
    # iterate through sentence list and compare each word greater than one letter with its reverse version
    # if its a match, increment the count
    for word in sentence_list:
        # remove all special characters and numbers using regex
        cleaned_word = re.sub('[^A-Za-z]+', '', word)
        if cleaned_word is not '':
            if cleaned_word == cleaned_word[::-1] and len(word) > 1:
                count += 1

    return count