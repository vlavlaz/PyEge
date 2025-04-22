#Взгляд навскидку

#123456789|123456789|123456789|12345_____      #35, 22, 12, 5, 1
#123456789|123456789|12____12345678/12345\ 1     #Всего N+1 строчек мы выведем
#123456789|12___123456/1234\123456/1234567\ 2
#12345__1234/123\1234/123456\1234/123456789\ 3
#1_12/12\12/12345\12/12345678\12/123456789|1\ 4
#/1\/1234\/1234567\/123456789|\/123456789|123\ 5
#---------------------------------------------->

def make_body(hills, distance, width):
    body = ""
    for index in range (hills):
        body += " "*distance+"/"+" "*(width+3*index)+"\\"
    return body

#N - кол-во гор
N = int(input())

tops = [0] * N
outs = [0] * (N+1)
ins = [0] * (N+1)

tops_str = [""] * (N+1)
bodies = [""] * (N+1)

t = 1

for i in range (N):
    tops[i] = t
    t = t + 4+(3*i)

    outs[i+1] = 2*i
    ins[i+1] = 1+i

#Сортируем все полученные размеры в обратном порядке, чтобы в конце была самая высокая гора!
tops = sorted(tops, reverse=True)
outs = sorted(outs, reverse=True)
ins = sorted(ins, reverse=True)

for i in range(N+1):
    if i<N: tops_str[i] = " " * tops[i] + "_" * (N - i)
    bodies[i] = make_body(i, outs[i-1], ins[i-1])

    print(tops_str[i]+bodies[i])