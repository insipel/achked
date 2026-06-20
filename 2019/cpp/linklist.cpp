#include <iostream>
#include <cstdio>

using namespace std;

class Node {
    public:
        int data;
        Node *next;

        Node(int);
        ~Node();
};

Node::Node(int data) {
    this->data = data;
    this->next = NULL;

    cout << "function:" << __FUNCTION__ <<endl;
    printf("%s: data :%d \n", __func__, this->data);
};

Node::~Node() {
    cout << __func__ << "called." << endl;
}

class LinkList {
    private:
        Node *head;
    public:
        LinkList();
        ~LinkList();
        void addNode(int);
        void printList();
};

LinkList::LinkList() {
    cout << __func__ << "initing head to null" << endl;
    this->head = NULL;
}

LinkList::~LinkList() {
    cout << __func__ << "deleting the list" << endl;
}

void LinkList::addNode(int data) {
    cout << __func__ << "adding a new node" << data << endl;
    Node *node = new Node(data);
    Node *h = head;

    if (!head) {
        head = node;
    } else {

        while (h->next) {
            h= h->next;
        }

        h->next = node;
    }

    return;
}

void LinkList::printList() {
    Node *h = head;

    while(h) {
        cout << __func__ << ": data: " << h->data << "address: 0x" << std::hex << reinterpret_cast<unsigned long>(h) << endl;
        h = h->next;
    }

    return;
}

int main()
{
    Node *node = new Node(5);
    delete node;

    LinkList list;
    list.addNode(5);
    list.addNode(98);
    list.addNode(43);
    list.printList();
}

