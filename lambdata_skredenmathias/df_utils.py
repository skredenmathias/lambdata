import pandas
from sklearn.model_selection import train_test_split  # For good measure

TEST_DF = pandas.DataFrame([1, 2, 3])

# Set pandas max displays function


def set_display_options(rows, columns):  # 3rd: pandas option
    """
    Set Pandas display options for notebook
    """
    pd.set_option('display.max_rows', rows)
    pd.set_option('display.max_columns', columns)
    return rows, columns

# train / val / test split function


def train_test_split(df, random_state=42):
    """
    Create train/val/test dataframes with test_size = .2, from dataframe df
    """
    if len(df) < 3:
        print('no bueno')
    train, test = train_test_split(df, test_size=.2, random_state=random_state)
    train, val = train_test_split(
        train, test_size=.2, random_state=random_state)
    return train, test, val
