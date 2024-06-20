from functools import reduce
from typing import List, Optional

from delta.tables import DeltaTable
from pyspark.sql  import DataFrame, SparkSession, Column
from pyspark.sql.functions import col, expr, lit, when

from .exceptions import TableIsEmptyError,NotValidTableSaveMode,NotValidOverwriteSchemaOption
from .logger_utils import logging_var


def get_spark_session(options: Optional[dict] = None) -> SparkSession:

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

def optmize_delta_table(
    spark: SparkSession,
    table_path: str,
    zorder_by: Optional[List[str]] = None
    ) -> bool:
    pass
