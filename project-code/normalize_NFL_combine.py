import numpy as np
import pandas as pd


def normalize_nfl_combine(nfl, nfl_2019, position):
    # Inlcudes only numbers and applies the position filter
    nfl_numeric = nfl[nfl.Pos == position].select_dtypes(include=[np.number])
    nfl_2019_numeric = nfl_2019[nfl_2019.Pos == position].select_dtypes(include=[np.number])

    # Creates tables for both
    nfl_df = pd.DataFrame(data=nfl_numeric)
    distance_columns = nfl_df[['Wt (lbs)', '40YD (s)', 'Vertical (in)', 'BenchReps', 'Broad Jump (in)',
                               '3Cone (s)', 'Shuttle (s)']]

    nfl_df_2019 = pd.DataFrame(data=nfl_numeric)
    distance_columns = nfl_df_2019[['Wt (lbs)', '40YD (s)', 'Vertical (in)', 'BenchReps', 'Broad Jump (in)',
                                    '3Cone (s)', 'Shuttle (s)']]
    # Normalize Datasets
    nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
    nfl_normalized.fillna(0, inplace=True)
    nfl_normalized_2019 = (nfl_2019_numeric - nfl_2019_numeric.mean()) / nfl_2019_numeric.std()
    nfl_normalized_2019.fillna(0, inplace=True)

    return nfl_normalized, nfl_normalized_2019
