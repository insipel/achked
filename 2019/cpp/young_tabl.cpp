#include <iostream>
#include <iomanip>
using namespace std;

class young_tbl {
    private:
        int **tbl;
        int size;

    public:
        young_tbl(int n = 3); //default size is 3x3
        ~young_tbl();
        void generate();
        void print();
        int  search(int num);
};

young_tbl::young_tbl(int n)
{
    size = n;
    tbl = new int*[n];
    for (int i = 0; i < size; i++) {
        tbl[i] = new int[size];
    }

    cout << "Allocated " << n << " * " << n << " elements." << endl;
}

young_tbl::~young_tbl()
{
    for (int i = 0; i < size; i++) {
        delete[] tbl[i];
    }

    delete[] tbl;
    cout << "Freed the table" << endl;
}

void
young_tbl::generate()
{
    int i, j;
    cout << "Generate the Young Tableau" << endl;

    int n = 23;

    for (i =0; i < size; i++) {
        for (j = 0; j < size; j++) {
            this->tbl[i][j] = n++;
        }
    }
}

void
young_tbl::print()
{
    int i, j;

    cout << "Print the Young Tableau" << endl;

    for (i =0; i < size; i++) {
        for (j = 0; j < size; j++) {
            cout << setw(3) << this->tbl[i][j] << " ";
        }

        cout << endl;
    }
}

int
young_tbl::search(int num)
{
    int i, j;

    if (num < this->tbl[0][0] || num > this->tbl[size-1][size-1]) {
        cout << "Didn't Find " << num << endl;
        return -1;
    }

    i = size - 1;
    j = 0;

    while ( i >= 0 && j < size) {
        if (num == this->tbl[i][j]) {
            cout << "Found " << num << " at [" << i << "][" << j << "]" << endl;
            return i;
        }

        if (num < this->tbl[i][j]) {
            i--;
        } else {
            j++;
        }
    }

    cout << "Didn't Find " << num << endl;
    return -1;
}

int main()
{
    young_tbl *tbl = new young_tbl(5);
    tbl->generate();
    tbl->print();
    tbl->search(42);

    delete tbl;

}

