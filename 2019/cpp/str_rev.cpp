#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

class StrData {
    private:
        string cString;

    public:
        StrData(string str);
        ~StrData();
        void printStr();
        char *reverseStr();

        /* copy constructor */
        StrData(const StrData &);
        /* overloaded constructor */
        StrData &operator=(const StrData &);
        string getString();
};

string
StrData::getString() {
    cout << __func__ << "returning : " << this->cString;
    return this->cString;
}

StrData::StrData(string str)
{
    int len =  sizeof(str);
    cout << __func__ << ": string is " << str << ". len: " << len << "." << endl;
    //this->cString = new char[len];
    this->cString = str;

    //cout << "allocated:  0x" << hex << reinterpret_cast<unsigned long>(this->cString) << endl;
}

StrData::StrData(const StrData &rhs)
{
    cout << __func__ << "in copy constru" << endl;
}

StrData &
StrData::operator=(const StrData &rhs)
{
    cout << __func__ << "in overload = operator" << endl;
}

StrData::~StrData()
{
    cout << __func__ << " :" << endl;
    //delete(this->cString);

    //cout << "Freed: 0x" << hex << reinterpret_cast<unsigned long>(this->cString)
    //     << ". " << endl;

    return;
}

void
StrData::printStr()
{
    cout << __func__ << ": String is: " << this->cString << ". " << endl;
}

char *
StrData::reverseStr()
{
    cout << __func__ << " :" << endl;
}

int main()
{
    // I could make new StrData(new char("Animesh Pathak")) to get rid
    // of const keyword in the constructor.
    StrData *strData = new StrData("Animesh Pathak");
    strData->printStr();

    StrData strData1("Animesh");
    StrData revStr("");
    revStr = strData1;
    // StrData *revStr = new StrData(strData->reverseStr());
    // revStr->printStr();
    cout << __func__ << "Reversed string: " << reverse<string>(revStr.getString());

    delete strData;
}

