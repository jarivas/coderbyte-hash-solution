letters = 'abcdefghijklmnopqrstuvwxyz'
max = len(letters) -1 # the index of last letters
initial_h = 7 # the initial value that would be used on the hashing
multiplier = 37 # constant value used on the hashing

first_position_value = initial_h * multiplier # is the value of hash('a')
last_position_value = first_position_value + max # is the value of hash('z')

def hash(word: str) -> int:
    h = initial_h

    for letter in word:
        position = letters.index(letter)
        h = h * multiplier + position
    
    return h

# Now we can calculate base case, we have to reverse the hash formula
# h = previousH * multiplier + position
# h - position = previousH * multiplier
# (h - position) / multiplier = previousH
# that leads to unknown values, position and previousH
def unHash(num: int) -> str:
    result = ''

    # if num is less than hash('a') can not be correct
    if num < first_position_value: 
        return result
    
    # in order to be a base case has to be a value between hash('a') and hash('z')
    if num >= first_position_value and num <= last_position_value:
        position = num - first_position_value
        return letters[position]

    position = getPosition(num)

    # since we now the position, we use the reversed version of the formula
    # so we will obtain the previous calculated h
    previousH = int((num - position) / multiplier) 

    # we will concatenate the result of the previous h to the current letter
    return unHash(previousH) + letters[position]

# Since we know the range of values that position can be
# we can iterate over all the indices until a index
# makes the result division betweend (num - index) and multiplier
# equals to 0, so we can say (num - index) is divisble by multiplier
# in other words (num - index) contains multiplier
def getPosition(num: int) -> int:
    result = 0
    i = 0
    tempNum = 0
    isDivisble = False

    while (i <= max):
        tempNum = (num - i)
        isDivisble = (tempNum % multiplier == 0)

        if isDivisble:
            result = i
            i = max + 1
        else:
            i = i + 1

    return result

h = hash('z')
print(unHash(h))

h = hash('aa')
print(unHash(h))

h = hash('hola')
print(unHash(h))

h = hash('acelga')
print(unHash(h))

h = hash('carapapel')
print(unHash(h))