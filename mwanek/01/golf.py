from pathlib import *;print((lambda s:(s[-1],sum(s)))(sorted([sum(map(int,e.split("\n")))for e in Path('i').read_text().strip().split("\n\n")])[-3:]))
