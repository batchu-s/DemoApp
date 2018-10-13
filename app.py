from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import yaml, pymysql

app = Flask(__name__)
Bootstrap(app)

def subscription():
    email = request.form['email']
    db = yaml.load(open('db.yaml'))
    conn = pymysql.Connection(host=db['mysql_host'], user=db['mysql_user'],
    password=db['mysql_password'], db=db['mysql_database'])
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO USERS VALUES(%s)"
            print(cursor.execute(sql, (email)))
        conn.commit()

        with conn.cursor() as cursor:
            sql = "SELECT email FROM USERS"
            cursor.execute(sql)
            for row in cursor:
                if row[0] == email:
                    print('Successfully registered!!')
            
    finally:
        conn.close()


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        subscription()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)