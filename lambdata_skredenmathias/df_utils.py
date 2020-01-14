import pandas
from sklearn.model_selection import train_test_split  # For good measure

TEST_DF = pandas.DataFrame([1, 2, 3])

# Set pandas max displays function


def set_display_options(rows, columns):
    """
    Set Pandas display options for notebook
    """
    rows = pd.options.display.max_rows
    columns = pd.options.display.max_columns
    return rows, columns  # Doesn't work (returns (60, 0))

# train / val / test split function


def train_test_split(df):
    """
    Create train/val/test dataframes with test_size = .2, from dataframe df
    """
    from sklearn.model_selection import train_test_split
    train, val = train_test_split(df, test_size=.2, random_state=42)
    train, test = train_test_split(train, test_size=.2, random_state=42)
