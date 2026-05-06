#include <stdio.h>
#include <stdlib.h>

/*
 * out params:
 *  1. array pointer
 * in param:
 *  1. max number of elems in the list
 */
extern int generate_array(int **, int);

int
partition(int *a, int start, int end)
{
    int i, j, k, key, temp;

    i = start - 1;
    j = start;

    key = a[end];

    while (j < end) {
        if (a[j] < key) {
            i = i + 1;
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }

        j += 1;
    }

    if (end != i + 1) {
        temp = a[i+1];
        a[i+1] = a[end];
        a[end] = temp;
    }

    return (i+1);
}

void
quick_sort(int *a, int start, int end)
{
    int p;

    if (start < end) {
        p = partition(a, start, end);
        quick_sort(a, start, p - 1);
        quick_sort(a, p + 1, end);
    }
}

int main()
{
    int *a = NULL;
    int num_elems = generate_array(&a, 20 /* max #elems */);

    /*
     * Ideally it should be in the library, but just a bit lazy to
     * change it for now. So generating the list till I get non-0
     * number of elements in the list.
     */
    while (!num_elems) {
        printf("try again\n");
        num_elems = generate_array(&a, 20 /* max #elems */);
    }

    quick_sort(a, 0, num_elems - 1);
    print_array_elems(a, num_elems);
}

