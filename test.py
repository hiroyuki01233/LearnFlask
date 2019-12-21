import random
import sqlite3

conn = sqlite3.connect('mess2.db')

c = conn.cursor()

c.execute("select * from user")#select文

messtuple = c.fetchall()#list型で挿入

print(type(messtuple))

conn.close()



# c = conn.cursor()

# # Create table
# c.execute('''CREATE TABLE messages
#              (username text, message text)''')
# name = "hiroyukiii"
# mess = "test222"
# # Insert a row of data
# c.execute("INSERT INTO messages VALUES ("hrou","fsafd")")

# c.execute("select * from messages")
# list1 = c.fetchall()

# # Save (commit) the changes
# conn.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been commit
# # ted or they will be lost.
# conn.close()

# list1 = ["list1","list2","list3","list4'"]

# new_list = str(list1)

# new_list = new_list.replace("'","43089573908709385703458")

# print(new_list)

# newnew_list = new_list.replace("43089573908709385703458","'")

# print(newnew_list)