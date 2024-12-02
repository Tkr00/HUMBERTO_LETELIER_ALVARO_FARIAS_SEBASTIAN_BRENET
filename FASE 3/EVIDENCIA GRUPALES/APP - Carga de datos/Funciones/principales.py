import pandas as pd
import oracledb
from datetime import datetime 
from Funciones.secundarias import fecha_actual, configuracion, configuracion2
import time
from tkinter import messagebox
import csv




# FUNCIÓN PARA VACIAR ARCHIVO
def eliminar_lineas(contador):
    ### OBTENER Y FORMATEAR HORA ACUTAL
    fecha_hora = fecha_actual()
    parametros = configuracion()
    try:
        with open(parametros["path"], 'r') as archivo:
            lineas = archivo.readlines()

        lineas = [lineas[0]] + lineas[contador :-1]

        with open(parametros["path"], 'w') as archivo:
            archivo.writelines(lineas)

        print(f"{fecha_hora}: Se han eliminado {contador} registros")
    except Exception as ex:
        print(f"{fecha_hora}: Error al eliminar líneas del archivo: {ex}")




# FUNCIÓN PARA CONECTAR CON BDD
def conectar_bdd():
    parametros = configuracion()
    
    user = parametros["user"]
    password = parametros["password"]  
    dsn = "malttechnology_high"
    wallet_password = "MALT@malt12345678"  # Contraseña del wallet
    
    # Ruta al wallet
    config_dir = r"C:\\Users\Alvaro\Documents\Wallet_MaltTechnology"
    wallet_location = r"C:\\Users\Alvaro\Documents\Wallet_MaltTechnology"
    vi_contador = 0
    v_conectado = "n"
    while vi_contador < 3:
        try:
            global cnn
            cnn = oracledb.connect(
                user=user,
                password=password,
                dsn=dsn,
                config_dir=config_dir,
                wallet_location=wallet_location,
                wallet_password=wallet_password
            )
            vi_contador = 10
            v_conectado = "s"
        except:
            vi_contador += 1
            v_conectado = "n"
    return v_conectado




# FUNCIÓN PRINCIPAL
def main(timer_runs, ruta_archivo):
    parametros = configuracion()
    fecha_hora = fecha_actual()
    print(f"{fecha_hora}: Ingresando datos..." )
    # INGRESAR DATOS
    while timer_runs.is_set():
        tiempo = parametros["tiempo"]
        v_conectado = conectar_bdd()
        if v_conectado == "s":
            ingresar_datos(ruta_archivo)

        time.sleep(int(tiempo))  # Segundos




#FUNCIÓN PARA INGRESAR DATOS
def ingresar_datos(ruta_archivo):
    fecha_hora = fecha_actual()

    try: 
        df = pd.read_csv(ruta_archivo, sep=";", parse_dates=["dd-MM-yyyy H:mm:ss"], dayfirst=True, encoding='unicode_escape').fillna('0')
    except Exception as ex:
        messagebox.showerror(message="Archivo erroneo o no vinculado, intente otra vez", title='ERROR')
        return
    
    try:
        # Valores Float
        df['T Sobre Grano'] = df['T Sobre Grano'].astype(str).str.replace(',', '.').astype(float)
        df['T Sobre Tela'] = df['T Sobre Tela'].astype(str).str.replace(',', '.').astype(float)
        df['T Bajo Tela'] = df['T Bajo Tela'].astype(str).str.replace(',', '.').astype(float)
        df['T AMBIENTE'] = df['T AMBIENTE'].astype(str).str.replace(',', '.').astype(float)
        df['%HR Sobre tela'] = df['%HR Sobre tela'].astype(str).str.replace(',', '.').astype(float)
        # Valores Int
        df['Presion diferencial'] = df['Presion diferencial'].astype(str).str.replace(',', '.').astype(float) / 1
        df['GAS ETAPA 1'] = df['GAS ETAPA 1'].astype(str).str.replace(',', '.').astype(float) / 1
        df['GAS ETAPA 2'] = df['GAS ETAPA 2'].astype(str).str.replace(',', '.').astype(float) / 1
        df['GAS ETAPA 3'] = df['GAS ETAPA 3'].astype(str).str.replace(',', '.').astype(float) / 1
        df['GAS ETAPA 4'] = df['GAS ETAPA 4'].astype(str).str.replace(',', '.').astype(float) / 1
        df['GAS ETAPA 5'] = df['GAS ETAPA 5'].astype(str).str.replace(',', '.').astype(float) / 1
        df['GAS ETAPA 6'] = df['GAS ETAPA 6'].astype(str).str.replace(',', '.').astype(float) / 1
        df['TIEMPO BARRA ETAPA 1'] = df['TIEMPO BARRA ETAPA 1'].astype(str).str.replace(',', '.').astype(float) / 1
        df['TIEMPO BARRA ETAPA 2'] = df['TIEMPO BARRA ETAPA 2'].astype(str).str.replace(',', '.').astype(float) / 1
        df['TIEMPO BARRA ETAPA 3'] = df['TIEMPO BARRA ETAPA 3'].astype(str).str.replace(',', '.').astype(float) / 1
        df['TIEMPO BARRA ETAPA 4'] = df['TIEMPO BARRA ETAPA 4'].astype(str).str.replace(',', '.').astype(float) / 1
        df['TIEMPO BARRA ETAPA 5'] = df['TIEMPO BARRA ETAPA 5'].astype(str).str.replace(',', '.').astype(float) / 1
        df['TIEMPO BARRA ETAPA 6'] = df['TIEMPO BARRA ETAPA 6'].astype(str).str.replace(',', '.').astype(float) / 1
        df['SET POINT DE TEMPERATURA ETAPA 1'] = df['SET POINT DE TEMPERATURA ETAPA 1'].astype(str).str.replace(',', '.').astype(float) / 1
        df['SET POINT DE TEMPERATURA ETAPA 2'] = df['SET POINT DE TEMPERATURA ETAPA 2'].astype(str).str.replace(',', '.').astype(float) / 1
        df['SET POINT DE TEMPERATURA ETAPA 3'] = df['SET POINT DE TEMPERATURA ETAPA 3'].astype(str).str.replace(',', '.').astype(float) / 1
        df['SET POINT ETAPA 4'] = df['SET POINT ETAPA 4'].astype(str).str.replace(',', '.').astype(float) / 1
        df['SET POINT DE TEMPERATURA ETAPA 5'] = df['SET POINT DE TEMPERATURA ETAPA 5'].astype(str).str.replace(',', '.').astype(float) / 1
        df['SET POINT DE TEMPERATURA ETAPA 6'] = df['SET POINT DE TEMPERATURA ETAPA 6'].astype(str).str.replace(',', '.').astype(float) / 1
        df['Numero de Batch'] = df['Numero de Batch'].fillna(0).astype(int)
        df['Presion diferencial'] = df['Presion diferencial'].astype(int)
        df['GAS ETAPA 1'] = df['GAS ETAPA 1'].astype(int)
        df['GAS ETAPA 2'] = df['GAS ETAPA 2'].astype(int)
        df['GAS ETAPA 3'] = df['GAS ETAPA 3'].astype(int)
        df['GAS ETAPA 4'] = df['GAS ETAPA 4'].astype(int)
        df['GAS ETAPA 5'] = df['GAS ETAPA 5'].astype(int)
        df['GAS ETAPA 6'] = df['GAS ETAPA 6'].astype(int)
        df['TIEMPO BARRA ETAPA 1'] = df['TIEMPO BARRA ETAPA 1'].astype(int)
        df['TIEMPO BARRA ETAPA 2'] = df['TIEMPO BARRA ETAPA 2'].astype(int)
        df['TIEMPO BARRA ETAPA 3'] = df['TIEMPO BARRA ETAPA 3'].astype(int)
        df['TIEMPO BARRA ETAPA 4'] = df['TIEMPO BARRA ETAPA 4'].astype(int)
        df['TIEMPO BARRA ETAPA 5'] = df['TIEMPO BARRA ETAPA 5'].astype(int)
        df['TIEMPO BARRA ETAPA 6'] = df['TIEMPO BARRA ETAPA 6'].astype(int)
        df['SET POINT DE TEMPERATURA ETAPA 1'] = df['SET POINT DE TEMPERATURA ETAPA 1'].astype(int)
        df['SET POINT DE TEMPERATURA ETAPA 2'] = df['SET POINT DE TEMPERATURA ETAPA 2'].astype(int)
        df['SET POINT DE TEMPERATURA ETAPA 3'] = df['SET POINT DE TEMPERATURA ETAPA 3'].astype(int)
        df['SET POINT ETAPA 4'] = df['SET POINT ETAPA 4'].astype(int)
        df['SET POINT DE TEMPERATURA ETAPA 5'] = df['SET POINT DE TEMPERATURA ETAPA 5'].astype(int)
        df['SET POINT DE TEMPERATURA ETAPA 6'] = df['SET POINT DE TEMPERATURA ETAPA 6'].astype(int)

    except Exception as ex:
        print(f"{fecha_hora}: Ha ocurrido el siguiente error: {ex}")
        return
    

    try:    
        # CURSOR PARA INGRESAR DATOS
        cursor_insert = cnn.cursor()
        ultimo = ultimo_registro()
    except Exception as ex:
        fecha_act = fecha_actual()
        print(f"{fecha_act}: Ups, algo salió mal")
        print(f"{fecha_hora}: Ha ocurrido el siguiente error: {ex}")
        return


    # CONTADOR DE REGISTROS
    contador = 0
    try:
        ultimoRegistro = ultimo[0]
        if ultimoRegistro == None:
            ultimoRegistro = datetime.strptime("17/01/2018 10:05:00", '%d/%m/%Y %H:%M:%S')
        else:
            ultimoRegistro = datetime.strftime(ultimoRegistro, '%d/%m/%Y %H:%M:%S')
            ultimoRegistro = datetime.strptime(ultimoRegistro, '%d/%m/%Y %H:%M:%S')
    except Exception as ex:
        print(f"{fecha_hora}: Ups, algo salió mal...")
        return     

    try:
        for i, row in df.iterrows():   
            
            # FORMATEO FECHA
            campo_fecha = row['dd-MM-yyyy H:mm:ss']
            v_fecha = datetime.strftime(campo_fecha, '%d/%m/%Y %H:%M:%S')
            fecha = datetime.strptime(v_fecha, '%d/%m/%Y %H:%M:%S')

            v_fecha1 = datetime.strftime(campo_fecha, '%Y/%m/%d %H:%M:%S')
            
            
            
            if fecha != ultimoRegistro and fecha > ultimoRegistro:
                
                try:
                    # INSERT SQL
                    sql = f'''INSERT INTO INFO_HORNO (
                                BATCH, FECHA, VARIEDAD, TEMP_SOBRE_GRANO, TEMP_BAJO_TELA, TEMP_AMBIENTE, 
                                HR_SOBRE_TELA, P_APERTURA_DAMPER, PRESION_DIFERENCIAL, GAS_TOTAL, 
                                GAS_ET_1, GAS_ET_2, GAS_ET_3, GAS_ET_4, GAS_ET_5, GAS_ET_6, 
                                TIEMPO_TOTAL, TIEMPO_BARRA_E1, TIEMPO_BARRA_E2, TIEMPO_BARRA_E3, 
                                TIEMPO_BARRA_E4, TIEMPO_BARRA_E5, TIEMPO_BARRA_E6, 
                                SP_TEMP_1, SP_TEMP_2, SP_TEMP_3, SP_TEMP_4, SP_TEMP_5, SP_TEMP_6
                            ) VALUES (
                                '{row['Numero de Batch']}',TO_DATE('{v_fecha1}', 'YYYY-MM-DD HH24:MI:SS'),'{row['Variedad']}', '{row['T Sobre Grano']}', 
                                '{row['T Bajo Tela']}', '{row['T AMBIENTE']}', '{row['%HR Sobre tela']}', 
                                '{row['Porcentaje de apertura de DAMPER']}', '{row['Presion diferencial']}', '{row['GAS TOTAL']}', 
                                '{row['GAS ETAPA 1']}', '{row['GAS ETAPA 2']}', '{row['GAS ETAPA 3']}', '{row['GAS ETAPA 4']}', 
                                '{row['GAS ETAPA 5']}', '{row['GAS ETAPA 6']}', '{row['TIEMPO TOTAL']}', '{row['TIEMPO BARRA ETAPA 1']}', 
                                '{row['TIEMPO BARRA ETAPA 2']}', '{row['TIEMPO BARRA ETAPA 3']}', '{row['TIEMPO BARRA ETAPA 4']}', 
                                '{row['TIEMPO BARRA ETAPA 5']}', '{row['TIEMPO BARRA ETAPA 6']}', '{row['SET POINT DE TEMPERATURA ETAPA 1']}', 
                                '{row['SET POINT DE TEMPERATURA ETAPA 2']}', '{row['SET POINT DE TEMPERATURA ETAPA 3']}', '{row['SET POINT ETAPA 4']}', 
                                '{row['SET POINT DE TEMPERATURA ETAPA 5']}', '{row['SET POINT DE TEMPERATURA ETAPA 6']}'
                            )'''

                    cursor_insert.execute(sql)
                    contador += 1
                except Exception as ex:
                    print(f"{fecha_hora}: Error en fila \n {v_fecha} - {row['Numero de Batch']}")
                    print(f"{fecha_hora}: Ha ocurrido el siguiente error: {ex}")
        # COMMIT 
        cnn.commit()
        cursor_insert.close()
        cnn.close()
    except TypeError:
        messagebox.showerror(message="Error en archivo, Favor informar a Depto. TI", title='ERROR')
        return
    except:
        return

    print(f"{fecha_hora}: Se han ingresado: {contador} registros")





### FUNCIÓN PARA PARAR CERRAR CONEXION BDD
def cerrar_conexion():
    fecha_hora = fecha_actual()
    try:
        cnn.close()
        print(f"{fecha_hora}: La conexión se ha cerrado")
    except:
        print(f"{fecha_hora}: Conexión cerrada...")
        
        


### FUNCIÓN PARA RECUPERAR ÚLTIMO REGISTRO DE BDD
def ultimo_registro():
    cursor = cnn.cursor()
    sql = "SELECT MAX(Fecha) FROM INFO_HORNO"
    cursor.execute(sql)

    global registro_fecha
    registro_fecha = cursor.fetchone()

    cursor.close()
    ultima_fecha = []
    for i in registro_fecha:
        ultima_fecha.append(i)
    return ultima_fecha
    

