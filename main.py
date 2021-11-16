from flask import Flask, render_template
import mysql.connector as my
class database():
    def __init__(self):
        self.__host = "bmm9nmdc8jkviblsmk1v-mysql.services.clever-cloud.com"
        self._database="bmm9nmdc8jkviblsmk1v"
        self._user="ul8a9buow3kovfwl"
        self._password="T5fBv04lvFp9hBV9W70b"
    def db_retrieve(self):
        conn = my.connect(host = self.__host, database = self._database, user = self._user, password = self._password)
        cursor = conn.cursor()
        stmt = 'select project, link from ckpyprojects'
        cursor.execute(stmt)
        res = cursor.fetchall()
        pro_det = {}
        for row in res:
            pro_det[row[0]] = row[1]
        cursor.close()
        conn.close()
        return pro_det
app = Flask(__name__)
@app.route('/')
def index():
    mydb = database()
    data = mydb.db_retrieve()
    return render_template('index.html', data = data)
if __name__ == '__main__':
    app.run(debug=True)