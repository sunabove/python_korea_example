# 패키지의 모듈 임포트
from myPkg1 import myMod1

print( myMod1.a )
print( myMod1.b )
print( myMod1.myFun() )

print( "#"*40)

# 패키지 모듈의 구성 요소(변수, 함수) 임포트
from myPkg1.myMod1 import a, b, myFun

print( a )
print( b )
print( myFun() )

print( "#"*40)
 
# 패키지의 모듈을 닉네임으로 임포트
from myPkg1 import myMod2 as nick

print( nick.a )
print( nick.b )
print( nick.myFun() )

print( "#"*40)

# 서브 패키지의 모듈 임포트
from myPkg1.myPkg11 import myMod1

print( myMod1.a )
print( myMod1.b )
print( myMod1.myFun() )

print( "#"*40)

# 서브 패키지 모듈의 모든 구성 요소(변수, 함수, 기타) 임포트
from myPkg1.myPkg11.myMod2 import *

print( a )
print( b )
print( myFun() ) 

print( "#"*40)