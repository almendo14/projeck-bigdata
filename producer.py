import csv
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'online-retail'

with open('dataset/OnlineRetail.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.reader(file)
    header = next(reader)  # skip header
    for row in reader:
        line = ','.join(row)
        producer.send(topic, line.encode('utf-8'))
        print(f"Sent: {line}")
        time.sleep(random.uniform(0.5, 2))  # delay 0.5 to 2 seconds

producer.flush()
producer.close()
