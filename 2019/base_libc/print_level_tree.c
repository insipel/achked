#include <stdio.h>
#include "../eanimpa/build_tree_lib.h"

extern node* build_tree (int);

typedef struct _node_list {
    int level;
    struct _node_list *next;
    node *tree_node;
} node_list;

node_list *
get_level_list(node_list **list, int level)
{
    node_list *new_list, *temp_list = *list, *prev_list = *list;
    int temp = level;

    while(temp_list && temp) {
        prev_list = temp_list;
        temp_list= temp_list->next;
        temp--;
    }

    if (!temp_list) {
        new_list = (node_list *) malloc(sizeof(node_list));
        new_list->level = level;
        new_list->tree_node = NULL;
        new_list->next = NULL;

        if (prev_list) {
            prev_list->next = new_list;
        } else {
            *list = new_list;
        }

        return new_list;

    } else {

        return temp_list;
    }

}

void
add_cur_node(node_list *level_list, node *cur_node)
{
    node *tree_node = level_list->tree_node;
    node *new_tree_node;

    while(tree_node && tree_node->left) tree_node=tree_node->left;

    new_tree_node = malloc(sizeof(node));
    new_tree_node->data = cur_node->data;
    new_tree_node->left = NULL;

    if(!tree_node) {
        level_list->tree_node = new_tree_node;
    } else {
        tree_node->left = new_tree_node;
    }
}

void
add_node(node *cur_node, node_list **list, int level)
{
    node_list *level_list;

    printf("level:%d\n", level);
    level_list = get_level_list(list, level);
    add_cur_node(level_list, cur_node);
}

void
print_level_tree(node *cur_node, node_list **list, int *level)
{
    if (!cur_node) {
        return;
    }

    add_node(cur_node, list, *level);
    (*level)++;
    print_level_tree(cur_node->left, list, level);
    print_level_tree(cur_node->right, list, level);
    (*level)--;
}

void
print_level_tree_data(node_list *list)
{
    node *tree_node;

    while(list) {
        tree_node = list->tree_node;
        printf("Level %02d:", list->level);
        while(tree_node) {
            printf("%02d, ", tree_node->data);
            tree_node = tree_node->left;
        }
        printf("\n");

        list = list->next;
    }
}

int
main()
{
    node *root = build_tree(20);
    node_list *list = NULL;
    int level  = 0;

    print_level_tree(root, &list, &level);
    print_level_tree_data(list);
}

