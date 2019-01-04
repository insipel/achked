#include <stdio.h>
#include "../practice_hdr.h"
#include "../eanimpa/build_tree_lib.h"

void
get_tree_height(node *node, int *height, int cur_height)
{
    if (!node) {

        if (*height < cur_height)
            *height = cur_height;

        printd("node is null\n");
        return;
    }

    cur_height++;
    get_tree_height(node->left, height, cur_height);
    get_tree_height(node->right, height, cur_height);
    cur_height--;
}

int main()
{
    node *tree1 = build_tree(0);
    int height = 0;

    get_tree_height(tree1, &height, 0);
    printf("\n Height: %d\n", height);
}
