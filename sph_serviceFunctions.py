import numpy as np

def find_nearest(array, value):
    """
       Find the index of the element in array with
       the nearest value to a given number.
       https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    # Original version returns value
    #return array[idx]
    return idx, array[idx]
