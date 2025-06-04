# Proyek Big Data: Simulasi Streaming Data Retail

Proyek ini mensimulasikan aliran data streaming dari dataset **OnlineRetail.csv** menggunakan Apache Kafka dan memprosesnya dengan Apache Spark. Tujuan utama proyek adalah memahami konsep real-time data streaming dan bagaimana data diproses secara batch.

## 🗂️ Struktur Proyek

projeck-bigdata/
│
├── dataset/
│ └── OnlineRetail.csv # Dataset utama
│
├── producer.py # Mengirim data ke Kafka topic (simulasi streaming)
├── consumer.py # Menerima data dari Kafka dan simpan per batch
├── docker-compose.yml # Menjalankan Kafka & Zookeeper dengan Docker
└── README.md # Dokumentasi proyek ini


---

## 📦 Tools & Teknologi

- **Apache Kafka** (via Docker - Bitnami image)
- **Apache Zookeeper** (via Docker)
- **Apache Spark** (opsional, untuk pengolahan batch selanjutnya)
- **Python** dengan library:
  - `kafka-python`
  - `pandas`

---

## 🚀 Cara Menjalankan

## 1 Jalankan Kafka dan Zookeeper (dengan docker)
docker-compose up -d
![Screenshot 2025-05-31 203341](https://github.com/user-attachments/assets/18cdc48c-a68a-4630-85ad-e1890b25218e)


Pastikan container Kafka dan Zookeeper berjalan
docker ps
![Screenshot 2025-05-31 203436](https://github.com/user-attachments/assets/fa971a4c-b799-4e2d-8d9c-a08a3b30201d)


## 2 Jalankan producer.py untuk mengirim data
python producer.py

produser python berjalan dengan baik
![Image](https://github.com/user-attachments/assets/fdee6b85-06f0-47a0-8f35-6b1e88a05834)

## 3 Jalankan consumer.py untuk menerima data
python consumer.py



