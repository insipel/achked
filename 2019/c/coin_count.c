#include <stdio.h>

#define DEBUG_PRINT
#ifdef DEBUG_PRINT
#define PRINT_FUNC(format,...) printf(format, ## __VA_ARGS__);
#else
#define PRINT_FUNC(format,...) 
#endif

int coin_set[100];

int
orig_coin_counting(int coins[], int num_coins, int sum, int idx)
{
    //PRINT_FUNC("idx:%d num_coins:%d sum:%d\n", idx, num_coins, sum);

    if (sum == 0) {
        //PRINT_FUNC("number of coins:%d\n", idx);
        return 1;
    }

    if (num_coins <= 0 && sum > 0)
        return 0;

    if (sum < 0)
        return 0;

    return( coin_counting(coins, num_coins - 1, sum, idx + 1) +
            coin_counting(coins, num_coins,
                          (sum - coins[num_coins - 1]), idx + 1));
}

int
coin_counting(int coins[], int num_coins, int sum, int idx)
{
    //PRINT_FUNC("idx:%d num_coins:%d sum:%d\n", idx, num_coins, sum);
    static int x = 0;

    if (sum == 0) {
        PRINT_FUNC("number of coins:%d\n", idx);
        return 1;
    }

    if (num_coins <= 0 && sum > 0)
        return 0;

    if (sum < 0)
        return 0;

    x += coin_counting(coins, num_coins - 1, sum, idx + 1);
    //PRINT_FUNC("Excluding coins:%d\n", x);
    x += coin_counting(coins, num_coins,
                          (sum - coins[num_coins - 1]), idx + 1);
    //PRINT_FUNC("including coins:%d\n", x);

    return (x);
#if 0
    return( coin_counting(coins, num_coins - 1, sum, idx + 1) +
            coin_counting(coins, num_coins,
                          (sum - coins[num_coins - 1]), idx + 1));
#endif

}

int
main()
{
    unsigned int sum;
    unsigned int coins[]= {10, 3, 5, 8};
    unsigned int num_coins;

    srand(time(NULL));
    sum = rand()%30;
    while(!(num_coins = rand()%4));

    PRINT_FUNC("sum:%d num_coins:%d\n", sum, num_coins);

    PRINT_FUNC("ORIG: number of ways: %d\n", orig_coin_counting(coins, num_coins, sum, 1));
    PRINT_FUNC("number of ways: %d\n", coin_counting(coins, num_coins, sum, 1));
}
