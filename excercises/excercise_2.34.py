import pandas as pd

def test_species_unique(df):
    """
    Test that verifies that the species column of a DataFrame has only unique values.
    """
    # Note: “unique” is a pandas function, not a method of dataframe objects! Right one should be .nunique method of dataframe objects, buuut there is a pandas series object method .unique that could work. Gotta test it in code.
    # Proof: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html 
    # Assertion:  negate(https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique )
    num_species = df['species'].nunique()
    num_rows = df.shape[0]
    assert num_species == num_rows

data = {
    'species': ['penguin', 'jaguar', 'human', 'Trevor'],
    'quantity': [200, 50, 8000000000, 1]
}
df_species = pd.DataFrame(data)

test_species_unique(df_species)