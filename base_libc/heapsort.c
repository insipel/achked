#include <stdio.h>

/*
 * out params:
 *  1. array pointer
 * in param:
 *  1. max number of elems in the list
 */
extern int generate_array(int **, int);

void
swap_elems(int *a, int i, int j)
{
    int temp;

    temp = a[i];
    a[i] = a[j];
    a[j] = temp;

    return;
}

void
max_heapify(int *a, int index, int heap_size)
{
    int left = 2 * index;
    int right = (2 * index) + 1;
    int largest = index;

    if ((left < heap_size) && (a[index] < a[left])) {
        largest = left;
    }

    if ((right < heap_size) && (a[largest] < a[right])) {
        largest = right;
    }

    if (largest != index) {
        swap_elems(a, index, largest);
        max_heapify(a, largest, heap_size);
    }

    return;
}

int
build_max_heap(int *a, int length)
{
    int i, heap_size = length;

    for (i = length/2; i >= 0; i--) {
        max_heapify(a, i, heap_size);
    }

    return heap_size;
}

void
heap_sort(int *a, int num_elems)
{
    int heap_size, i;

    /*
     * 1. build heap.
     * 2. in a for loop, reduce the heap_size in each iteration and
     * taking out the last largest element.
     */
    heap_size = build_max_heap(a, num_elems);

    for (i = num_elems - 1; i >=0; i--) {
        swap_elems(a, 0, i);
        heap_size -= 1;
        max_heapify(a, 0, heap_size);
    }
}

int
main()
{
    int *a, num_elems = 0;

    num_elems = generate_array(&a, 20);

    while(!num_elems) {
        printf("Try again\n");
        num_elems = generate_array(&a, 20);
    }

    heap_sort(a, num_elems);
    print_array_elems(a, num_elems);

    return 0;
}
