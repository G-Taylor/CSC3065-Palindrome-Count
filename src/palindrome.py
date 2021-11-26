def palindrome_count(text_input):

    count = 0
    sentence_list = text_input.split()
    
    # iterate through sentence list and compare each word greater than one letter with its reverse version
    # if its a match, increment the count
    for word in sentence_list:
        if word == word[::-1] and len(word) > 1:
            count += 1

    return count