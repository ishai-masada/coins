from collections import namedtuple


def load_data(filename):
    """ Loads CSV data into namedtuples.
    """
    # Load raw text from file
    data = list()
    with open(filename) as f:
        raw_data = f.read().strip().splitlines()

    # Create namedtuple from CSV header
    Row = namedtuple('Row', raw_data[0])
    # Convert remaining data
    for row in raw_data[1:]:
        data.append(Row(*[float(col) for col in row.split(',')]))

    return data


data = load_data('data.csv')

def dfh(data, alt):
    for idx, row in enumerate(data):
        if row.alt == alt:
            return row.delta
        elif row.alt > alt:
            row_a, row_b = data[idx-1], data[idx]
            return  (alt - row_a.alt) / (row_b.alt - row_a.alt) * (row_b.delta - row_a.delta) + row_a.delta
