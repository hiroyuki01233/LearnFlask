from flask import Flask,render_template,request
from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/startbtn', methods=['GET', 'POST'])
def createname():
    conn = sqlite3.connect('mess2.db')

    c = conn.cursor()
    
    c.execute("select name,message from usermess ORDER BY id DESC;")#select文

    messtuple = c.fetchall()#list型で挿入


    mess0 = str(messtuple[0][0])
    mess0_2 = str(messtuple[0][1])
    mess1 = str(messtuple[1][0])
    mess1_2 = str(messtuple[1][1])
    mess2 = str(messtuple[2][0])
    mess2_2 = str(messtuple[2][1])
    mess3 = str(messtuple[3][0])
    mess3_2 = str(messtuple[3][1])
    mess4 = str(messtuple[4][0])
    mess4_2 = str(messtuple[4][1])
    mess5 = str(messtuple[5][0])
    mess5_2 = str(messtuple[5][1])
    mess6 = str(messtuple[6][0])
    mess6_2 = str(messtuple[6][1])
    mess7 = str(messtuple[7][0])
    mess7_2 = str(messtuple[7][1])
    mess8 = str(messtuple[8][0])
    mess8_2 = str(messtuple[8][1])
    mess9 = str(messtuple[9][0])
    mess9_2 = str(messtuple[9][1])

    message = str(messtuple)#listをstrに変換

    # message = message.replace("0213124124382135794302857439025","'")
    # message = message.replace("0223124124382135794302857439025","(")

    conn.commit()

    conn.close()

    return render_template("index.html",messlist=message,mess0=mess0,mess0_2=mess0_2,mess1=mess1,mess1_2=mess1_2,mess2=mess2,mess2_2=mess2_2,mess3=mess3,mess3_2=mess3_2,mess4=mess4,mess4_2=mess4_2,mess5=mess5,mess5_2=mess5_2,mess6=mess6,mess6_2=mess6_2,mess7=mess7,mess7_2=mess7_2,mess8=mess8,mess8_2=mess8_2,mess9=mess9,mess9_2=mess9_2)


@app.route("/")
def main():
    return render_template("start.html")

@app.route('/btn', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':

        conn = sqlite3.connect('mess2.db')

        c = conn.cursor()

        usertext = request.form["usertext"]
        username = request.form["username"]

        if "'" in usertext or "'" in username:
            return render_template("nokigou.html")
        
        

        usertextlen = len(usertext)
        usernamelen = len(username)

        if usertextlen > 100 or usernamelen > 100:
            return render_template("50moji.html")
        
        if usertextlen == 0 or usernamelen == 0:
            return render_template("50moji.html")

        # usertext = usertext.replace("'","0213124124382135794302857439025")#置換する
        # usertext = usertext.replace("(","0223124124382135794302857439025")

        # Insert a row of data
        c.execute("insert into usermess(name,message) values('%s','%s');"%(username,usertext))#insertする

        c.execute("select name,message from usermess ORDER BY id DESC;")#select文

        messtuple = c.fetchall()#list型で挿入
        
        mess0 = str(messtuple[0][0])
        mess0_2 = str(messtuple[0][1])
        mess1 = str(messtuple[1][0])
        mess1_2 = str(messtuple[1][1])
        mess2 = str(messtuple[2][0])
        mess2_2 = str(messtuple[2][1])
        mess3 = str(messtuple[3][0])
        mess3_2 = str(messtuple[3][1])
        mess4 = str(messtuple[4][0])
        mess4_2 = str(messtuple[4][1])
        mess5 = str(messtuple[5][0])
        mess5_2 = str(messtuple[5][1])
        mess6 = str(messtuple[6][0])
        mess6_2 = str(messtuple[6][1])
        mess7 = str(messtuple[7][0])
        mess7_2 = str(messtuple[7][1])
        mess8 = str(messtuple[8][0])
        mess8_2 = str(messtuple[8][1])
        mess9 = str(messtuple[9][0])
        mess9_2 = str(messtuple[9][1])


        message = str(messtuple)#listをstrに変換

        # message = message.replace("0213124124382135794302857439025","'")
        # message = message.replace("0223124124382135794302857439025","(")

        conn.commit()

        conn.close()

        return render_template("index.html",messlist=message,mess0=mess0,mess0_2=mess0_2,mess1=mess1,mess1_2=mess1_2,mess2=mess2,mess2_2=mess2_2,mess3=mess3,mess3_2=mess3_2,mess4=mess4,mess4_2=mess4_2,mess5=mess5,mess5_2=mess5_2,mess6=mess6,mess6_2=mess6_2,mess7=mess7,mess7_2=mess7_2,mess8=mess8,mess8_2=mess8_2,mess9=mess9,mess9_2=mess9_2)

@app.route('/reloadbtn', methods=['GET', 'POST'])
def reloadbtn():
    conn = sqlite3.connect('mess2.db')

    c = conn.cursor()
    
    c.execute("select name,message from usermess ORDER BY id DESC;")#select文

    messtuple = c.fetchall()#list型で挿入


    mess0 = str(messtuple[0][0])
    mess0_2 = str(messtuple[0][1])
    mess1 = str(messtuple[1][0])
    mess1_2 = str(messtuple[1][1])
    mess2 = str(messtuple[2][0])
    mess2_2 = str(messtuple[2][1])
    mess3 = str(messtuple[3][0])
    mess3_2 = str(messtuple[3][1])
    mess4 = str(messtuple[4][0])
    mess4_2 = str(messtuple[4][1])
    mess5 = str(messtuple[5][0])
    mess5_2 = str(messtuple[5][1])
    mess6 = str(messtuple[6][0])
    mess6_2 = str(messtuple[6][1])
    mess7 = str(messtuple[7][0])
    mess7_2 = str(messtuple[7][1])
    mess8 = str(messtuple[8][0])
    mess8_2 = str(messtuple[8][1])
    mess9 = str(messtuple[9][0])
    mess9_2 = str(messtuple[9][1])

    message = str(messtuple)#listをstrに変換

    # message = message.replace("0213124124382135794302857439025","'")
    # message = message.replace("0223124124382135794302857439025","(")

    #CREATE TABLE usermess(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, message text);
    #insert into usermess(name,message) values('hoge','huga');

    conn.commit()

    conn.close()

    return render_template("index.html",messlist=message,mess0=mess0,mess0_2=mess0_2,mess1=mess1,mess1_2=mess1_2,mess2=mess2,mess2_2=mess2_2,mess3=mess3,mess3_2=mess3_2,mess4=mess4,mess4_2=mess4_2,mess5=mess5,mess5_2=mess5_2,mess6=mess6,mess6_2=mess6_2,mess7=mess7,mess7_2=mess7_2,mess8=mess8,mess8_2=mess8_2,mess9=mess9,mess9_2=mess9_2)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
