#include <stdio.h>
#include <stdlib.h>

void print_int_arr(int *elems, int num)
{
    int i;

    printf("%02d Elements are: ", num);
    for (i =0; i < num; i++) {
        printf ("%02d ", elems[i]);
    }

    printf("\n");
}

int partition(int *elems, int start, int end)
{
    int i, j, k, temp_elem, key;
    i = start -1;
    j = start;
    k = end;
    key = elems[end];

    while (j < end) {
        if (elems[j] < key) {
            i += 1;
            temp_elem = elems[i];
            elems[i] = elems[j];
            elems[j] = temp_elem;
        }
        j++;
    }

    i = i+1;
    temp_elem = elems[i];
    elems[i] = key;
    elems[end] = temp_elem;

    return i;
}

void qsort1(int *elems, int start, int end)
{
    int q;

    if (start < end) {
        q = partition(elems, start, end);
        qsort1(elems, start, q -1);
        qsort1(elems, q +1, end);
    }
}

int main()
{
    int *elems, num_elems, i;

    srand(time(NULL));

    num_elems = rand() % 15;
    printf("num_elems:%d\n", num_elems);
    elems = (int *) malloc(sizeof(unsigned int) * num_elems);
    for (i = 0; i < num_elems; i++) {
        elems[i] = rand() % 30;
    }

    print_int_arr(elems, num_elems);


    /*
     * Start the merge sort.
     */
    qsort1(elems, 0, num_elems - 1);
    print_int_arr(elems, num_elems);

}

