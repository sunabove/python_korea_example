for i in range( 1, 10 ) :

    if i > 5 :
        i = 10 - i
    pass
    
    for k in range( 5 - i ) :
        print( " ", end="" )
    pass

    for k in range( i ) :
        print( "* ", end="" )
    pass

    print()
pass