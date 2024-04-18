size = 5

n = [ ]

for row in range( size ) :
    n.append( [0]*size )
pass

row = 0
col = 0
direction = 0 

for i in range( 1, size*size + 1 ) :
    n[row][col] = i 

    # 다음 위치 계산
    if direction == 0:  # 오른쪽으로 이동
        if col < size - 1 and n[row][col + 1] == 0:
            col += 1
        else:
            direction = 1
            row += 1
    elif direction == 1:  # 아래로 이동
        if row < size - 1 and n[row + 1][col] == 0:
            row += 1
        else:
            direction = 2
            col -= 1
    elif direction == 2:  # 왼쪽으로 이동
        if col > 0 and n[row][col - 1] == 0:
            col -= 1
        else:
            direction = 3
            row -= 1
    elif direction == 3:  # 위로 이동
        if row > 0 and n[row - 1][col] == 0:
            row -= 1
        else:
            direction = 0
            col += 1
    pass

pass

for m in n :
    for v in m :
        print( f"{v:>3d}", end="" )
    pass

    print()
pass