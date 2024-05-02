# partie sans décorateur pour calculer une suite de fibonacci
import timeit

from functools import lru_cache

def fibolent(n):
	if n<2:
		return n
	return fibolent(n-1)+fibolent(n-2)


# avec decorator lru_cache (garde en cache le résultat de la fonction avec les mêmes arguments)
# à n'utiliser que si les mêmes arguments donnent le même résultat

@lru_cache(maxsize=None)
def fiborapide(n):
	if n < 2:
		return n
	return fiborapide(n-1)+fiborapide(n-2)

print(timeit.timeit('[fibolent(10)]', globals=globals()),'s')
print(timeit.timeit('[fiborapide(10)]', globals=globals()),'s')
