n = [ 0, 1, 0 ]

for i in range( 4 ) :

    t = ""
    for k in n[ 1 : -1 ] :
        t += f"{k} "
    pass

    print( f"{t:^20}" )

    for k in range( len( n ) - 2 ) :
        n.insert( k + 1, n[k] + n[k+1] )
    pass

pass