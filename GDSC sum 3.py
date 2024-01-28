def is_palindrome(word):
    return word == word[::-1]

def make_palindrome(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if not is_palindrome(word):
            l=len(word)
            palindrome_word = word + word[l-2::-1]
            result.append(palindrome_word)
        else:
            result.append(word)

    return ' '.join(result)

user_sentence = input("Enter a sentence: ")
result_sentence = make_palindrome(user_sentence)

print("\nConverted Sentence:")
print(result_sentence)
