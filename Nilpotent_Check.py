import numpy as np


def create_matrix():
    dimension = int(input("Please enter matrix dimension: ")) # grab the dimension to create a square matrix
    if dimension == 1:
        print('Matrix of dimension 1 is just a number')
        return -1
    else:
        initial = np.zeros((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                value = int(input(f"Enter the value for [{i}][{j}]: "))
                initial[i][j] = value
        return initial


def NilpotentCheck():
    """ 
    NilpotentCheck() calls a helper function to create a matrix
    Then, it iterates through the matrix, and the result of the matrix multiplied by itself
    to see if the given matrix is nilpotent.
    """
    zero_count = 0 # initializes counting variable
    starting = to_check = create_matrix()  # setting starting for a static variable for later, to check will change
    dim = to_check.ndim # variable to hold the dimension of the matrix
    result = starting # setting a reference to the starting matrix
    # this for loop multiplies the matrix with each iteration
    for i in range(dim):
        # iterate through the number of times that a matrix can be multiplied for it to be a nilpotent matrix
        for j in range(dim):
            # iterate through rows
            for k in range(dim):
                # iterate through columns
                if to_check[j][k] == 0:
                    # checks each entry in the matrix
                    # if the entry is 0, increment zero_count
                    zero_count += 1
        if zero_count == dim * dim:
            # if the number of zeros is equal to the total number of entries
            print(f'\n{starting} is nilpotent')
            return 1
        zero_count = 0
        result = np.matmul(to_check, starting)
        to_check = result
        # end of matrix check, loop back and multiply again
    print(f"{starting} is not nilpotent")
    return -1


if __name__ == '__main__':
    NilpotentCheck()
