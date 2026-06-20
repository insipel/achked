/*
 * Find a number in sorted array.
 */
#include <stdio.h>

int my_comp(const void *n1, const void *n2)
{
    int num1 = *((int *)n1);
    int num2 = *((int *)n2);

    return ( num1 - num2);
}

int find_num(int *a, int size, int num)
{
    if (!a || !size)
        return -1;

    int start, end, index;
    start  = 0;
    end = size - 1;

    while (start <= end) {  // = is needed to compare the case when start and end point to the same element. and that would be the end case.

        index = (start+end)/2;
        if (a[index] == num) {
            return index;
        } else if (a[index] < num) {
            start = index + 1;
        } else {
            end = index - 1;
        }
    }

#ifdef temp
    // earlier approach. it's incorrect. it would search but the
    // terminal condition would exit the loop wrongly.
    int index = size/2;
    int step = index/2;

    while(1) {
        if (a[index] == num) {
            return index;
        } else if (a[index] < num) {
            index = index + step;
        } else {
            index = index - step;
        }

        step = step/2;
        if (step == 0) {
            return -1;
        }
    }
#endif

    printf ("dead code\n");
    return -1;
}

int main()
{
    int *a;

    srand(time(NULL));

    int size = generate_array(&a, 20);
    //print_array_elems(a, size);

    qsort(a, size, sizeof(int), &my_comp);
    print_array_elems(a, size);
    if (!size) return;
    int idx = rand() % (size * 2);
    int element = a[idx];
    int index = find_num(a, size, element);
    printf ("number %d found at index:%d\n", element, index);
}

