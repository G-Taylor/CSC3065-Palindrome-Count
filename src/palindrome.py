def palindrome_count(text_input):

    count = 0
    sentence_list = text_input.split()

    for word in sentence_list:
        if word == word[::-1] and len(word) > 1:
            count += 1

    return count