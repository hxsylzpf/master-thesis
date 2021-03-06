'''
Author: Sebastian Alfers
This file is part of my thesis 'Evaluation and implementation of cluster-based dimensionality reduction'
License: https://github.com/sebastian-alfers/master-thesis/blob/master/LICENSE
'''

from sklearn.random_projection import SparseRandomProjection, GaussianRandomProjection


def getGaussianRP(new_dimension):
    return GaussianRandomProjection(n_components=new_dimension)

def getSparseRP(new_dimension):
    return SparseRandomProjection(n_components=new_dimension)

# scikit-learn implementation: gaussian matrix
def gaussianRP(data, new_dimension):
    rp = getGaussianRP(new_dimension)
    return rp.fit_transform(data)

# scikit-learn implementation: sparse matrix
def sparseRP(data, new_dimension):
    rp = getSparseRP(new_dimension)
    return rp.fit_transform(data)
