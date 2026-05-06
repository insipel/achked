#include <stdio.h>

// #define DEBUG_ON
#ifdef DEBUG_ON
#define DEBUG_PRINT(format,...) printf(format, ## __VA_ARGS__);
#else
#define DEBUG_PRINT(format,...)
#endif

#define SUBSET_LENGTH 4
// #define SUBSET_LENGTH 3
// #define SUBSET_LENGTH 5

void generateSubset(int array[], int subset[], int used[], int length, int index, int lastoffset)
{
    int k;

    if (index == length)
    {
        // printf("subset %d%d%d\n", subset[0], subset[1], subset[2]);
        // printf("subset %d%d%d%d%d\n", subset[0], subset[1], subset[2],
        //         subset[3], subset[4]);
        printf("subset %d%d%d%d\n", subset[0], subset[1], subset[2], subset[3]);
        //DEBUG_PRINT("subset %d%d%d%d\n", subset[0], subset[1], subset[2], subset[3]);
        DEBUG_PRINT("======================\n\n");
        return;
    }

    for (k = 0; k < length; k++)
    {
        DEBUG_PRINT("k:%d used[%d]:%d\n", k, k, used[k]);
        if (used[k]) continue;

        // if (k < lastoffset) continue;
        subset[index] = array[k];
        used[k] = 1;

        DEBUG_PRINT("Before recursion k:%d index:%d used[%d]:%d array[%d]:%d\n",
                k, index, k, used[k], k, array[k]);
        generateSubset(array, subset, used, length, index + 1, k);

        used[k] = 0;
        DEBUG_PRINT("After recursion k:%d index:%d used[%d]:%d\n",
                k, index, k, used[k]);
    }
}

int main()
{
    int array[4] = {1, 2, 3, 4};
    // int array[3] = {1, 2, 3};
    // int array[5] = {1, 2, 3, 4, 5};
    int used[4] = {0, 0, 0, 0};
    // int used[3] = {0, 0, 0};
    // int used[5] = {0, 0, 0, 0, 0};
    int subset[SUBSET_LENGTH];

    memset((void *)used, 0, sizeof(array)/sizeof(int));
    memset((void *)subset, 0, SUBSET_LENGTH);

    generateSubset(array, subset, used, sizeof(array)/sizeof(int), 0, 0);

    return 0;
}


