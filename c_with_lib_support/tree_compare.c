struct Node{
int data;
struct Node* left;
struct Node* right;
};



bool compare_trees(node *t1, node *t2)
{
    // both are empty 
    if(t1== NULL && t2==NULL) <--- 
        return 1;
   // both trees are non empty      
    if(t1!=NULL && t2!= NULL){
        return (compare_trees(t1->left, t2->left) && compare_trees(t1->right, t2->right)))
   
   }
   //
   return 0;
    
}

