#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "build_tree_lib.h"

void
insert_elem(node **root, uint32_t data)
{
    node *curNode, *tempRoot, *prev;

    curNode = (node *) malloc(sizeof(node));
    curNode->data = data;
    curNode->parent = NULL;
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
    curNode->parent = prev;

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

node* build_tree (int max_elems)
{
    srand(time(NULL));

    if (max_elems <= 0) {
        return NULL;
    }

    int num_nodes = rand() % max_elems;
    uint32_t data, i;
    node *root = NULL;

    while(!num_nodes)
        num_nodes = rand() % max_elems;

    printf("\nTotal elements in the tree are: %d\n", num_nodes);
    for (i = 0; i < num_nodes; i++) {

        data = rand() % 60;
        printf("%d ", data);
        insert_elem(&root, data);
    }

    printf("\n Tree data:\n");
    print_tree(root);
    return root;
}

node* build_tree_data (int num_elems,...)
{
    int num_nodes = num_elems;
    uint32_t data, i;
    node *root = NULL;
    va_list ap;

    va_start(ap, num_elems);

    if (!num_elems) {
        printf("Return! invalid num_elems: %d\n", num_elems);
        return;
    }

    printf("\nTotal elements in the tree are: %d\n", num_elems);
    for (i = 0; i < num_elems; i++) {

        data = va_arg(ap, int);
        printf("%d ", data);
        insert_elem(&root, data);
    }

    va_end(ap);

    printf("\n Tree data:\n");
    print_tree(root);
    return root;
}

