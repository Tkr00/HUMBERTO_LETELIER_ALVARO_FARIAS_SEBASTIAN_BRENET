import cx_Oracle

# Conexión usando el mismo alias que en test_bbdd.py
try:
    connection = cx_Oracle.connect('MALT_USER', 'MALT.capstone1', 'malttechnology_high')
    print("Conexión exitosa:", connection.version)

    cursor = connection.cursor()

    # Consulta para listar columnas de todas las tablas visibles para el usuario
    query = """
    SELECT table_name, column_name, data_type, data_length
    FROM all_tab_columns
    WHERE owner = :owner
    ORDER BY table_name, column_id
    """

    # Ejecutar la consulta (ajusta 'MALT_USER' si necesitas otro esquema)
    cursor.execute(query, owner='MALT_USER')

    # Formato de salida
    print(f"{'Tabla':<30} {'Columna':<30} {'Tipo':<20} {'Longitud'}")
    print("-" * 90)

    for table_name, column_name, data_type, data_length in cursor:
        print(f"{table_name:<30} {column_name:<30} {data_type:<20} {data_length}")

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()