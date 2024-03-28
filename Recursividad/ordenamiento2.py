def bubble_sort(vector):
    permutation = True
    iteración = 0
    while permutation == True:
        permutation = False
        iteración = iteración + 1
        for actual in range(0, len(vector) - iteración):
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
    print(vector) 
    
bubble_sort([10,2,20,80])
