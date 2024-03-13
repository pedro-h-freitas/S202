from pymongo import MongoClient

from threading import Thread
from random import randint
from time import sleep

"""
{
  _id,              (gerado automaticamente)
  nomeSensor,       (Ex:  Temp1,  Temp2,  etc..)
  valorSensor,      (temperatura gerada aleatoriamente no Python)
  unidadeMedida,    (C° para todos)
  sensorAlarmado    (setado inicialmente com o valor false e true quando temperatura > 38)
}
"""


def ler_sensor(nome_sensor, timer):
    while True:
        client = MongoClient('mongodb://localhost:27017', )
        db = client['bancoiot']
        sensores = db.sensores

        result = sensores.find({'nomeSensor': nome_sensor})[0]

        if result['sensorAlarmado']:
            print(
                f'{nome_sensor}: Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!\n'
            )

            sleep(timer)
            continue

        temperatura = randint(30, 40)
        unidade_medida = 'C°'
        sensor_alarmado = True if temperatura > 38 else False

        sensores.update_one(
            {'nomeSensor': nome_sensor},
            {'$set': {
                'valorSensor': temperatura,
                'sensorAlarmado': sensor_alarmado,
            }}
        )

        print(f'{nome_sensor}: {temperatura}{unidade_medida}\n')
        if sensor_alarmado:
            print(
                f'{nome_sensor}: Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!'
            )

        sleep(timer)


x = Thread(target=ler_sensor, args=('Temp1', 1))
y = Thread(target=ler_sensor, args=('Temp2', 1))
z = Thread(target=ler_sensor, args=('Temp3', 1))

x.start()
y.start()
z.start()
