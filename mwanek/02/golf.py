from pathlib import *;print([(lambda h:sum(m+1+(m+1-o)%3*3 for o,m in h))(y)for y in(lambda q: (q,[(a,(a+2+b)%3)for a,b in q]))([('ABC'.index(a),'XYZ'.index(b))for a,b in[s.split()for s in Path('i').read_text().strip().split('\n')]])])
