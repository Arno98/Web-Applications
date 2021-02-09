import psycopg2
import psycopg2.extras

def get_db(sql, params=None):
	psycopg2_connection = psycopg2.connect(database='postgres', user='postgres', password='abc123', host='postgres', port='5432')
	db = psycopg2_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
	if params == None:
		command = db.execute(sql)
	else:
		command = db.execute(sql, params)
	db_command = sql.split()
	if db_command[0] == 'SELECT':
		try:
			records = db.fetchall()
			return_list = []
			for row in records:
				return_list.append(dict(row))
		except AttributeError:
			return None
		else:
			return return_list
			psycopg2_connection.commit()
	if db_command[0] == 'INSERT' or db_command[0] == 'UPDATE' or db_command[0] == 'DELETE' or db_command[0] == 'CREATE':
		psycopg2_connection.commit()
		psycopg2_connection.close()
