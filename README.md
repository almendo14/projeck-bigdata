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

Pastikan container Kafka dan Zookeeper berjalan
docker ps

## 2 Jalankan producer.py untuk mengirim data
python producer.py

## 3 Jalankan consumer.py untuk menerima data
python consumer.py



