for r in range( 2 ) : 
    for i in range( 5 ) :
        for k in range( 10 - i ) :
            print( "_", end="" )
        pass

        for k in range( i + 1 ) :
            print( "* ", end="" )
        pass

        for k in range( 10 - i ) :
            print( "_", end="" )
        pass

        print()
    pass
pass