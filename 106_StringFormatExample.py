print()

# + string concatenation
print( "+ string concatenration" )

item = "Apple" 
unit_price = 2345.744
count = 1234

print( item + " price : " + str( unit_price ) + " * " + str( count ) + " = " + str( unit_price*count )  )

# % string formatting
print( "\n% string formatting" )

item = "Apple" 
unit_price = 2345.744
count = 1234

print( "%s price : %.2f * %d = %.1f" % ( item, unit_price, count,  unit_price*count ) )

# format() string formatting
print( "\nformat() string formatting" )

item = "Apple"
unit_price = 2345.744
count = 1234

print( "{0} price : {1:,.2f} * {2:,d} = {3:,.1f}".format( item, unit_price, count, unit_price*count ) )

# fstring formatting
print( "\nfstring formatting" )

item = "Apple" 
unit_price = 2345.744
count = 1234

print( f"{item} price : {unit_price:,.2f} * {count:,d} = {unit_price*count:,.1f}" )

print()