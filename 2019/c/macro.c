/*
 * Macros:
 *      1. Stringification
 *      2. Token pasting OR Token concatenation
 *
 * Align/Round up   to a multiple of power of 2.
 * Align/Round down to a multiple of power of 2.
 *
 * Get the next power of 2 for a given integer.
 */
#include <stdio.h>

/*
 * When a macro parameter is used with a leading ‘#’, the preprocessor replaces it with the literal text of the actual argument, converted to a string constant. Unlike normal parameter replacement, the argument is not macro-expanded first. This is called stringification.
 */
#define cat(a, b...) (printf(#a"\ntemp\n", b))
#define cat1(a, b...) (printf(a"\ntemp\n"## b, b))

/*
 * The do and while (0) are a kludge to make it possible to write WARN_IF (arg);, which the resemblance of WARN_IF to a function would make C programmers want to do; see Swallowing the Semicolon.
 */
// The do-while style of Macro writing. with this approach, it can
// work in both "if (WARN_IF(arg))" and "WARN_IF(arg);" format.


/*
 * If you want to stringify the result of expansion of a macro argument, you have to use two levels of macros.
 *
 *   #define xstr(s) str(s)
     #define str(s) #s
     #define foo 4
     str (foo)
          ==> "foo"
     xstr (foo)
          ==> xstr (4)
          ==> str (4)
          ==> "4"
 */
#define xstr(s) str(s)
#define str(s) #s // STRINGIFICATION
#define foo 4

/*
It is often useful to merge two tokens into one while expanding macros. This is called token pasting or token concatenation. The ‘##’ preprocessing operator performs token pasting.
When a macro is expanded, the two tokens on either side of each ‘##’ operator are combined into a single token, which then replaces the ‘##’ and the two original tokens in the macro expansion. Usually both will be identifiers, or one will be an identifier and the other a preprocessing number. When pasted, they make a longer identifier.

This isn't the only valid case. It is also possible to concatenate two numbers (or a number and a name, such as 1.5 and e3) into a number. Also, multi-character operators such as += can be formed by token pasting.
 */
int quit_command()
{
    return(printf("%s\n", __func__));
}

int help_command()
{
    return(printf("%s\n", __func__));
}

struct command
{
    char *name;
    int (*function) (void);
};

struct command commands[] =
{
    { "quit", quit_command }, // this is giving quit, quit twice.
    { "help", help_command },
};
/*
It would be *cleaner* not to have to give each command name twice, once in the string constant and once in the function name. A macro which takes the name of a command as an argument can make this unnecessary. The string constant can be created with stringification, and the function name by concatenating the argument with ‘_command’. Here is how it is done: 
 */
#define COMMAND(NAME)  { #NAME, NAME ## _command }

struct command commands1[] =
{
    COMMAND (quit),
    COMMAND (help),
};

//#####################################

/* Round up x to the next multiple of y where y is a power of 2. */
#define ROUNDUP(x, y)            (((x) + ((y) - 1)) & ~((y) - 1))
#define ROUNDDOWN(x, y)          ((x) & ~((y) - 1))

/* Varants of ROUNDUP that preserve datatype */
#define ALIGN_UP(val, align)                              \
    ({                                                 \
        uint32_t _val = (uint32_t) (val);         \
        uint32_t _mask = (uint32_t) (align) - 1;  \
        (typeof (val)) ((_val + _mask) & ~_mask); \
    })
#define ALIGN_DOWN(val, align)                            \
    ({                                                 \
        uint32_t _val = (uint32_t) (val);         \
        uint32_t _mask = (uint32_t) (align) - 1;  \
        (typeof (val)) (_val & ~_mask);           \
    })
#define ALIGN_OFFSET(val, align)                          \
    ({                                                 \
        uint32_t _val = (uint32_t) (val);         \
        uint32_t _mask = (uint32_t) (align) - 1;  \
        (_val & _mask);                           \
    })


/*
 * roundup_to_next_power_of_two:
 *
 * It works for a 32-bit integer.
 *
 * Sets all bits right of the most significant set bit.
 * then adds 1 to that value to get the rounded up power of 2.
 */
static inline unsigned int
roundup_to_next_power_of_two (unsigned int x)
{
    /* If it is already a power of 2, prevents rounding up to next power of 2 */
    printf("\n\nx:%d\n", x);
    x--;
    printf("x--:0x%x\n", x);
    printf("x>>1:0x%x, (x| (x >>1)):0x%x\n", (x >> 1), (x | (x >> 1)));
    x |= x >> 1;    /* Make sure most significant 2 bits of x are set. */
    printf("x>>2:0x%x, (x| (x >>2)):0x%x\n", (x >> 2), (x | (x >> 2)));
    x |= x >> 2;    /* Make sure most significant 4 bits of x are set. */
    x |= x >> 4;    /* Make sure most significant 8 bits of x are set. */
    x |= x >> 8;    /* Make sure most significant 16 bits of x are set. */
    x |= x >> 16;   /* Make sure most significant 32 bits of x are set. */
    x++;            /* Round up to next power of 2. */
    printf("Final x:%d\n", x);
    return x;
}
//#####################################

void
test_int_abs_value_without_branching()
{
    int v = -5;
    unsigned int r;
    int const mask = v >> sizeof(int) * 8 /* CHAR_BIT */ - 1;

    printf("%d v:0x%08x mask:%d (v+mask):%x\n", __LINE__, v, mask, (v+mask));

    r = (v + mask) ^ mask;

    printf("abs(%d)=%d\n", v, r);
}

int main()
{

    cat("%d : macro:%s", 10, "cat");
//printf("%s", cat1("%d : macro:%s", 10, "cat1"));
    printf("str(foo):%s\n", str (foo));
    printf("xstr(foo):%s\n", xstr (foo));

    printf("quit: %s:%d\n", commands1[0].name, commands1[0].function());
    printf("help: %s:%d\n", commands1[1].name, commands1[1].function());

    srand(time(NULL));
    int num = rand() % 100;
    roundup_to_next_power_of_two(num);

    test_int_abs_value_without_branching();
}

