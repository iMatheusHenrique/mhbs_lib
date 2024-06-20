from functools import reduce
from typing import List, Optional,Dict

from delta.tables import DeltaTable
from pyspark.sql  import DataFrame, SparkSession, Column,DataFrameReader
from pyspark.sql.functions import col, expr, lit, when

from .exceptions import TableIsEmptyError,NotValidTableSaveMode,NotValidOverwriteSchemaOption
from .logger_utils import logging_var


def get_spark_session(
        options: Optional[dict] = None
    ) -> SparkSession:
    """
    Create and return a SparkSession object with optional configurations.

    :param options: A dictionary of Spark configuration options.
    :type options: Optional[dict]
    :return: A SparkSession object.
    :rtype: SparkSession
    :raises TypeError: If options is not a dictionary or None.

    :example:
    >>> spark = get_spark_session({'spark.app.name': 'MyApp'})
    >>> isinstance(spark, SparkSession)
    True
    """
    if not isinstance(options, dict) and options is not None:
        raise TypeError("Options parameters must be dict type")

    spark_builder = SparkSession.builder.enableHiveSupport()

    if options:
        logging_var(f"{options=}")

        spark_builder = reduce(
            lambda x, y: x.config(y[0],y[1]),
            options.items(),spark_builder
            )

    spark_session: SparkSession = spark_builder.getOrCreate()

    return spark_session


def save_as_table(
    df: DataFrame,
    mode: str,
    database: str,
    table_name: str,
    table_path: str,
    partition_by: Optional[List[str]] = None,
    overwrite_schema: str = False
    ) -> bool:
    """
    Save a Spark DataFrame as a table in a specified database.

    :param df: The DataFrame to be saved.
    :type df: DataFrame
    :param mode: The mode of saving ('append' or 'overwrite').
    :type mode: str
    :param database: The name of the database.
    :type database: str
    :param table_name: The name of the table.
    :type table_name: str
    :param table_path: The file path to save the table.
    :type table_path: str
    :param partition_by: List of columns to partition the table by, defaults to None.
    :type partition_by: Optional[List[str]], optional
    :param overwrite_schema: Whether to overwrite the schema, defaults to False.
    :type overwrite_schema: bool, optional
    :return: True if the table is successfully saved.
    :rtype: bool
    :raises NotValidTableSaveMode: If the save mode is not valid.
    :raises TypeError: If the DataFrame is not a Spark DataFrame.
    :raises NotValidOverwriteSchemaOption: If the overwrite_schema option is not valid.

    :example:
    >>> df = spark.createDataFrame([(1, 'a'), (2, 'b')], ['id', 'value'])
    >>> save_as_table(df, 'overwrite', 'default', 'my_table', '/path/to/table')
    True
    """
    valid_save_modes: List[str] = ["append", "overwrite"]
    valido_overwrite_schema_options: List[str] = ["True","False"]
    table_on_catalog: str = f"{database}.{table_name}"
    is_table_partitionated: bool = partition_by is not None
    save_format: str = "delta"

    if mode.lower() not in valid_save_modes:
        raise NotValidTableSaveMode(
            f"The mode write must be in {valid_save_modes}, the receibed is  {mode}"
            )

    if not isinstance(df, DataFrame):
        raise TypeError("The df informed must be a spark DataFrame")


    if overwrite_schema not in valido_overwrite_schema_options:
        raise NotValidOverwriteSchemaOption(
            f"The overwrite_schema informed must be in {valido_overwrite_schema_options}, the received is  {overwrite_schema}"
            )

    if is_table_partitionated:
        df.write.partitionBy(*partition_by).mode(mode).format(save_format).option(
            "path", table_path
        ).option("overwriteschema", overwrite_schema).saveAsTable(table_on_catalog)
    else:
        df.write.mode(mode).format(save_format).option(
            "path", table_path
        ).option("overwriteschema", overwrite_schema).saveAsTable(table_on_catalog)

    logging_var("WRITE TABLE FINISHED")
    return True


def optimize_delta_table(
    spark: SparkSession,
    table_path: str,
    zorder_by: Optional[List[str]] = None
    ) -> bool:
    """
    Optimize a Delta table at the specified path.

    :param spark: The SparkSession object.
    :type spark: SparkSession
    :param table_path: The file path of the Delta table.
    :type table_path: str
    :param zorder_by: List of columns to Z-Order by, defaults to None.
    :type zorder_by: Optional[List[str]], optional
    :return: True if the optimization is successful.
    :rtype: bool
    """
    pass


def read_csv(
    spark: SparkSession,
    reader_config: Dict[str, str],
    csv_file_path: str
    ) -> DataFrame:
    """
    Read a CSV file into a Spark DataFrame using the provided SparkSession and configuration.

    :param spark: The SparkSession object.
    :type spark: SparkSession
    :param reader_config: A dictionary of configuration options for the Spark CSV reader.
    :type reader_config: Dict[str, str]
    :param csv_file_path: The file path to the CSV file.
    :type csv_file_path: str
    :return: A DataFrame containing the data from the CSV file.
    :rtype: DataFrame

    :example:
    >>> spark = get_spark_session()
    >>> config = {'header': 'true', 'inferSchema': 'true'}
    >>> df = read_csv(spark, config, '/path/to/file.csv')
    >>> df.show()
    """

    spark_reader: DataFrameReader = reduce(
        lambda x,y: x.option(y[0], y[1]),
        reader_config.items(),
        spark.read
        )

    delimieter_of_csv_file: str = reader_config.get("delimiter",";")

    source_csv_df: DataFrame = spark_reader.csv(
        csv_file_path,
        sep=delimieter_of_csv_file
        )

    return source_csv_df
