for i in range( 9 ) :

    for m in range(2) :
        if i > 4 :
            i = 8 - i
        pass
        
        for k in range( 4 - i ) :
            print( " ", end="" )
        pass

        for k in range( i + 1 ) :
            print( "* ", end="" )
        pass

        for k in range( 4 - i ) :
            print( " ", end="" )
        pass
    pass

    print()
pass