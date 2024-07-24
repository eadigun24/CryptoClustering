# Import required libraries and dependencies
import pandas as pd
from sklearn.cluster import KMeans

def determine_best_kvalue(data):
    """ Creates a Dataframe of k values and inertia. The k values range from 1 - 11. and the inertia values
    are retrieved from the KMeans model. The values are iterated over the k_values list times.

    Args:
        data (DataFrame): This is the DataFRame whose data we intend to fit the model with.

    Returns:
        list of int: the k values in the range 1 - 11.
        list of inertia: the inertia values of the model per iteration.
        DataFrame: The DataFrame with the elbow curve data.
    """
    # Create a list with the number of k-values to try
    # Use a range from 1 to 11
    k_values = list(range(1, 11))

    # Create an empty list to store the inertia values
    inertia = []

    # Create a for loop to compute the inertia with each possible value of k
    # Inside the loop:
    # 1. Create a KMeans model using the loop counter for the n_clusters
    # 2. Fit the model to the data using the scaled DataFrame
    # 3. Append the model.inertia_ to the inertia list
    for k in k_values:
        model = KMeans(n_clusters=k, n_init='auto', random_state=1)
        model.fit(data)
        inertia.append(model.inertia_)

    # Create a dictionary with the data to plot the Elbow curve
    elbow_data = {"k": k_values, "inertia": inertia}

    # Create a DataFrame with the data to plot the Elbow curve
    elbow_df = pd.DataFrame(elbow_data)

    return (k_values, inertia, elbow_df)