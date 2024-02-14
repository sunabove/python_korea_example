# + string concatenation

print( "+ string concatenration" )

item = "Apple" 
unit_price = 2345.744
count = 1234

print( item + "price : " + str( unit_price ) + " * " + str( count ) + " = " + str(unit_price*count)  )

# % string formatting

print( "% string formatting" )

item = "Apple" 
unit_price = 2345.744
count = 1234

print( "%s price : %.2f * %d = %.1f" % ( item, unit_price, count,  unit_price*count ) )

# format() string formatting

print( "format() string formatting" )

item = "Apple"
unit_price = 2345.744
count = 1234

print( "{0} price : {1:,.2f} * {2:,} = {3:,.1f}".format( item, unit_price, count, unit_price*count ) )

# fstring formatting

print( "fstring formatting" )

item = "Apple" 
unit_price = 2345.744
count = 1234

print( f"{item} price : {unit_price:,.2f} * {count:,} = {unit_price*count:,.1f}" )