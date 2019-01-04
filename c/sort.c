#include <stdio.h>
//#include <math.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int temp = *a;

    *a = *b;
    *b = temp;
}

void
max_heapify(int *a, int i, int len)
{

    int orig_a = a[i];
    int changed_idx;

    printf("%s: max_heapify idx:%d len:%d\n", __func__, i, len);

    if (2*i < len && a[i] < a[2*i]) {
        printf("%s: swapping 2*i a[%d]:%d, a[%d]:%d, \n",
                __func__, i, a[i], 2*i, a[2*i]);
        swap(&a[i], &a[2*i]);
        printf("%s: swapped 2*i a[%d]:%d, a[%d]:%d, \n",
                __func__, i, a[i], 2*i, a[2*i]);
        changed_idx = 2*i;
    }

    if ((2*i + 1) < len && a[i] < a[(2*i + 1)]) {
        printf("%s: swapping 2*i+1 a[%d]:%d, a[%d]:%d, \n",
                __func__, i, a[i], 2*i+1, a[2*i+1]);
        swap(&a[i], &a[2*i+1]);
        printf("%s: swapped 2*i+1 a[%d]:%d, a[%d]:%d, \n",
                __func__, i, a[i], 2*i+1, a[2*i+1]);
        changed_idx = 2*i + 1;
    }

    if(i != changed_idx) {
        printf("%s: max_heapify again: new idx:%d\n", __func__, changed_idx);
        max_heapify(a, changed_idx, len);
    }

}

void build_max_heap(int *a, int len)
{
    int i;

    for (i = len/2; i > 0; i--) {
        printf("%s: i:%d\n", __func__, i-1);
        max_heapify(a, i-1, len);
    }
}

void heapsort(int *a, int len)
{
    // int a[] = {12, 4, 7, 65, 43, 88, 32, 21, 34, 9, 17, 98};
    int orig_len;

    orig_len = len;
    build_max_heap(a, len);
    printf("%s: done with build_max_heap \n", __func__);
    len = orig_len;
    while (len--)
        printf("a[%d]:%d, ", len+1, a[len]);

    len = orig_len;
    while (len > 0) {

        printf("%s: a0:%d, a_[len-1]%d, \n", __func__, a[0], a[len-1]);
        swap(&a[0], &a[len-1]);
        printf("Got %d-th eleme: %d\n", len, a[len-1]);
        max_heapify(a, 0, len-1);
        len--;
    }

    len = orig_len;
    while (len--)
        printf("a[%d]:%d, ", len+1, a[len]);

}

int
partition(int *a, int start, int end)
{
    int i = start -1, j =  start;

    while (j < end-1) {

        if (a[j]  < a[end-1]) {
            i++;
            swap(&a[i], &a[j]);
        }

        j++;
    }

    swap(&a[i+1], &a[end-1]);

    return i+1;
}

void quicksort(int *a, int start, int end)
{
    int i = 0, j;

    if (start < end) {
        i = partition(a, start, end);

        j =start;
        quicksort(a, start, i-1);
        quicksort(a, i+1, end);
    }

}

void merge(int *a, int start, int midl, int end)
{
    int n1 = midl - start + 1;
    int n2 = end - midl;
    int l[n1+1], r[n2+1];
    int i, j, k;

    for (i = 0; i < n1; i++) {
        l[i] = a[start + i];
    }
    l[i] = 0xFFFFFFFF;
    for (i = 0; i < n2; i++) {
        r[i] = a[midl + i + 1];
    }
    r[i] = 0xFFFFFFFF;

    i = j = 0;
    k = start;
    while (k < end) {

        if (l[i] <= r[j]) {
            a[k] = l[i++];
        } else {
            a[k] = r[j++];
        }

        k++;
    }

}

void mergesort(int *a, int start, int end)
{
    int i;

    if (start < end) {
        i = (start+end)/2;
        mergesort(a, start, i);
        mergesort(a, i+1, end);
        merge(a, start, i, end);
    }
}

void
rand_input()
{
    int *a;
    int len;
    int i = 0;

    srand(time(NULL));
    while (1) {
        len = rand()%21;
        printf("len:%d ", len);
        if (len > 10 && len < 20)
            break;
    }

    a = (int *) malloc(len);
    if (!a) {
        printf("OOM Error!!!\n");
        return;
    }

    for (i = 0; i < len; i++) {
        a[i] = rand()%100;
    }
    i =0;
    printf("\nInput Array:\n");
    while (i < len) {
        printf("%d ", a[i]);
        i++;
    }

    // heapsort(a, sizeof(a)/sizeof(int));
    quicksort(a, 0, len);

    printf("\nOutput Array:\n");
    i =0;
    while (i < len) {
        printf("%d, ", a[i]);
        i++;
    }
}

void
static_input()
{
    int a[] = {84, 84, 14, 74, 15, 84, 9, 41, 74, 85, 79, 24, 0, 71, 34, 30, 14, 4, 99};
    int len = sizeof(a)/sizeof(int);
    int i = 0;

    i =0;
    printf("\nStatic Input Array:\n");
    while (i < len) {
        printf("%d ", a[i]);
        i++;
    }

    // heapsort(a, sizeof(a)/sizeof(int));
    quicksort(a, 0, len - 1);

    printf("\nOutput Array:\n");
    i =0;
    while (i < len) {
        printf("%d, ", a[i]);
        i++;
    }
}

int main()
{
    static_input();
}

