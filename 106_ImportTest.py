# Package Import
from myPkg1 import myMod1

print( myMod1.a )
print( myMod1.b )
print( myMod1.myFun() )

print( "#"*40)

from myPkg1 import myMod2

print( myMod2.a )
print( myMod2.b )
print( myMod2.myFun() )

print( "#"*40)

from myPkg1.myPkg11 import myMod1

print( myMod1.a )
print( myMod1.b )
print( myMod1.myFun() )

print( "#"*40)

from myPkg1.myPkg11 import myMod2

print( myMod2.a )
print( myMod2.b )
print( myMod2.myFun() ) 

