import mysql.connector

class Alumnos:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost",user="root",passwd="sofocles11",database="School")

    def recupera_alumnnos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM students")
        datos = cur.fetchall()
        cur.close()    
        # print('datos.... en "alumnos.py": \n \n', datos)
        # print(type(datos)) # list !
        # print('.'*100)
        return datos


    def buscar_alumno_x_nombre(self, last_name):
        cur = self.cnn.cursor()
        linea_sql= "SELECT * FROM students WHERE last_name = '{}'".format(last_name)
        cur.execute(linea_sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def busca_alumno_x_dni(self, dni):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM students WHERE dni = '{}'".format(dni))
        datos = cur.fetchall()
        for fila in datos:
            print(fila)
        cur.close()
    
    def inserta_alumno(self, dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2):
        cur = self.cnn.cursor()
        linea_sql = '''INSERT INTO students (dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2) VALUES('{}','{}','{}','{}','{}','{}','{}', '{}', '{}', '{}', '{}')'''.format(dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2)
        cur.execute(linea_sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_alumno(self,register):
        cur = self.cnn.cursor()
        linea_sql = '''DELETE FROM students WHERE register = {}'''.format(register)
        cur.execute(linea_sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_alumno(self, id, dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2):
        cur = self.cnn.cursor()
        print(id)
        print(type(id))
        register = int(id)
        linea_sql='''UPDATE students SET dni='{}', class_division='{}', first_name='{}', last_name='{}', day_birth='{}', status='{}', sexo='{}', address='{}', line_phone='{}', movile_phone1='{}', movile_phone2='{}' WHERE register={}'''.format(dni, class_division, first_name, last_name, day_birth, status, sexo, address, line_phone, movile_phone1, movile_phone2, register)
        cur.execute(linea_sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
