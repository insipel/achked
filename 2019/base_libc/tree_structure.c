#include <stdio.h>
#include "../practice_hdr.h"
#include "../eanimpa/build_tree_lib.h"

uint8_t
compare_tree_structure(node *node1, node *node2)
{
    if (!node1 && !node2) {
        printd("Both nodes are null\n");
        return 1;
    }

    if ((node1 && !node2) || (!node1 && node2)) {
        printd("node1:%p node2:%p\n", node1, node2);
        return 0;
    }

    printd("Node1 data:%d, node2 data:%d\n", node1->data, node2->data);
    return(compare_tree_structure(node1->left, node2->left) &&
           compare_tree_structure(node1->right, node2->right));
}

int main()
{
    node *tree1 = build_tree_data(4, 4, 6, 23, 10);
    node *tree2 = build_tree_data(4, 0, 12, 31, 30);

    printf("\n");
    if (compare_tree_structure(tree1, tree2)) {
        printf("Same structure\n");
    } else {
        printf("NOT Same structure\n");
    }
}
