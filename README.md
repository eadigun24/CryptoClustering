# CryptoClustering
## Challenge Notes
* The main requirements for this challenge was from the module 11 challenge details in bootcamp.

## Preparing the Data
* First I scale the data loaded from the CSV file. This is done using the 'StandardScaler()' from scikit-learn.
* After scaling the data, I create a DataFrame from the scaled data, and columns from the original dataframe.
    * Index on the resulting scaled dataframe is set to the values from the original dataframe.
        - A new column "coin_id" is created to store these values.
* Next we set out to find the best value for k.
    * In this step we iterate over a range of values from 1 to 11.
        - Create a KMeans model.
        - Fit the model with the data from the scaled dataframe.
        - store the model's inertia values.
        - we use the iterator values above and the stored inertia values to to plot an elbow curve to determine the best value for k.
* Proceeding, we cluster the data utilizing the original scaled data.
    * Following the pattern: Model - Fit - Predict; I:
        - Create a kMeans model.
        - Fit the model with the data from the scaled dataframe.
        - Predict the clusters using the scaled dataframe.
    * I then take a copy of the original dataframe, copy it to make a new dataframe "for the predictions"
        - Add a new column to the copied dataframe; name it "crypto_cluster".
        - Then Proceed to plot the data using a scatter plot.

## PCA Component Analysis
* In this section we set out to perform dimensionality reduction using PCA.
    * Create a PCA model with n_components = 3.
    * Fit the model with the scaled dataframe.
    * Then I proceed to analyze the explained variance ratio of the model.
* Next, we proceed to find the best k value for the PCA data
    - The k value from the previous step is then compared to the result k value from the PCA data.
* I then cluster the PCA data with KMeans.
    - the resuling dataframe is then plotted using a scatter plot for visual exploration.
* Finally I proceed to determine the weights of each feature on each Principal Component.
    - Details of the results are included in the notebook.
