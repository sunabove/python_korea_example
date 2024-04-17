size = 5

n = [ ]

for r in range( size + 2 ) :
    v = 0 if 0 < r < size + 1 else -1 

    m = [ ]
    m.append( -1 )
    m.extend( [v]*size )
    m.append( -1 )

    n.append( m )
pass

r = 1
c = 1
dir = 0 

for i in range( 1, size*size + 1 ) :
    n[r][c] = i 

    if n[r][c+1] == 0 :
        dir = 0
        c += 1
    elif n[r+1][c] == 0 :
        dir = 1
        r += 1
    elif n[r-1][c] == 0 :
        dir = 3
        r -= 1
    elif n[r][c -1] == 0 :
        dir = 4
        c -= 1
    pass

pass

for m in n[ 1 : -1 ] :
    for v in m[ 1 : -1 ] :
        print( f"{v:>3d}", end="" )
    pass
    print()
pass