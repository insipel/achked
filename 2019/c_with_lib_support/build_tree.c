#include <stdio.h>
#include <stdlib.h>

typedef unsigned char  uint8_t;
typedef unsigned short uint16_t;
typedef unsigned int   uint32_t;

typedef struct _node {
    
    uint32_t     data;
    struct _node *left;
    struct _node *right;

} node;

void
insert_elem(node **root, uint32_t data)
{
    node *curNode, *tempRoot, *prev;

    curNode = (node *) malloc(sizeof(node));
    curNode->data = data;
    curNode->left = NULL;
    curNode->right = NULL;

    if (*root == NULL) {
        *root = curNode;
        return;
    }

    tempRoot = *root;
    while (tempRoot) {

        prev = tempRoot;
        if (tempRoot->data > data) {

            tempRoot = tempRoot->left;

        } else if (tempRoot->data < data) {

            tempRoot = tempRoot->right;

        } else {
            printf("\nNew Data: %d already in the tree\n", data);
            return;
        }
    }

    if (prev->data > data) {
        prev->left = curNode;
    } else {
        prev->right = curNode;
    }

    return;
}

void print_tree(node *root)
{
    if (!root)
        return;

    print_tree(root->left);
    printf("%d ", root->data);
    print_tree(root->right);
    return;
}

int main ()
{
    srand(time(NULL));

    int num_nodes = rand() % 20;
    node *root = NULL;
    uint32_t data, i;

    printf("\nTotal elements in the tree are: %d\n", num_nodes);
    for (i = 0; i < num_nodes; i++) {

        data = rand() % 60;
        printf("%d ", data);
        insert_elem(&root, data);
    }

    printf("\n Tree data:\n");
    print_tree(root);
}

