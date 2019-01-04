#include <iostream>

using namespace std;

class first {
    private:
        int static_int;

    public:
        first(int);
        ~first();
        int get_static_int();
};

first::first(int param)
{
    cout << "in " << __func__ <<endl;
    this->static_int = param;
}

first::~first()
{
    cout << "in " << __func__ <<endl;
    this->static_int = 0xFF;
}

int first::get_static_int()
{
    cout << "in " << __func__ <<endl;
    return(this->static_int);
}

int main()
{
    first first_var(0xdeadbeef);

    cout << "This is hello world" << endl;
    std::cout<< "get first int: 0x" << hex << first_var.get_static_int() << endl;
}
