letters = 'abcdefghijklmnopqrstuvwxyz'
max = len(letters) -1
indices = range(max)
initial_h = 7
multiplier = 37

first_position_value = initial_h * multiplier
last_position_value = first_position_value + max

def hash(word: str) -> int:
    h = initial_h

    for letter in word:
        position = letters.index(letter)
        h = h * multiplier + position
    
    return h

def unHash(num: int) -> str:
    result = ''

    if num < first_position_value:
        return result
    
    if num >= first_position_value and num <= last_position_value:
        position = num - first_position_value
        return letters[position]
    
    position = getPosition(num)
    previousH = int((num - position) / multiplier)

    return unHash(previousH) + letters[position]


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