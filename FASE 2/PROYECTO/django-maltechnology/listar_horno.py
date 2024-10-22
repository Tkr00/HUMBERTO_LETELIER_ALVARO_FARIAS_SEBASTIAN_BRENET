import cx_Oracle
import pandas as pd

# Conexión a la base de datos usando el alias y las credenciales
try:
    connection = cx_Oracle.connect('MALT_USER', 'MALT.capstone1', 'malttechnology_high')
    print("Conexión exitosa:", connection.version)

    cursor = connection.cursor()

    # Consulta para obtener toda la información de la columna USUARIOS_USUARIO
    query = """
    SELECT *
    FROM INFO_HORNO
    """

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener los nombres de las columnas
    columns = [col[0] for col in cursor.description]

    # Obtener todos los registros de la consulta
    data = cursor.fetchall()

    # Crear un DataFrame con los datos obtenidos
    df = pd.DataFrame(data, columns=columns)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel('INFO_HORNO.xlsx', index=False)
    print("Datos guardados en INFO_HORNO.xlsx")

except cx_Oracle.DatabaseError as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
