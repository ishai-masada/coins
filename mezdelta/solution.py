from collections import namedtuple

def load_data(filename):
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


def delta_from_alt(alt, data):
    target_alt = float(alt)

    last_idx = None
    # Iterate throw rows (and keep count)
    for idx, row in enumerate(data):
        # Exact match found
        if row.alt == target_alt:
            return row.delta
        # Current row exceeds target
        elif row.alt > target_alt:
            # No data to interpolate from
            if last_idx is None:
                return None
            # Get the last row for use in the following calculation
            last_row = data[last_idx]
            # Calculate and return the interpolated delta
            return last_row.delta + (target_alt - last_row.alt) \
                    * (row.delta - last_row.delta) / (row.alt - last_row.alt)
        last_idx = idx


data = load_data('data.csv')
