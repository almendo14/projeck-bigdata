from flask import Flask, request, jsonify
from pyspark.ml.clustering import KMeansModel
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors

app = Flask(__name__)
spark = SparkSession.builder.appName("RetailAPI").getOrCreate()

models = [KMeansModel.load(f"model_{i}") for i in range(1, 4)]

@app.route('/predict/<int:model_id>', methods=['POST'])
def predict(model_id):
    data = request.json
    quantity = float(data['quantity'])
    price = float(data['price'])
    df = spark.createDataFrame([(Vectors.dense([quantity, price]),)], ['features'])
    prediction = models[model_id - 1].transform(df).collect()[0].prediction
    return jsonify({'cluster': int(prediction)})

if __name__ == '__main__':
    app.run(port=5000)
