#include <stdio.h>
#include <stdlib.h>

#define PARENT(i)  (i / 2)
#define LEFT(i)  (2 * i)
#define RIGHT(i) (2 * i + 1)

void print_arr_elem(int *elems, int num_elem)
{
    int i;

    printf("%02d Elements are: ", num_elem);
    for (i = 0; i < num_elem; i++) {
        printf("%02d ", elems[i]);
    }
    printf("\n");
}

void build_min_heap(int *elems, int idx, int heap_size)
{
    int i, largest = idx, temp;

    if (LEFT(idx) < heap_size && elems[idx] < elems[LEFT(idx)]) {
        largest = LEFT(idx);
    }
    if (RIGHT(idx) < heap_size && elems[largest] < elems[RIGHT(idx)]) {
        largest = RIGHT(idx);
    }

    if (largest != idx) {
        temp = elems[idx];
        elems[idx] = elems[largest];
        elems[largest] = temp;

        build_min_heap(elems, largest, heap_size);
    }
}

void build_heap(int *elems, int num_elem, int heap_size)
{
    int i;

    for (i = num_elem/2; i >= 0; i--) {
        build_min_heap(elems, i, heap_size);
    }
    printf("after %s\n", __func__);
    print_arr_elem(elems, num_elem);
}

void heapsort(int *elems, int num_elem)
{
    int temp, i, heap_size = num_elem;

    build_heap(elems, num_elem, heap_size);

    for (i =0; i < num_elem; i++) {

        temp = elems[heap_size - 1];
        elems[heap_size - 1] = elems[0];
        elems[0] = temp;
        heap_size--;

        build_min_heap(elems, 0, heap_size);
    }
}

int main()
{
    int num_elems, i;
    int *elems;

    srand(time(NULL));

    num_elems = rand() % 15;
    printf("Number of elements to sort: %d\n", num_elems);
    printf("RAND_MAX: %x\n", RAND_MAX);

    for (i = 0; i < num_elems; i++) {
        // elems[i] = (rand() + rand()) % 25;
        // elems[i] = rand() % 25;
        printf("%d = %d\n", rand(), (rand() + rand()));
    }
    print_arr_elem(elems, num_elems);

    heapsort(elems, num_elems);

    print_arr_elem(elems, num_elems);
}

