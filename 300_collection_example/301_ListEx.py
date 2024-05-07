fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print( fruits )
print( fruits.count('apple') )  # 'applet' 요소들의 갯수 
print( fruits.index('banana') ) # 'applet' 요소의 첫 번째 인덱스 
fruits.reverse()                # 리스트 데이터 역전
print( fruits )
fruits.append('grape')          # 'grape' 요소 추가
print( fruits )
fruits.sort()                   # 리스트 정렬
print( fruits )
print( fruits.pop() )           # 리스트 마지막 데이터 제거
print( fruits )