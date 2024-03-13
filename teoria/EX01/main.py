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
  serieTemporal: [  (lista com todos os registros da ultima hora, ordenado do mais antigo ao mais recente, apenas da ultima hora)
    {               (documento do registro)
      intervalo,     (intervalo de tempo entre esse registro e o próximo)
      valorSensor   (temperatura)
    }
  ],
}
"""


def atualiza_serie_temporal(serie_temporal, timer, temperatura):
    nova_serie_temporal = serie_temporal

    nova_serie_temporal.append({
        'intervalo': timer,
        'valorSensor': temperatura
    })

    while True:
        intervalo = 0
        for registro in nova_serie_temporal:
            intervalo += registro['intervalo']

        # verifica se o intervalo total entre os registros é maior que uma hora
        if intervalo > 360:
            # caso seja, remove o mais antigo
            nova_serie_temporal.pop(0)
        else:
            # caso nao seja, retorna a nova serie
            return nova_serie_temporal


def ler_sensor(nome_sensor, timer):
    while True:
        client = MongoClient('mongodb://localhost:27017', )
        db = client['bancoiot']
        sensores = db.sensores

        result = sensores.find({'nomeSensor': nome_sensor})[0]
        serie_temporal = result['serieTemporal']

        if result['sensorAlarmado']:
            print(
                f'{nome_sensor}: Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!\n'
            )

            temperatura = result['valorSensor']
            serie_temporal = atualiza_serie_temporal(
                serie_temporal,
                timer,
                temperatura
            )

            sensores.update_one(
                {'nomeSensor': nome_sensor},
                {'$set': {
                    'serieTemporal': serie_temporal
                }}
            )

            sleep(timer)
            continue

        temperatura = randint(30, 40)
        unidade_medida = 'C°'
        sensor_alarmado = True if temperatura > 38 else False
        serie_temporal = atualiza_serie_temporal(
            serie_temporal,
            timer,
            temperatura
        )

        sensores.update_one(
            {'nomeSensor': nome_sensor},
            {'$set': {
                'valorSensor': temperatura,
                'sensorAlarmado': sensor_alarmado,
                'serieTemporal': serie_temporal
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
