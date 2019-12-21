import sqlite3

conn = sqlite3.connect('mess2.db')

c = conn.cursor()

# c.execute("insert into usermess(name) values('sdf')")#select文
c.execute("select name,message from usermess ORDER BY id DESC;")

messtuple = c.fetchall()#list型で挿入

messtuple0 = messtuple[0][0]

names = ["mess1","mess1_2","mess2","mess2_2","mess3","mess3_2","mess4","mess4_2","mess5","mess5_2","mess6","mess6_2","mess7","mess7_2","mess8","mess8_2","mess9","mess9_2","mess10","mess10_2"]


y,g = 0,0

for name in names:
    x = messtuple[y][g]
    xstr = str(x)
    exec('{} = {}'.format(xstr, name))
    g += 1
    if g == 2:
        y += 1
        g = 0

for i in range(10):
    print(names[{}].format(i))

conn.close()