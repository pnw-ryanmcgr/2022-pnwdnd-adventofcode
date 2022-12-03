from pathlib import *
from string import *
(lambda f:
    print(
        sum(
            [
                1 + ascii_letters.index(
                    (
                        set( l[ :len(l)//2 ] ) & set( l[ len(l)//2: ] )
                    ).pop()
                )
                for l in f
            ]
        ),
        sum(
            [
                1 + ascii_letters.index(
                    (
                        set( f[i] ) & set( f[i+1] ) & set( f[i+2] )
                    ).pop()
                )
                for i in range(0, len(f), 3)
            ]
        )
    )
)(Path('i').read_text().strip().split('\n'))
