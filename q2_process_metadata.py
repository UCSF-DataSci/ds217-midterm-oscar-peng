#!/usr/bin/env python3

# TODO: Add shebang line: #!/usr/bin/env python3
# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.

def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    config = {}
    with open(filepath, 'r') as file:
        for row in file:
            key, value = row.strip().split('=')
            config[key] = value
    return config


def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    results = {}
    if not config['sample_data_rows'].isdigit() or int(config['sample_data_rows']) <= 0:
        results['sample_data_rows'] = False
    else:
        results['sample_data_rows'] = True

    if not config['sample_data_min'].isdigit() or int(config['sample_data_min']) < 1:
        results['sample_data_min'] = False
    else:
        results['sample_data_min'] = True

    if not config['sample_data_max'].isdigit() or int(config['sample_data_max']) <= int(config['sample_data_min']):
        results['sample_data_max'] = False
    else:
        results['sample_data_max'] = True

    return results


def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """
    # TODO: Parse config values (convert strings to int)
    # TODO: Generate random numbers and save to file
    # TODO: Use random module with config-specified range
    import random
    rows = int(config['sample_data_rows'])
    min_val = int(config['sample_data_min'])
    max_val = int(config['sample_data_max'])
    with open(filename, 'w') as file:
        for i in range(rows):
            number = random.randint(min_val, max_val)
            file.write(f"{number}\n")



def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    n = len(data)
    total = sum(data)
    mean = total / n if n > 0 else 0
    sorted_data = sorted(data)
    median = (sorted_data[n // 2] if n % 2 != 0 else
              (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2) if n > 0 else 0
    return {'mean': mean, 'median': median, 'sum': total, 'count': n}


if __name__ == '__main__':
    # TODO: Test your functions with sample data
    # Example:
    # config = parse_config('q2_config.txt')
    # validation = validate_config(config)
    # generate_sample_data('data/sample_data.csv', config)
    config = parse_config('q2_config.txt')
    validation = validate_config(config)
    generate_sample_data('data/sample_data.csv', config)
    print("Config:", config)
    print("Validation:", validation)

    # TODO: Read the generated file and calculate statistics
    with open('data/sample_data.csv', 'r') as file:
        data = [int(line.strip()) for line in file]
    stats = calculate_statistics(data)
    print("Statistics:", stats)

    # TODO: Save statistics to output/statistics.txt
    with open('output/statistics.txt', 'w') as file:
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")
