n = [ 0, 1, 0 ]

for i in range( 10 ) :

    t = ""
    for k in n[ 1 : -1 ] :
        t += f"{k:^3} "
    pass

    print( f"{t:^40}" )

    m = [ ]

    m.append( n[0] )

    for k in range( len(n) - 1 ) :
        m.append( n[k] + n[k+1] )
    pass

    m.append( n[-1] )

    n = m 

pass