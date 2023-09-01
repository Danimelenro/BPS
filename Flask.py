import pyodbc
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True 


DATABASE_URI = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\dmelende\Documents\env\TallerDB.accdb'

def create_db_connection():
    try:
        conn = pyodbc.connect(DATABASE_URI)
        return conn
    except pyodbc.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

@app.route('/')
def index():
    conn = create_db_connection()
    if conn:
        try:
            cursor1 = conn.cursor()
            cursor1.execute('SELECT * FROM Curso')
            data1 = cursor1.fetchall()

            cursor2 = conn.cursor()
            cursor2.execute('SELECT * FROM Estudiantes')
            data2 = cursor2.fetchall()

            cursor1.close()
            cursor2.close()
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return "Error en la consulta a la base de datos"
        finally:
            conn.close()

        return render_template('reporte.html', data1=data1, data2=data2)
    else:
        return "Error en la conexión a la base de datos"

if __name__ == '__main__':
    app.run(debug=True)

