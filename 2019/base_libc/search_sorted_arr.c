#include <stdio.h>
#include <stdlib.h>
#include "../practice_hdr.h"

extern int generate_array(int **, int);

int
compareFunc(const void *p1, const void *p2)
{
    return ( *((int *)p1) - *((int *)p2));
}

void
shift_array(int **arr, int num_elems)
{
    int i, shift = rand() % num_elems;
    int *arr1 = (int *) malloc(sizeof(int) * num_elems);

    printd("Shifting by %d elems\n", shift);

    for (i = 0; i < num_elems; i++) {
        arr1[(i + shift) % num_elems] = (*arr)[i];
    }
    free(*arr);
    *arr = arr1;
}

int
find_start_index(int *a, int num_elems)
{
    int start, end, middle, i;

    if (a[0] < a[num_elems - 1]) {
        return 0 /* array is not shifted */;
    }

    start = 0; end = num_elems - 1;
    while ( i < num_elems && (a[start] < a[end])) {

        middle = (start + end) /2;
        if (a[start] > a[middle]) {
            end = middle;
        } else {
        }
    }
}

int
main()
{

    int *arr, num_elems;
    
    num_elems = generate_array(&arr, 20);
    qsort(arr, num_elems, sizeof(int), compareFunc);


    printd("Sorted elements:\n");
    print_array_elems(arr, num_elems);

    shift_array(&arr, num_elems);
    print_array_elems(arr, num_elems);
}

