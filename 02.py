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

def unHash(num: int) -> str:
    result = ''

    # if num is less than hash('a') can not be correct
    if num < first_position_value: 
        return result
    
    # in order to be a base case has to be a value between hash('a') and hash('z')
    if num >= first_position_value and num <= last_position_value:
        position = num - first_position_value
        return letters[position]

# Testing the base case works iterating over all possible solutions
for position in range(max):
    letter = letters[position]
    h = hash(letter)
    print(letter, '=', unHash(h))
