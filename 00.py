letters = 'abcdefghijklmnopqrstuvwxyz'

def hash(word: str) -> int:
    h = 7

    for letter in word:
        position = letters.index(letter)
        h = h * 37 + position
    
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