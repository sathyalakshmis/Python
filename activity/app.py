from flask import Flask
import mysql.connector  

app = Flask(__name__)

@app.route('/')
def retrieve_data():
    try:
        conn = mysql.connector.connect(
            host  = "localhost",
            user = "root",
            password = "SATHYAs123$>>",
            database = "c361cohort"
        )

        cursor = conn.cursor()
        cursor.execute("select * from patients")

        rows = cursor.fetchall()

        data = ''

        for row in rows:
            id,firstname,lastname,age,phnno = row
            data += f"id: {id}, firstname: {firstname}, lastname: {lastname}, age: {age}, phnno: {phnno}<br>"
        

        conn.commit()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        return "Error in mysql connection"


if __name__ == '__main__':
    app.run()