text: str = 'l0ppx! pxp.'

trans: dict = {'l': 'H',
               '0': 'e',
               'p': 'l',
               'x': 'o',
               '!': ','}

table: dict = text.maketrans(trans)

print('Table:', table)
print('Input:', text)
print('Output:', text.translate(table))

text: str = 'abab'

trans: dict = {'a': '1',
               'b': '2'}

table: dict = text.maketrans(trans)

print('Table:', table)
print('Input:', text)
print('Output:', text.translate(table))
