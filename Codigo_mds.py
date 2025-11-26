# --- CÓDIGO COMPLETO RASPBERRY + SENSOR DHT + MYSQL ---
# (Datos de conexión y nombres de BD/tablas se dejan para rellenar)

import MySQLdb
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

# ---------------- CONFIGURACIÓN SENSOR DHT ----------------
dht_sensor_port = 7      # Puerto del sensor DHT
dht_sensor_type = 0      # 0 = azul, 1 = blanco

# Configurar color del LCD
setRGB(0, 255, 0)

# ---------------- CONFIGURACIÓN BASE DE DATOS ----------------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "MDS123"
DB_NAME = "sensores"              

def conectar_bd():
    return MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME
    )
# ------------------------------------------------------------
# LOOP PRINCIPAL
# ------------------------------------------------------------
while True:
    try:
        # Leer temperatura y humedad del sensor
        [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
        print("Temp =", temp, "Humidity =", hum)

        # Validar NaN
        if isnan(temp) or isnan(hum):
            raise TypeError("nan error")

        # Convertir a texto
        t = str(temp)
        h = str(hum)

        # Mostrar en LCD
        setText_norefresh("Temp : " + t + " C\n" + "Humidity : " + h + "%")

        # Guardar en BD
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            consulta = "INSERT INTO tabla_datos (temperatura, humedad) VALUES (%s, %s);"  # Rellenar nombre de tabla
            cursor.execute(consulta, (temp, hum))
            conexion.commit()
            conexion.close()
            print("Datos guardados en la BD")
        except MySQLdb.Error as e:
            print("Error BD:", e)

    except (IOError, TypeError) as e:
        print("Sensor error:", e)
        setText("")

    except KeyboardInterrupt:
        print("Programa detenido")
        setText("")
        break

    sleep(0.85)