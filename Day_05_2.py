"""
Problem Statement:
    String with a Twist

Link to this Questions
    1. The program will receive 3 English words inputs from STDIN
    2. These three words will be read one at a time, in three separate line
    3. The first word should be changed like all vowels should be replaced by %
    4. The second word should be changed like all consonants should be replaced by #
    5. The third word should be changed like all char should be converted to upper case
    6. Then concatenate the three words and print them
    7. Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h%wa#eYOU.

You can assume that input of each word will not exceed more than 5 chars
"""

sentence = [[i, input()] for i in [1, 2, 3]]
vowels = 'aeiouAEIOU'
result = ''

for word in sentence:
    if word[0] == 1:
        for letter in word[1]:
            if letter in vowels:
                result += '%'
            else:
                result += letter
    elif word[0] == 2:
        for letter in word[1]:
            if letter not in vowels:
                result += '#'
            else:
                result += letter
    elif word[0] == 3:
        result += word[1].upper()

print(result)
