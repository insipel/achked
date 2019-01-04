#include <stdio.h>

#define ROUNDDOWN(x, y)          ((x) & ~((y) - 1))

int main()
{
    printf("rounddown:%d\n", ROUNDDOWN((1500) - (14 + 20), 8));
}

