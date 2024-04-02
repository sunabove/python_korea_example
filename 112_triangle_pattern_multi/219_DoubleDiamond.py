for i in range( 9 ) :

    if i > 4 :
        i = 8 - i
    pass

    for m in range(2) :
        print( " "*(4 -i), end="" )
        print( "* "*(i + 1), end="" )
        print( " "*(4 -i), end="" )
    pass

    print()
pass