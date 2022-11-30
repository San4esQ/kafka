import json
from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for number in range(4):
    print('Number:', number)

    data = {'number': number}
    result = producer.send('number', key=b'hello', value=data).get(10)

    print('Topic:', result.topic)
    print('Partition:', result.partition)
    print('Offset:', result.offset)

    producer.flush()
    print('Flush')
    print('-' * 30)
    sleep(3)

