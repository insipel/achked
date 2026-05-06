#include <iostream>

template <typename T>
class basic1 {

    public:
        basic1(int size);
        ~basic1();
        // print_elems();

    private:
        T *data;
        int size;
};

template <typename T>
basic1<T>::basic1(int size)
{
    this->data = NULL;
    this->size = size;
    std::cout << __func__ << "constructor size:" << size << std::endl;
}

template <typename T>
basic1<T>::~basic1()
{
    if (this->data) {
        delete data;
    }
}

int main()
{
    basic1<int> i(15);
}

