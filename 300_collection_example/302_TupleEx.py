t = ( 12345, 54321, 'hello!' )
print( t )
print( t[0] )

# but they can contain mutable objects:
v = ( [1, 2, 3], [3, 2, 1] )
v[0][1] = 3
print( v )

# Tuples are immutable:
t[0] = 88888

