<<<<<<< HEAD
# --- CÓDIGO COMPLETO RASPBERRY + SENSOR DHT + MYSQL ---
# (Datos de conexión y nombres de BD/tablas se dejan para rellenar)

import MySQLdb
=======
# Home_Weather_Display.py
#
# This is an project for using the Grove RGB LCD Display and the Grove DHT Sensor from the GrovePi starter kit
#
# In this project, the Temperature and humidity from the DHT sensor is printed on the RGB-LCD Display
#
#
# Note the dht_sensor_type below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
#
# For more info please see: http://www.dexterindustries.com/topic/537-6c-displayed-in-home-weather-project/
#
'''
The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

>>>>>>> 95f1cb636e07aadd5223216948a6a1a3a1605955
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

<<<<<<< HEAD
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
=======
dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor

# set green as backlight color
# we need to do it just once
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(0,255,0)

while True:
    try:
        # get the temperature and Humidity from the DHT sensor
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum,"%")

        # check if we have nans
        # if so, then raise a type error exception
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')

        t = str(temp)
        h = str(hum)

        # instead of inserting a bunch of whitespace, we can just insert a \n
        # we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
        setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")

    except (IOError, TypeError) as e:
        print(str(e))
        # and since we got a type error
        # then reset the LCD's text
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        # since we're exiting the program
        # it's better to leave the LCD with a blank text
        setText("")
        break

    # wait some time before re-updating the LCD
    sleep(0.05)
>>>>>>> 95f1cb636e07aadd5223216948a6a1a3a1605955
