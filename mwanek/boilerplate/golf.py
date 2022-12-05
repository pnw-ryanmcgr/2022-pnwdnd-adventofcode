(lambda f: #f is the text in the file, split by lines
    (lambda p: #p is the parsed data
        print(
            [part1 for part1 in p], #Solve part 1
            [part2 for part2 in p]  #Solve part 2
        )
    )(
        [p for p in f] # Parse and return list
    )
)(open('i').read().strip().split('\n'))
