tel = {'jack': 4098, 'sape': 4139}
print( tel )

tel['guido'] = 4127    # 요소 추가
print( tel )

print( tel['jack'] )    # 요소 획득

del tel['sape']         # 요소 삭제
print( tel )

print( 'guido' in tel )  # 요소 포함 여부