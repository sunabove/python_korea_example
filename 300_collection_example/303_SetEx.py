basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print( basket )               # 중복이 제거된 데이터들만 출력됨
print( 'orange' in basket )   # 요소 포함 여부 

a = set('abracadabra')
b = set('alacazam')

print( a )
print( b )
print( a - b )     # 차집한
print( a | b )     # 합집합
print( a & b )     # 교집합
print( a ^ b )     # 여집합