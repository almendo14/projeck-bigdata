# spark_train.py
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("RetailClustering").getOrCreate()

for i in range(1, 4):
    df = spark.read.csv(f"batch_{i}.csv", header=False, inferSchema=True)
    df_clean = df.selectExpr("_c5 as Quantity", "_c6 as Price") \
                 .dropna() \
                 .filter("Quantity > 0 AND Price > 0")

    assembler = VectorAssembler(inputCols=["Quantity", "Price"], outputCol="features")
    data = assembler.transform(df_clean)
    kmeans = KMeans(k=3, seed=1)
    model = kmeans.fit(data)
    model.save(f"model_{i}")
    print(f"Model {i} saved")
