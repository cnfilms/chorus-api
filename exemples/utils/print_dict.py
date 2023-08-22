import inspect


def print_as_table(obj):
    data_dict = vars(obj) if hasattr(obj, '__dict__') else obj if isinstance(obj, dict) else None
    # Get the keys and values from the dictionary
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    # Determine the maximum width for each column
    max_key_width = max(len(str(key)) for key in keys)
    max_value_width = max(len(str(value)) for value in values)

    # Print the table header
    print(f"+{'-' * (max_key_width + 2)}+{'-' * (max_value_width + 2)}+")
    print(f"| {'Key':<{max_key_width}} | {'Value':<{max_value_width}} |")
    print(f"+{'-' * (max_key_width + 2)}+{'-' * (max_value_width + 2)}+")

    # Print the rows
    for key, value in data_dict.items():
        print(f"| {str(key):<{max_key_width}} | {str(value):<{max_value_width}} |")
        if isinstance(value, list):
            print(f"\n *** Affichage de la clé : [{key}]")
            print(f"+{'-' * (max_key_width + 2)}+{'-' * (max_value_width + 2)}+")
            print_list_as_table(value)
            print("\n")

        if hasattr(value, '__dict__'):
            print_as_table(value.__dict__)

    # Print the table footer
    print(f"+{'-' * (max_key_width + 2)}+{'-' * (max_value_width + 2)}+")


def print_list_as_table(data):
    if not data:
        print("No data to display.")
        return

        # Get the column headers from the first object's attribute names
    headers = list(data[0].__dict__.keys())

    # Determine the maximum width for each column based on header and data values
    col_widths = [max(len(str(header)), max(len(str(getattr(row, header))) for row in data)) for header in headers]

    # Print the headers
    for i, header in enumerate(headers):
        print(f"{header:{col_widths[i]}}", end=' ')
    print()

    # Print the data rows
    for row in data:
        for i, header in enumerate(headers):
            value = getattr(row, header)
            print(f"{str(value):{col_widths[i]}}", end=' ')
        print()
