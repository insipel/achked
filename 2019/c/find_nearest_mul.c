#include <stdio.h>

int main()
{
    unsigned int a[] = {17, 4, 9, 42, 78, 82, 72};
    int size = sizeof(a)/sizeof(unsigned int);
    unsigned int a1[size];
    unsigned int pt = 16;

    int i = 0, n, n1;
    for (i = 0; i < size; i++) {
        n = a[i];
        n1 = ((n & (pt - 1)) > (pt >> 1));
        a1[i] = (n & ~(pt - 1)) | ((pt & (n1 ? -1 : 0)));
        printf("a[%d]: %d -> a1[%d]: %d\n", i, a[i], i, a1[i]);
    }

    return;
}
