#include <stdio.h>

int num1s(int n) {
    int count = 0;
    
    while (n) {
        if (n%10 == 1) {
            count++;
        }
        
        n = n/10;
    }
    
    return count;

}

int countDigitOne(int n) {
    int count = 0, pass = 0;
    
    while (n > 0) {
        count += num1s(n);
        n--;
    }
    
    return count;
}

int main() {
    printf("Number of 1s: %d\n", countDigitOne(100));
}
