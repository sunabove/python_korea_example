for r in range( 2 ) :
    for i in range( 5 ) :
        for c in range( 5 - 5*r ):
            print( " ", end="" )

        for c in range( r + 1 ) : 
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
pass