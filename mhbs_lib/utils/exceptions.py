class TableIsEmptyError(Exception):
    """
    Exception raised when a table is found to be empty.

    This exception is used to indicate that the operation cannot proceed
    because the specified table is empty.

    :example:
    >>> if table_is_empty:
    >>>     raise TableIsEmptyError("The table is empty and cannot be processed.")
    """
    pass

class NotValidTableSaveMode(Exception):
    """
    Exception raised for invalid table save modes.

    This exception is used to indicate that the provided save mode for
    a table operation is not valid. Valid save modes might include 'append'
    and 'overwrite'.

    :example:
    >>> save_mode = 'invalid_mode'
    >>> if save_mode not in ['append', 'overwrite']:
    >>>     raise NotValidTableSaveMode(f"The save mode '{save_mode}' is not valid.")
    """
    pass

class NotValidOverwriteSchemaOption(Exception):
    """
    Exception raised for invalid overwrite schema options.

    This exception is used to indicate that the provided option for overwriting
    the schema is not valid. Valid options might include True and False.

    :example:
    >>> overwrite_schema = 'invalid_option'
    >>> if overwrite_schema not in [True, False]:
    >>>     raise NotValidOverwriteSchemaOption(
    >>>         f"The overwrite schema option '{overwrite_schema}' is not valid."
    >>>     )
    """
    pass
