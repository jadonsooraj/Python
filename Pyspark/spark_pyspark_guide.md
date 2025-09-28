# PySpark & Apache Spark Learning Guide

This documentation provides a structured learning path for **Apache Spark** and **PySpark** (the Python API for Spark). It covers fundamental concepts, practical coding examples, hands-on exercises with sample datasets, and advanced topics to help you become proficient in big data processing with Spark.

---

## 1. Introduction to Spark & PySpark

### What is Apache Spark?
- Open-source distributed computing framework.
- Processes large-scale data efficiently across clusters.
- Provides APIs in **Scala, Java, Python (PySpark), and R**.
- Supports **batch processing, real-time streaming, machine learning, and graph processing**.

### Why PySpark?
- Python-friendly API for Spark.
- Integrates with popular libraries like Pandas, NumPy, scikit-learn.
- Widely used in data science and analytics.

---

## 2. Spark Core Concepts

### Spark Architecture
- **Driver Program**: Coordinates execution, runs main function.
- **Cluster Manager**: Manages resources (Standalone, YARN, Mesos, Kubernetes).
- **Executors**: Run tasks on worker nodes.
- **Resilient Distributed Datasets (RDDs)**: Core abstraction for fault-tolerant distributed data.

### Key Features
- **In-memory computation** (faster than Hadoop).
- **Lazy evaluation**.
- **Fault tolerance**.
- **Scalability**.

---

## 3. PySpark Setup

### Installation
```bash
pip install pyspark
```

### Starting PySpark
Working with pyspark requires to build a session:
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Learning PySpark") \
    .getOrCreate()
```

### Spark Shells
- `pyspark` → Interactive shell for Python.
- `spark-shell` → Scala shell.

---

## 4. PySpark Data Structures

### Resilient Distributed Dataset (RDD)
- Immutable distributed collection of objects.
- Supports transformations (map, filter) and actions (collect, count).

### DataFrame
- Distributed collection of data organized into named columns.
- Similar to Pandas DataFrame but optimized for big data.

### Dataset
- Strongly typed API (not available in PySpark, only Scala/Java).

---

## 5. Working with RDDs

```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# Transformations
rdd2 = rdd.map(lambda x: x * 2)
rdd3 = rdd2.filter(lambda x: x > 5)

# Actions
print(rdd3.collect())
print(rdd3.count())
```

**Exercise:**
1. Create an RDD with numbers 1–20.
2. Filter even numbers and multiply them by 3.
3. Count how many results you have.

**Sample Solution:**
```python
rdd = spark.sparkContext.parallelize(range(1, 21))
evens = rdd.filter(lambda x: x % 2 == 0)
result = evens.map(lambda x: x * 3)
print(result.collect())
print(result.count())
```

---

## 6. Working with DataFrames

### Creating DataFrames
```python
# From Python objects
data = [(1, "Alice", 29), (2, "Bob", 31)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)
df.show()

# From CSV
csv_df = spark.read.csv("employees.csv", header=True, inferSchema=True)
csv_df.printSchema()
```

### DataFrame Operations
```python
# Selection
df.select("name", "age").show()

# Filtering
df.filter(df.age > 30).show()

# Aggregation
df.groupBy("age").count().show()
```

**Exercise:**
1. Load a CSV file of employees (`id, name, dept, salary`).
2. Find employees with salary greater than 50,000.
3. Group employees by department and calculate average salary.

**Sample Dataset (`employees.csv`):**
```
id,name,dept,salary
1,Alice,HR,48000
2,Bob,Finance,52000
3,Charlie,IT,61000
4,Diana,Finance,45000
5,Evan,IT,72000
```

**Sample Solution:**
```python
df = spark.read.csv("employees.csv", header=True, inferSchema=True)
df.filter(df.salary > 50000).show()
df.groupBy("dept").avg("salary").show()
```

---

## 7. Spark SQL

```python
# Register DataFrame as SQL table
df.createOrReplaceTempView("people")

result = spark.sql("SELECT name, age FROM people WHERE age > 30")
result.show()
```

**Exercise:**
1. Load a student dataset into a DataFrame.
2. Register it as a SQL table.
3. Write SQL to find the top 3 students by marks.

**Sample Dataset (`students.csv`):**
```
id,name,marks
1,Arjun,85
2,Ravi,92
3,Sneha,78
4,Meera,95
5,Amit,88
```

**Sample Solution:**
```python
df = spark.read.csv("students.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("students")
top_students = spark.sql("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 3")
top_students.show()
```

---

## 8. Data Sources in PySpark

- **CSV**: `spark.read.csv()`
- **JSON**: `spark.read.json()`
- **Parquet**: `spark.read.parquet()`
- **Avro**: `spark.read.format("avro").load()`
- **Databases**: JDBC connectors

**Exercise:** Load a JSON dataset of products and query for products priced above 1000.

**Sample Dataset (`products.json`):**
```json
[
  {"id": 1, "name": "Laptop", "price": 1200},
  {"id": 2, "name": "Mouse", "price": 400},
  {"id": 3, "name": "Phone", "price": 1500}
]
```

**Sample Solution:**
```python
df = spark.read.json("products.json")
df.filter(df.price > 1000).show()
```

---

## 9. Advanced Concepts

### Window Functions
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("region").orderBy("amount")
df.withColumn("row_number", row_number().over(windowSpec)).show()
```

**Exercise:**
1. Load sales data with columns `(id, region, amount)`.
2. Use window functions to rank sales within each region.

**Sample Dataset (`sales.csv`):**
```
id,region,amount
1,North,200
2,North,500
3,South,300
4,South,700
5,East,450
```

**Sample Solution:**
```python
df = spark.read.csv("sales.csv", header=True, inferSchema=True)
windowSpec = Window.partitionBy("region").orderBy(df.amount.desc())
df.withColumn("rank", row_number().over(windowSpec)).show()
```

---

## 10. Spark Streaming

**Exercise:**
1. Create a socket stream on port 9999.
2. Send text messages and count word frequency in real time.

**Sample Solution:**
```python
stream_df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

from pyspark.sql.functions import split, explode
words = stream_df.select(explode(split(stream_df.value, " ")).alias("word"))
counts = words.groupBy("word").count()

query = counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```

---

## 11. Machine Learning with MLlib

**Exercise:**
1. Load a dataset with `features, label`.
2. Build a linear regression model.
3. Evaluate RMSE (Root Mean Square Error).

**Sample Dataset (`regression.csv`):**
```
feature,label
2.0,3.0
3.0,4.5
4.0,6.0
5.0,7.5
```

**Sample Solution:**
```python
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

df = spark.read.csv("regression.csv", header=True, inferSchema=True)
assembler = VectorAssembler(inputCols=["feature"], outputCol="features")
train_df = assembler.transform(df)

lr = LinearRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_df)
print("RMSE:", model.summary.rootMeanSquaredError)
```

---

## 12. Optimization Techniques

**Exercise:**
1. Create a large dataset with `join` operations.
2. Use broadcast join and compare performance with normal join.

**Sample Solution:**
```python
from pyspark.sql.functions import broadcast

big_df = spark.range(1, 1000000).withColumnRenamed("id", "big_id")
small_df = spark.range(1, 100).withColumnRenamed("id", "small_id")

# Normal join
big_df.join(small_df, big_df.big_id == small_df.small_id).count()

# Broadcast join
big_df.join(broadcast(small_df), big_df.big_id == small_df.small_id).count()
```

---

## 13. Deployment

- **Local Mode**: For testing on your machine.
- **Standalone Cluster**: Spark’s built-in cluster manager.
- **YARN / Kubernetes**: For enterprise-scale deployment.
- **AWS EMR / Databricks**: Managed Spark services.

---

## 14. Best Practices

- Understand data partitioning.
- Avoid using UDFs unless necessary (use built-in functions).
- Optimize joins with broadcast.
- Monitor jobs with **Spark UI**.
- Use **checkpointing** in streaming applications.

---

## 15. Resources for Further Learning

- [Official Spark Documentation](https://spark.apache.org/docs/latest/)
- *Learning Spark* by Jules Damji et al.
- Databricks Community Edition (free practice environment)

---

✅ This guide now includes **sample datasets and step-by-step solutions** for RDDs, DataFrames, SQL, Streaming, MLlib, and optimization exercises. You can copy these datasets into CSV/JSON files and practice directly in PySpark.

