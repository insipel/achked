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


void merge(int *elems, int start, int middle, int end)
{
    int l1_size = middle - start + 1;
    int l2_size = end - middle;
    int l1 [l1_size];
    int l2 [l2_size];
    int i, j, k;

    for (i = 0; i < l1_size; i++) {
        l1[i] = elems[start + i];
    }
    for (i = 0; i < l2_size; i++) {
        l2[i] = elems[middle + i + 1];
    }

    i =0; j =0, k = start;
    while (i < l1_size && j < l2_size) {

        if ((l1[i] < l2[j])) {
            elems[k++] = l1[i++];
        } else if (l2[j] <= l1[i]) {
            elems[k++] = l2[j++];
        }
    }

    if (i < l1_size) {
        for (; i < l1_size; i++, k++) {
            elems[k] = l1[i];
        }
    } else if (j < l2_size) {
        for (; j < l2_size; j++, k++) {
            elems[k] = l2[j];
        }
    }

}

void merge_sort(int *elems, int start, int end)
{
    int middle;

    if (start < end) {
        middle = (start + end) /2 ;
        merge_sort(elems, start, middle);
        merge_sort(elems, middle+1, end);
        merge(elems, start, middle, end);
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
    merge_sort(elems, 0, num_elems - 1);
    print_int_arr(elems, num_elems);

}

