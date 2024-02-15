print()
i = 1234
j = 4567.89

print( "\nFstring 예제" )
print( f"i = {i}, j = {j}" )

print( "\n타입 예제" )
print( f"i = {i:d}, j = {j:f}" )

print( "\n그룹 예제" )
print( f"i = {i:,d}, j = {j:,f}" )
print( f"i = {i:_d}, j = {j:_f}" )

print( "\n자리수 퍼센트 예제" )
print( f"i = {i:10d}, j = {j:10.1f}, percent = {i/j:.1%}" )

print( "\n패딩(채움) 예제" )
print( f"i = {i:*>10}, j = {j:*>10.1f}" ) # 좌측 정렬 채움
print( f"i = {i:*^10}, j = {j:*^10.1f}" ) # 중앙 정렬 채움
print( f"i = {i:*<10}, j = {j:*<10.1f}" ) # 우측 정렬 채움

print()