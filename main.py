import random
import time
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DeAdPoOl2001",
    database="diploma_schema"
)

c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS oxygen_sensor_data
#              (timestamp DATETIME, oxygen_level FLOAT)''')

while True:
    oxygen_level = random.uniform(0, 5)

    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    c.execute("INSERT INTO oxygen_data (timestamp, oxygen_level) VALUES (%s, %s)", (current_time, oxygen_level))

    conn.commit()

    time.sleep(1)

