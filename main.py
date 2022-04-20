def Soji(y, x):
    if map3[y][x] != 0:
        minimize = 1000
        if y < h-1 and map3[y+1][x] < minimize :
            minimize = map3[y+1][x]
        if y > 0 and map3[y-1][x] < minimize :
            minimize = map3[y-1][x]
        if x < w-1 and map3[y][x+1] < minimize :
            minimize = map3[y][x+1]
        if x > 0 and map3[y][x-1] < minimize :
            minimize = map3[y][x-1]
        map3[y][x] = minimize + 1  
    if y < h-1:
        if map3[y+1][x] > map3[y][x] + 1 and map3[y+1][x] != 1001 :
            Soji(y+1, x)
    if y > 0:
        if map3[y-1][x] > map3[y][x] + 1 and map3[y-1][x] != 1001 :
            Soji(y-1, x)
    if x < w-1:
        if map3[y][x+1] > map3[y][x] + 1 and map3[y][x+1] != 1001 :
            Soji(y, x+1)
    if x > 0:
        if map3[y][x-1] > map3[y][x] + 1 and map3[y][x-1] != 1001 :
            Soji(y, x-1)

def print_step(y, x):
    map4[y][x] = 5
    print("(" , x , "," , y , ")", end=' ')
    minimize = 1000
    min_id = 0
    if map3[y][x] != 0:
        if y > 0 and map3[y-1][x] < minimize :
            minimize = map3[y-1][x]
            min_id = 1
        if y < h-1 and map3[y+1][x] < minimize :
            minimize = map3[y+1][x]
            min_id = 2
        if x < w-1 and map3[y][x+1] < minimize :
            minimize = map3[y][x+1]
            min_id = 3
        if x > 0 and map3[y][x-1] < minimize :
            minimize = map3[y][x-1]
            min_id = 4
    
    if min_id == 1:
        print("上")
        print_step(y-1, x)
    if min_id == 2:
        print("下")
        print_step(y+1, x)
    if min_id == 3:
        print("右")
        print_step(y, x+1)
    if min_id == 4:
        print("左")
        print_step(y, x-1)

a1, b1, c1, d1= input("Please input start point and end point: ").split()
a = int(a1)
b = int(b1)
c = int(c1)
d = int(d1)
f = open('test1.txt', 'r')

input_txt = f.read()
w = int(input_txt.split("\n")[0].split( )[0])
h = int(input_txt.split("\n")[0].split( )[1])#get w, h

map1 = []
for i in range(h):
    map1.append(input_txt.split("\n")[i+1])#map1 done
    
change_char = list(map1[d])
change_char[c] = 'G'
map1[d] = ''.join(change_char)#G done

map2 = []
map4 = []
list_tmp = []
list_tmp2 = []
for i in range(h):
    for j in range(w):
        list_tmp.append(map1[i][j])
    list_tmp2 = list_tmp.copy()
    map2.append(list_tmp2)
    list_tmp.clear()#map2 done
    
for i in range(h):
    for j in range(w):
        list_tmp.append(map1[i][j])
    list_tmp2 = list_tmp.copy()
    map4.append(list_tmp2)
    list_tmp.clear()#map4 done
    
map3 = map2.copy()
for i in range(h):
    for j in range(w):
        if map2[i][j] == '1':
            map3[i][j] = 1001
        if map2[i][j] == '0':
            map3[i][j] = 1000
map3[d][c] = 0#the prepare of map3 done

Soji(d, c)

print("起點到終點最少步數 : " , map3[b][a])
print_step(b, a)

change_char = list(map1[b])
change_char[a] = 'X'
map1[b] = ''.join(change_char)#X done
print("")
for i in range(h):
    for j in range(w):
        if map1[i][j] == 'G' :
            print("\033[1;30;43mG\033[0m ",end='')
        elif map1[i][j] == 'X' :
            print("\033[1;30;43mX\033[0m ",end='')
        elif map4[i][j] == 5 :
            print("\033[1;30;43m0\033[0m ",end='')
        else: 
            print(map1[i][j], end=' ')
    print("")

f.close()
