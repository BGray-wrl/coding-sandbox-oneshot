def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []
    if len(array) == 1:
        return list(array)

    first_val = array[0]
    last_val = array[-1]
    
    # Create a copy of the array to avoid modifying the original
    copied_array = list(array)

    if (first_val + last_val) % 2 == 0:  # Even sum
        copied_array.sort(reverse=True)
    else:  # Odd sum
        copied_array.sort()
    
    return copied_array
