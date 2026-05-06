#include <stdio.h>

int main()
{
    char s[10];

    printf("&s is:0x%p\n", s);;

    char *s1 = s+1;
    printf("&s is:0x%p\n", s1);;
}

