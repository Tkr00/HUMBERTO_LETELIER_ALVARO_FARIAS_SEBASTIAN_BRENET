import cx_Oracle

connection = cx_Oracle.connect('MALT_USER', 'MALT.capstone1', 'malttechnology_high')
print("Conexión exitosa:", connection.version)
connection.close()
