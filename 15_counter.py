from collections import Counter

c = Counter()

with open("d:/python/final/15_counter.py") as f:
	for line in f:
		c.update(line.split())

print filter(lambda x : c[x] == 1, c)

			
			
		