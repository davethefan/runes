import string
import random


def runegen (size=1, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print (runegen())

''' code to randomly generate a character, using Runes font, this will
display the users divined rune. '''

