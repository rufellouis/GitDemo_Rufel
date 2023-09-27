from pyspark.sql import SparkSession

def read_csv_into_sparkdf():

    # Create a Spark session
    spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

    # Define the file path
    file_path = "example-data.csv"

    # Read the CSV file into a DataFrame
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    # Show the DataFrame
    df.show()

    # Output the spark dataframe as df
    return df

if __name__ == "__main__":
    df = read_csv_into_sparkdf()
    df_count = df.count()
