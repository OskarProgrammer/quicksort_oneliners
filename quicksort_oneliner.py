testing_list = [2,1,2,5,1,12321,113123131,1211,2,21,7435,12,321,521]

quicksort_pivot_in_half = lambda array: array if len(array) < 2 else \
        quicksort_pivot_in_half([x for x in array[0:len(array)//2] if x <= array[len(array)//2]] + \
                  [x for x in array[len(array)//2 + 1:] if x <= array[len(array)//2]]) + \
        [array[len(array)//2]] + \
        quicksort_pivot_in_half([x for x in array[0:len(array)//2] if x > array[len(array)//2]] + \
                  [x for x in array[len(array)//2 + 1:] if x > array[len(array)//2]])

print(quicksort_pivot_in_half(testing_list))


quicksort_pivot_on_the_first_index = lambda array: array if len(array) < 2 else \
        quicksort_pivot_on_the_first_index([x for x in array[1:] if x <= array[0]]) + \
        [array[0]] + \
        quicksort_pivot_on_the_first_index([x for x in array[1:] if x > array[0]])

print(quicksort_pivot_on_the_first_index(testing_list))