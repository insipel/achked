#include <stdio.h>
#include <stdlib.h>

typedef unsigned char  uint8_t;
typedef unsigned short uint16_t;
typedef unsigned int   uint32_t;

typedef struct _node {
    
    uint32_t     data;
    struct _node *parent;
    struct _node *left;
    struct _node *right;

} node;

extern node* build_tree (int);
extern node* build_tree_data (int,...);

