letters = 'abcdefghijklmnopqrstuvwxyz'
max = len(letters) -1 # the index of last letters
initial_h = 7 # the initial value that would be used on the hashing
multiplier = 37 # constant value used on the hashing

def hash(word: str) -> int:
    h = initial_h

    for letter in word:
        position = letters.index(letter)
        h = h * multiplier + position
    
    return h

def unHash(num: int) -> str:
    pass

h = hash('z')
print(h)

h = hash('aa')
print(h)

h = hash('hola')
print(h)

h = hash('acelga')
print(h)

h = hash('carapapel')
print(h)