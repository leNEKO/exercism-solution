def transform(legacy_data):

    new_data = dict()

    for val, letters in legacy_data.items():
        for c in letters:
            new_data.update({c.lower(): val})

    return new_data
