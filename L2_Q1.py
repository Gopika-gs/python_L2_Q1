import string
import random
for i in range(10):
    vowels = ['A','E','I','O','U']
    ran=random.shuffle(vowels)
    res = ''.join(vowels)
    print(res)