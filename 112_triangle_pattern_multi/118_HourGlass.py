for i in range( 10 ) :
    if i < 5 : 
        i = 5 - i
    else :
        i = i - 4

    for k in range( 5 - i ) :
        print( " ", end="" )
    pass

    for k in range( i ) :
        print( "* ", end="" )
    pass

    print()
pass