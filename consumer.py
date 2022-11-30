import json
import db
from kafka import KafkaConsumer
# value_deserializer=lambda x: json.load(x.decode('utf- 8'))
consumer = KafkaConsumer('number', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id='my_group_id',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                         consumer_timeout_ms=10000)


for message in consumer:
    print('Topic:', message.topic)
    print('Partition:', message.partition)
    print('Offset:', message.offset)
    print('Key:', message.key)
    print('Value:', message.value)

    get_value = message.value
    value_num = get_value['number']

    print('Result:', value_num)

    insert_in_table = db.DataFromKafka(data=value_num)
    db.session.add(insert_in_table)
    print('{} добавлено в таблицу {}'.format(value_num, db.DataFromKafka.__tablename__))

    db.session.commit()
    print('Commit!')
    print('-' * 30)
