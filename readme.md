
import peewee, in alumnos_ORM.py

Peewee is a lightweight and expressive Object-Relational Mapping (ORM) library for Python. It provides a simple and Pythonic way to interact with relational databases, such as SQLite, MySQL, PostgreSQL, and others, by abstracting the database operations into Python code.




FILES:

	log.xls: record of logging






The remaining .db and .sql files belong to the old project before using Git



There´s two projects:

1) Without Login

	main.py
   	alumnos_ORM.py
   	ventana.py

Databases:

	schule.db -> SQLite is defined in alumnos_ORM.py

	    class Students(BaseModel): # fields of the DB:  
    		#id = AutoField(unique=True)
    		dni = CharField()
    		class_division = CharField()
    		first_name = CharField()
    		last_name = CharField()
		day_birth = CharField()
		status = CharField()
		sexo = CharField()
    		address = CharField()
    		line_phone = CharField()
    		movile_phone1 = CharField()
    		movile_phone2 = CharField()

 and

2) with Login

	/log/login_3_model_mysql.py --> MySql modell

	main_con_login.py
	alumnos.py
    	ventana_con_login.py


Databases:

	Students.sql -> db_usuarios_old

   		tables:
			students (contains the students' data)




