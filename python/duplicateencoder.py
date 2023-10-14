def duplicate_encode(word):
    # converts all chars to lower case
    word = word.lower()
    # initialize a new variable with an empty string value
    answer = ''
    # loop through word
    for i in word:
        # condtional if the count of the element i is greater than 1 add ) to the answer
        if word.count(i) > 1:
            answer += ')'
        # else add ( to the answer
        else:
            answer += '('
    return answer