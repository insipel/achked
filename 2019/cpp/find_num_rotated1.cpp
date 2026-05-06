#include <iostream>

using namespace std;

int reset_point(int a[], int sz)
{
    if (sz == 1) return 0;

    int start = 0, end = sz -1, m;
    while (start < end - 1) {
        m = (start + end)/2;

        if (a[m] < a[end]) {
            end = m;
        } else {
            start = m;
        }
    }

    if ((end - start) == 1) {
        return (a[end]>a[start]? start : end);
    } else {
        return -1;
    }
}

/*
 * Idea is to find the reset point first. Look at the function above.
 *
 * Then use the reset point as start index (as expected). Run the
 * start(p) and end(r) as you would run on a regular unsorted array.
 * This would simplify the range selection in which to look. But when
 * you are comparing the numbers in the range, use the adjusted index using
 * reset_point.
 */
int find_num(int a[], int sz, int num)
{
    if (!a || !sz) return -1;
    int start_idx = reset_point(a, sz);

    int p = 0, r = sz -1, m, m1;

    /*
     * Run the loop till start is 1 less than end. This would help to
     * avoid the infinite loop when start and end is adjacent to each
     * other. middle index will be equal to start. So if we end up
     * assigning 'm' to 'start', then it would result in same 'start'
     * value as the previous iteration and thus an endless loop.
     *
     * So the idea is to terminate the loop when 'start' is adjacent
     * to 'end'.
     */
    while ( p <= r) {
        m = (p + r)/2;

        m1 = (m + start_idx)%sz;
        if (a[m1] == num) {
            return m1;
        } else if (a[m1] < num) {
            p = m+1;
        } else /* if (a[m1] > num) */ {
            r = m-1;
        }
    }

    return -1;
}

typedef struct _input {
    int a[100];
    int sz;
    int num;
} input;

int main()
{
    input ip[] = {
                 {{1}, 1, 1},
                 {{1, 2}, 2, 1},
                 {{1, 2}, 2, 99},
                 {{1, 2}, 2, 2},
                 {{2, 1}, 2, 1},
                 {{2, 1}, 2, 2},
                 {{2, 1}, 2, 4},
                 {{3, 2, 1}, 3, 3},
                 {{3, 2, 1}, 3, 4},
                 {{3, 1, 2}, 3, 1},
                 {{3, 4, 99, 100, 1, 2}, 5, 6},
                 {{3, 4, 99, 100, 1, 2}, 5, 99},
                 {{3, 4, 99, 100, 1, 2}, 5, 1},
                 {{3, 14, 32, 67, 68, 99, 100, 1, 2}, 9, 6},
                 {{3, 14, 32, 67, 68, 99, 100, 1, 2}, 9, 32},
                 {{3, 14, 32, 67, 68, 99, 100, 1, 2}, 9, 100},
                 {{14, 32, 67, 68, 99, 100, 1, 2, 6, 9, 10}, 11, 6},
                 {{14, 32, 67, 68, 99, 100, 1, 2, 6, 9, 10}, 11, 14},
                 {{14, 32, 67, 68, 99, 100, 1, 2, 6, 9, 10}, 11, 10},
                 {{3, 4, 32, 45, 67, 68, 99, 100, 1, 2}, 10, 6},
                 {{3, 4, 32, 45, 67, 68, 99, 100, 1, 2}, 10, 3},
                 {{3, 4, 32, 45, 67, 68, 99, 100, 1, 2}, 10, 100},
                };

    for (int i = 0; i < sizeof(ip)/sizeof(input); i++) {

        cout << "input#:" << i+1 << " { [";
        for (int j = 0; j < ip[i].sz; j++) {
            cout << ip[i].a[j] << ", ";
        }
        cout << "], " << ip[i].sz << ", " << ip[i].num << "}. Reset point: ";

        cout << reset_point(ip[i].a, ip[i].sz) << endl;
        cout << "Number's index: " << find_num(ip[i].a, ip[i].sz, ip[i].num) << endl;
    }
}

