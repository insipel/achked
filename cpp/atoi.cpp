#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

void atoi()
{
    string s = "3465212.01";

    int num =0, base = 10, i, len = s.length();
    float fnum = 0, s1, pos = 1;

    cout << "string is: " << s << ". len: " << len << endl;
    for (i = 0; i < len; i++) {

        if (__builtin_expect((s[i] != '.'), 1)) {
            num = (num * base) + (s[i] - '0');
            cout << "num: " << num << endl;
        } else {

            /*
             * going past the decimal char.
             */
            i++;
            break;
        }
    }

    /*
     * if here, either the string has been converted full or we hit a
     * decimal char.
     */
    cout << "i: " << i << endl;
    for (; i < len; i++) {
        
        pos = pos * base;
        s1 = s[i] - '0';

        /*
         * if here, then we need to process the decimal part.
         */
        fnum = fnum + (s1 /pos);

        cout << "fnum: " << fnum
             << " s[i]: " << (s[i] - '0')
             << " pos: " << pos << endl;
    }

    cout << "final number: " << (num + fnum) << endl;
}

int main()
{
    atoi();
}

