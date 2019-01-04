/*1. Write a program to implement stack.
 *  define a Libraray
 */

struct stackNode {
    uint32_t data;
    struct stackNode *next;
}

struct stack{
     struct stackNode *top;
     uint32_t count;
     
}

bool stack_create(struct stack **stackptr)
{
     struct stack *s;
     
     s = calloc(1, sizeof(struct stack));
     if(!s) {
         *stackptr = NULL;
         return false;
     }
     s->top = NULL;
     s->count = 0;
     
     *stackptr = s;
     
     return true;
     
}
/*
 struct stack *s;
 rc = stack_create ( &s);
 */

bool push(struct stack *s, uint32_t data)
{
     struct stackNode *node;
     
     if (!s) {
         return false;
     }
     
     node = malloc(sizeof(struct stackNode));
     if(!node) {
         return false;
     }
     
  
     node->data = data;
     node->next = top;
     
     s->top = node;
     s->count++;
     return true;
     
     
     
}

bool pop(struct stck *s, uint32_t *data)
{
    struct stackNode *node;
    
    if(!s || s->count <=0) {
        return false;
    }
    
    node = s->top;
    s->top = node->next;
    s->count--;
    
    *data = node->data;
    free(node);
    
    return true;
        
}

bool stack_delete(stackNode *top)
{

 
}



