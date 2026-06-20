#include <stdio.h>
#include "build_tree_lib.h"

#define level_10 "  "
#define level_9  level_10"  "
#define level_8  level_9"  "
#define level_7  level_8"  "
#define level_6  level_7"  "
#define level_5  level_6"  "
#define level_4  level_5"  "
#define level_3  level_4"  "
#define level_2  level_3"  "
#define level_1  level_2"  "
#define level_0  level_1"  "
#define level_printf(i) printf(".%s.\n", level_ # i);

char *level_space[] =
    {
        "                      ",
        "                  ",
        "                ",
        "              ",
        "            ",
        "          ",
        "        ",
        "      ",
        "    ",
        "  ",
        " ",
    };

uint32_t
tree_height(node *root, uint32_t h)
{
    static height = 0;

    if (!root) return height;

    tree_height(root->left, h+1);

    if (h >= height)
        height++;

    tree_height(root->right, h+1);
}

void
print_tree_regular(node *root, node *level_list[], uint32_t height)
{
    uint32_t i;
    node *tmp_node;

    // <= as height is 0 based.
    for (i = 0; i <=height; i++) {

        tmp_node = level_list[i];
        if (tmp_node == NULL) break;

        printf("Level-%d: ", i);
        while(tmp_node) {
            printf("%02d  ", tmp_node->data);
            tmp_node = tmp_node->right;
        }

        printf("\n");
    }

}

void
build_tree_list(node *root, node *level_list[], uint32_t h)
{
    if (!root) return;

    build_tree_list(root->left, level_list, h+1);
    build_tree_list(root->right, level_list, h+1);

    printf("data:%d height(1-based):%d\n", root->data, h+1);

    /*
     * Now, put the tree nodes into the list.
     */
    // node *next = level_list[h]->right;
    node *next = level_list[h];
    printf("next:%p\n", next);

    if (next) {

        printf("next:%p: %d curdata:%d\n", next, next->data, root->data);
        next = level_list[h]->right;
        level_list[h]->right = root;
        root->left = level_list[h];
        root->right = next;

    } else {

        printf("null next:%p: %d\n", root, root->data);
        level_list[h] = root;
        root->right = NULL;
    }
}

int main()
{
    uint32_t i = 0;
    node *root, **level_list;

    root = build_tree();

    // Print tree level wise
    // Modify the trees
    
    uint32_t height = tree_height(root, 0);

    printf("\nHeight(1-based):%d root:%d\n", height+1, root->data);

    // level_list = (node **) calloc(sizeof(node *) * height, 0x0);
    // calloc didn't nullify the 3rd element. don't know why.
    level_list = (node **) calloc(sizeof(node *) * height, 0x0);
    for (i = 0; i < height; i++) {
        level_list[i] = 0;
        printf("%p ", level_list[i]);
    }
    printf("\n");

    build_tree_list(root, level_list, 0);
    print_tree_regular(root, level_list, height);

}

