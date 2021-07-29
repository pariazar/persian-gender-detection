import persianutils as pu
import re
import pandas as pd


def preprocessData(name):
    return re.sub(r'/^\s+|^0-9+|^۰-۹|[^(آ-ی)(a-z)]','', pu.standardize(name))


def detectGender(name):
    name = preprocessData(name)
    df = pd.read_csv('finalDB.csv')
    detectionResult = df.query('name == '+'"'+name+'"')
    if not detectionResult.empty:
        if detectionResult.iloc[0]["gender"] == 'M':
            return 'male'
        elif detectionResult.iloc[0]["gender"] == 'F':
            return 'female'
    else:
        return 'unknown'
        