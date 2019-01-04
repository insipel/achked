#include <stdio.h>
#include <stdlib.h>

void
print_array_elems(int *a, int num_elems)
{
    int i;

    if (!a || num_elems <= 0) {
        printf("No elements in the array\n");
        return;
    }

    printf("%02d Elements are: [ ", num_elems);
    for( i = 0; i < num_elems - 1; i++) {
        printf("%02d, ", a[i]);
    }
    printf("%02d ]\n", a[num_elems - 1]);
    return;
}

int
generate_array(int **arr, int max_elems)
{
    int i, *a, num_elems;

    if (max_elems < 0 || max_elems > 100) {
        max_elems = 20;
    }

    srand(time(NULL));

    num_elems = rand() % max_elems;
    printf("Generating %02d elements\n", num_elems);

    a = (int *) malloc(sizeof(int) * num_elems);
    if (!a) {
        printf("Error: OOM condition\n");
        return 0;
    }

    for (i = 0; i < num_elems; i++) {
        a[i] = rand() % 100;
    }

    print_array_elems(a, num_elems);

    *arr = a;
    return num_elems;
}

#if 0
int main()
{
    generate_array(30);
}
#endif
