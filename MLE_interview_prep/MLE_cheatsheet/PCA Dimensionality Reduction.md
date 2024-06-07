What is PCA?
• Based on the dataset find a new set of orthogonal feature vectors in such a way that the
data spread is maximum in the direction of the feature vector (or dimension)
• Rates the feature vector in the decreasing order of data spread (or variance)
• The datapoints have maximum variance in the first feature vector, and minimum variance
in the last feature vector
• The variance of the datapoints in the direction of feature vector can be termed as a
measure of information in that direction.
Steps
1. Standardize the datapoints
2. Find the covariance matrix from the given datapoints
3. Carry out eigen-value decomposition of the covariance matrix
4. Sort the eigenvalues and eigenvectors
Dimensionality Reduction with PCA
• Keep the first m out of n feature vectors rated by PCA. These m vectors will be the best m
vectors preserving the maximum information that could have been preserved with m vectors on the given dataset
Steps:
1. Carry out steps 1-4 from above
2. Keep first m feature vectors from the sorted eigenvector matrix
3. Transform the data for the new basis (feature vectors)
4. The importance of the feature vector is proportional to the magnitude of the eigen value