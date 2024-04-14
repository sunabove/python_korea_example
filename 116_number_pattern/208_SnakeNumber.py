for i in range( 9 ) :

    a = 0
    for k in range( i + 1 ) :
        a = a*10 + 1

    print( f"{f'{a} * {a}':>21} = {a*a}" )

pass