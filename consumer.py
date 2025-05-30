from kafka import KafkaConsumer
import json
import csv
import time

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

batch = []
batch_size = 10
output_file = f'dataset/output_{int(time.time())}.csv'

print("Consumer started...")

for message in consumer:
    decoded = message.value.decode('utf-8')
    batch.append(decoded)
    print(f"Received: {decoded}")

    if len(batch) >= batch_size:
        print(f"Saving batch of {len(batch)} to {output_file}")
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for line in batch:
                writer.writerow([line])
        break  # Hentikan setelah 1 batch tersimpan, untuk pengujian awal
