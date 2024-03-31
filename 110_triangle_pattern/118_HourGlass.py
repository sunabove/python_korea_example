for i in range( 5, -4, -1 ) :
    if i < 1 : i = -i + 2

    for k in range( 5 - i ) :
        print( " ", end="" )
    pass

    for k in range( i ) :
        print( "* ", end="" )
    pass

    print()
pass