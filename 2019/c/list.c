#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char  uint8_t;
typedef unsigned short uint16_t;
typedef unsigned int   uint32_t;

typedef struct _node {
    uint32_t      data;
    struct _node  *next;
} node; 

node *make_linklist(short *arr, uint32_t size, node **tail)
{
    uint32_t idx = 0;
    node *cur_node, *head, *next_node;

    printf("Making the list, size:%d\n", size);

    if (size == 0) {
        printf("Null list\n");
        *tail = NULL;
        return NULL;
    }

    head = (node *) malloc(sizeof(node));
    printf("Head ptr:%p\n", head);
    cur_node = head;
    cur_node->data = arr[idx];
    idx++;

    while(idx < size) {
        next_node = (node *) malloc(sizeof(node));
        cur_node->next = next_node;
        cur_node = next_node;


        cur_node->data = arr[idx];
        idx++;
    }

    cur_node->next = NULL;
    *tail = cur_node;
    printf("Tail ptr:%p\n", *tail);
    return head;
}

void print_list(node *head, node *tail)
{
    printf("head:%p tail:%p\n" ,head, tail);
    printf("list elems are: ");
    while (head) {
        printf("%d, ", head->data);
        head = head->next;
    }
    printf("\n");
    if (tail) printf("Tail elem:%d\n\n", tail->data);
}

void delete_node(node **head, node **tail, uint16_t data)
{
    node *temp = *head;

    if (!*head) {
        printf("list is empty. return\n");
        return;
    }

    if ((*head)->data == data) {
        printf("first element delete\n");
        *head = (*head)->next;
        free(temp);

        if(!*head) {
            *tail = NULL;
            printf("setting tail to null\n");
        }

        return;
    }

    while(temp && temp->next) {
        if (temp->next->data == data) {
            break;
        }
        temp = temp->next;
    }

    if (temp->next) {
        temp->next = temp->next->next;

        if (!temp->next) {
            *tail = temp;
            printf("last element removed. updating tail\n");
        }

    }

    return;
}

void insert_after(node **head, node **tail, uint16_t data1, uint16_t data2)
{
    node *temp = *head;
    node *new_node;

    while(temp && temp->next) {
        if (temp->data == data1) {
            break;
        }
        temp = temp->next;
    }
    printf("out of the loop\n");

    new_node = (node *) malloc(sizeof(node));
    new_node->data = data2;
    new_node->next = NULL;

    /* non-empty list */
    if (temp) {

        /* middle */
        if(temp->next) {
            new_node->next = temp->next;
        }

        temp->next = new_node;
    }

    if (!*head) {
        printf("null head\n");
        *head = new_node;
    }
    if (!new_node->next) {
        printf("adding at the end\n");
        *tail = new_node;
    }

    return;
}

int main ()
{
#if 1
    uint16_t arr[] = {53, 6, 18, 45, 32, 67, 29, 8, 82, 89, 60, 22, 11};
    uint16_t null_arr[]  = {};
    uint16_t one_elem_arr[] = {4};
    uint16_t two_elem_arr[] = {34, 12};
#else
    uint16_t arr[][] = {{53, 6, 18, 45, 32, 67, 29, 8, 82, 89, 60, 22, 11},
                        {34, 12},
                        {4},
                        {1}};
#endif

    node     *head[4];
    node     *tail[4];
    uint16_t  which_test, which_list;
    uint16_t  data1, data2;
    char      line[32];

    head[0] = make_linklist(arr, sizeof(arr)/sizeof(uint16_t), &tail[0]);
    printf("List prepared head:%p\n", head[0]);
    print_list(head[0], tail[0]);
    printf("\n");

    head[1] = make_linklist(null_arr, sizeof(null_arr)/sizeof(uint16_t), &tail[1]);
    printf("Null List prepared head:%p\n", head[1]);
    print_list(head[1], tail[1]);
    printf("\n");

    head[2] = make_linklist(one_elem_arr, sizeof(one_elem_arr)/sizeof(uint16_t), &tail[2]);
    printf("1 elem List prepared head:%p\n", head[2]);
    print_list(head[2], tail[2]);
    printf("\n");

    head[3] = make_linklist(two_elem_arr, sizeof(two_elem_arr)/sizeof(uint16_t), &tail[3]);
    printf("2 elem List prepared head:%p\n", head[3]);
    print_list(head[3], tail[3]);
    printf("\n");

    while (1) {

        printf("######################################\n");
        printf("# List 1: regular, 2: Null, 3: 1 elem, 4: 2 elem\n");
        printf("=================================================\n");
        printf("# 1: insertAfter <which list> <data> <data>\n");
        printf("# 2: deleteNode <which list> <data>\n");
        printf("######################################\n");

        printf("Test#:");
        fgets(line, 32, stdin);
        sscanf(line, "%d %d %d", &which_test, &which_list, &data1, &data2);
        which_test = line[0] - '0';
        which_list = line[2] - '0';
        // data1      = line[4] - '0';
        // data2      = line[6] - '0';

        printf("which_test:%d which_list:%d data:%d %d\n", which_test, which_list, data1, data2);

        switch(which_test) {
            case 1: /* insert after */
                insert_after(&head[which_list], &tail[which_list], data1, data2);
                print_list(head[which_list], tail[which_list]);
                break;

            case 2: /* deleteNode */
                delete_node(&head[which_list], &tail[which_list], data1);
                print_list(head[which_list], tail[which_list]);
                break;

            default:
                break;
        }
    }
}

