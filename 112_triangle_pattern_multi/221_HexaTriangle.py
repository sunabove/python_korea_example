for r in range( 3 ) :
    for i in range( 5 ) :
        print( " "*(10 -5*r), end="" )

        for c in range( r + 1 ) : 
            print( " "*(4 -i), end="" )
            print( "* "*(i + 1), end="" )
            print( " "*(4 -i), end="" )
        pass
    
        print()
    pass
pass