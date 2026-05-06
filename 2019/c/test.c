#include <stdio.h>

typedef struct _a {
    short a1:13         __attribute__((packed));
    unsigned int a2_0:32  __attribute__((packed));
} a;

int get() {
    static int x;

    return ++x;
}

int strPrint()
{
    char const *c = "12345";
    int i = 0x01020304;
    char *p_i = (char *)&i;

    printf("*c %d \n", *c);
    printf("*i %d \n", *p_i);
}

int bit_test() {

    unsigned char b=0x02; // reverse this byte

    printf ("orig b:0x%x\n", b);

    printf (" (b * 0x80200802ULL):0x%x\n", (b * 0x80200802ULL));
    printf (" & 0x0884422110ULL:0x%x\n", ((b * 0x80200802ULL)& 0x0884422110ULL));

    b = ((b * 0x80200802ULL) & 0x0884422110ULL) * 0x0101010101ULL >> 32;

    printf ("reversed b:0x%x\n", b);
}

int main ()
{
    int i = 0, id;
    a new_a;

    id = 4;

    switch (id) {
        case 1:
    // printf("i is: %d, %d, %d \n", i++, i++, i++);
    new_a.a1=0x1ff;
    new_a.a2_0=0xf1e2d3c4;
    // new_a.a2_1=0x1f;
    // new_a.a2_2=0x1c;
    // new_a.a2_3=0x1d;
    // new_a.a3=0xe;
    printf("size of a is: %d\n", sizeof(new_a));
        break;

        case 2:
        printf("%d %d %d \n", get(), get(), get());
        break;

        case 3:
        strPrint();
        break;

        case 4:
        bit_test();
        break;
    }
}

