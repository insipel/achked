#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

void func(int *arr,int *path, int *cost, int size,int linewidth);
void print_path(int *path, int size, int *arr);

int main()
{
    int *arr,size, linewidth, *path,*cost;

    cout<<"ent the total number of words: ";
    cin>>size;

    arr=new int[size];
    path=new int[size];
    cost=new int[size];

    srand(time(NULL));
    cout<<"ent the word len array:\n";
    for(int i=0;i<size;i++) {
        arr[i] = (rand() % 5 + 1);
        cout << "i:"<<i<<"word length:"<<arr[i]<<"\n";
    }

    cout<<"ent line width: ";

    cin>>linewidth;
    func(arr,path,cost,size,linewidth);
    cout<<"\n";
    print_path(path,size, arr);
}

void print_path(int *path, int size, int *arr)
{
    int end, start=0;
    while(start!=size)
    {
        end= path[start]+1; // + 1 because to display '1' based indices


        /* print routine */
        cout<<"word start point= "<<start+1<<" end point= "<<end<<endl;
        cout<<"|";
        for(int i=0; i < (end -start); i++) {


            for(int j=0; j < arr[start+i]; j++) {
                cout<<"a";
            }
            cout<<" ";
        }
        cout<<"|\n";

        /* after done with current line, move to the word after the
         * current line ended.
         */
        start=path[start]+1;
    }
}

#define DEBUGPRINT_FUNC
#ifdef DEBUGPRINT_FUNC
#define PRINT_FUNC(a,...) (a, ## __VA_ARGS__);
#else
#define PRINT_FUNC(a...)
#endif

void func(int *arr,int *path, int *cost, int size,int linewidth)
{
    int end=size-1;

    cout<<"\n\nsize:"<<size<<" end:"<<end<<endl;
    // PRINT_FUNC(cout<<"size:%d end:%d", size, end);

    for(int i=end; i>=0; i--)
    {
        int len=0, min=1111111111,index;

        cout<<"\tLine:"<<__LINE__<<" i:"<<i<<"\n\n";
        for(int j=i; j<size;j++)
        {
            cout<<"\t\tLine:"<<__LINE__<<" i:"<<i<<" j:"<<j<<" size:"<<size<<endl;
            //include words till i to j
            len+=arr[j];
            printf("\t\tLine:%d len:%d arr[%d]:%d\n", __LINE__, len, j, arr[j]);
            if(len>linewidth) {
                printf("\t\t\tLine:%d BREAK: len:%d width:%d\n", __LINE__, len, linewidth);
                break;
            } else
            {
                int p=linewidth-len;
                int c=pow(p,3);

                if(j<size-1) {
                    c+=cost[j+1];
                    printf("\t\tLine:%d pow(p,3):%d c:%d Previous cost[%d-j+1]:%d\n",
                           __LINE__, (p*p*p), c, j, cost[j+1]);
                }

                if(c<min)
                {
                    min=c;
                    index=j;
                    printf("\t\tLine:%d c:%d min:%d index:%d\n", __LINE__, c, min, index);
                }
                len=len+1; // space b/w 2 words
            }
        }

        cost[i]=min;
        path[i]=index;
        printf("\tLine:%d cost[%d-i]:%d path[%d-i]:%d\n", __LINE__, i, cost[i], i, path[i]);
    }
}
