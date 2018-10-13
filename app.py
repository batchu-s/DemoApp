from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import yaml, pymysql

app = Flask(__name__)
Bootstrap(app)
def dummy_function():
    return 'Dummy'

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']
        db = yaml.load(open('db.yaml'))
        conn = pymysql.Connection(host=db['mysql_host'], user=db['mysql_user'],
        password=db['mysql_password'], db=db['mysql_database'])
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO LOGIN VALUES(%s,%s)"
                cursor.execute(sql, (uname, password))
            conn.commit()

        finally:
            conn.close()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)