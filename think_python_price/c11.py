

# fruit='banana'
# index=0
# while index>-len(fruit):
#     letter=fruit[index-1]
#     print(letter)
#     index=index-1

# prefixes='JKLMNOPQ'
# suffix='ack'
# letter=prefixes[index]

# for letter in prefixes:
#     print(letter+suffix)


# def find(word,letter):
#     index=0
#     while o<len(word):
#         if word[o]==letter:
#             return index
#         index=index+1

#     return -1

# find(o)


# word='banana'
# count=0
# for letter in word:
#     if letter=='a':
#         count =count +1

# print(count)

#import math

# def is_palindrome(s):
#     s=str(s)
#     return s==s[::-1]


# print(is_palindrome("abdcd"))
# # print(is_palindrome("akdjfksdjfaksdjfkasdjf"))
# #print(is_palindrome('abcd'))

#很奇怪，没有办法倒序被打印出来
# def is_palindrome(string):
#     string = str(string)    
#     return string == string[::-1]

# print(is_palindrome('worw'))
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
# #             return 'True'
# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#         return flag

# print(any_lowercase4('bANANA'))
# def rotate_word(s, shift):
#     result = ""
#     for char in s:
#         result += chr((((ord(char) + (shift % 26)) % 123) % 97) + 97)
#     return result

# print (rotate_word("cheer", 7))
# print (rotate_word("melon", -10))
def rotate_word (word, num_shift):
    new_letter = ""
    new_word = ""
    word_lower = word.lower()
    
    for letter in word_lower:
        #rotate letter
        new_ltr_position = ord(letter)+num_shift
        
        # rotate z-->a or z<--a
        if new_ltr_position < ord('a'): #rotate z<--a
            new_ltr_position = new_ltr_position + 26
        elif new_ltr_position > ord('z'): #rotate z-->a
            new_ltr_position = new_ltr_position - 26
        
        #build new word
        new_letter = chr(new_ltr_position)
        new_word = new_word + new_letter

    return new_word
    
print (rotate_word("melon",-10))
print (rotate_word("cheer",7))