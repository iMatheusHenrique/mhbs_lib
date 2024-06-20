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



def check_table_empty(table_data):
    """
    Check if the given table data is empty and raise an exception if it is.

    :param table_data: Data of the table to be checked.
    :type table_data: list
    :raises TableIsEmptyError: If the table data is empty.
    """
    if not table_data:
        raise TableIsEmptyError("The table is empty and cannot be processed.")

def validate_save_mode(save_mode):
    """
    Validate the table save mode and raise an exception if it is invalid.

    :param save_mode: The save mode to be validated.
    :type save_mode: str
    :raises NotValidTableSaveMode: If the save mode is not valid.
    """
    valid_save_modes = ['append', 'overwrite']
    if save_mode not in valid_save_modes:
        raise NotValidTableSaveMode(f"The save mode '{save_mode}' is not valid.")

def validate_overwrite_schema_option(overwrite_schema):
    """
    Validate the overwrite schema option and raise an exception if it is invalid.

    :param overwrite_schema: The overwrite schema option to be validated.
    :type overwrite_schema: bool
    :raises NotValidOverwriteSchemaOption: If the overwrite schema option is not valid.
    """
    valid_options = [True, False]
    if overwrite_schema not in valid_options:
        raise NotValidOverwriteSchemaOption(
            f"The overwrite schema option '{overwrite_schema}' is not valid."
        )
