from pathlib import *
[
    (lambda h:
        print(
            sum(
                m+1 + (m+1-o)%3 * 3 for o,m in h
            )
        )
    )(y) for y in
        (lambda q:
            [
                q,
                [ ( a, (a+b+2)%3 ) for a,b in q ]
            ]
        )(
            [
                ( 'ABC'.index(a), 'XYZ'.index(b) ) for a,b in [
                    s.split() for s in Path('i').read_text().strip().split('\n')
                ]
            ]
        )
]
