for i in range( 7, -3, -1 ) :

    a = 0
    for k in range( 9, i + 1, -1 ) :
        a = a*10 + k

    print( f"{a:>10} * 9 {'+' if i > -1 else '-'} {abs(i)} = {a*9 + i}" )

pass