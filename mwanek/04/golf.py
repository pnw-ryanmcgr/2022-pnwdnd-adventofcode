(lambda f:(lambda l:print(len([x for x in l if x[0].issubset(x[1])or x[1].issubset(x[0])]),len([x for x in l if x[0]&x[1]])))([[set(range(*(lambda a,b:(int(a),int(b)+1))(*c.split('-'))))for c in d.split(',')]for d in f]))(open('i').read().strip().split('\n'))
