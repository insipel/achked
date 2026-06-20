#include <stdio.h>
#include <stdlib.h>

void
print_array(int *a, int num_elems)
{
    int i = 0;

    if (num_elems <=0) {
        printf("Nothing to print in the array\n");
        return;
    }

    printf("Array[%d]: [ ", num_elems);
    for (; i < num_elems; i++) {
        printf("%02d, ", a[i]);
    }
    printf("]\n");

    return;
}

void
merge(int *a, int start, int p, int end)
{
    int i, j, k;
    // p or middle could be same as start. so if we had just 'p -
    // start' as the l_elems, then it'd mean that l_elems is 0 and
    // r_elem has all the elements. It wont be correct atleast for the
    // first merge case of 0, 0 and 1. l_elem would be 0 and r_elem as
    // 2 elements. It'd assume that r_elem in r are sorted but it is
    // not.
    int l_elems = p - start + 1;
    int r_elems = end - p;

    int l[l_elems];
    int r[r_elems];

    for (i = 0; i < l_elems; i++) {
        l[i] = a[start + i];
    }

    for (i = 0; i < r_elems; i++) {
        r[i] = a[p + 1 + i];
    }

    j = k = 0;
    i = start;
    while (j < l_elems && k < r_elems) {

        if (l[j] < r[k]) {
            a[i] = l[j];
            j++;
        } else {
            a[i] = r[k];
            k++;
        }

        i++;
    }

    // 'r' is exhaused
    if (j < l_elems) {

        for (; j < l_elems; j++, i++) {
            a[i] = l[j];
        }

    } else {
        // 'l' is exhaused
        for (; k < r_elems; k++, i++) {
            a[i] = r[k];
        }
    }

    // print_array(a+start, end + 1);
}

void
merge_sort(int *a, int start, int end)
{
    int p = -1;

    if (start < end) {
        p = (start + end) / 2;
        //printf("1.start:%d end:%d\n", start, p);
        merge_sort(a, start, p);
        //printf("2.start:%d end:%d\n", p+1, end);
        merge_sort(a, p+1, end);
        //printf("3.start:%d middle:%d end:%d\n", start, p, end);
        merge(a, start, p, end);
    }

    //printf("4. return start:%d middle:%d end:%d\n", start, p, end);
    return;
}

void
sort(int *a, int num_elems)
{
    if(!a) {
        printf("Invalid array\n");
        return;
    }

    if (num_elems <= 1) {
        printf("No sort needed\n");
        return;
    }

    //printf("0.start:%d end:%d\n", 0, num_elems -1 );
    merge_sort(a, 0, num_elems - 1);
    return;
}

void
main()
{
    int *a, i;
    int num_elems;

    srand(time(NULL));

    num_elems = rand() % 15;
    printf("Going to sort %d of elements\n", num_elems);

    a = (int *) malloc(num_elems * sizeof(int));
    if (!a) {
        printf("Out of memory condition\n");
        return;
    }

    for (i =0; i < num_elems; i++) {
        a[i] = rand() % 50;
    }

    print_array(a, num_elems);
    sort(a, num_elems);
    print_array(a, num_elems);
}
