# import (para importar TUDO de uma biblioteca
# frombibliotecaimportalgo - para importar somente uma coisa

# import math
from math import sqrt
num = int(input('Digite um valor'))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}.'.format(num, raiz))

import random
n = random.randint(1,5)
print(n)

import emoji
print(emoji.emojize("Amo vc :red_heart:", variant="emoji_type"))