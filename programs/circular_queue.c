#include <stdio.h>

//variables.
int maxsize, front = -1, rear = -1, Q[50], choice, exited = 0, item, i;

//operations.
void insert();
void delete();
void display();
void exitProgram();

void makeSelection();

void main()
{
    //get maxszie of Queue.
    printf("Enter the size of Queue : ");
    scanf("%d", &maxsize);

    //do while loop for executing multiple operations on a single execution.
    do {

        // show available operations.
        printf("\n\n --- Available Operations --- \n\n");
        printf("1). Insertion \n");
        printf("2). Deletion \n");
        printf("3). Display \n");
        printf("4). Exit \n");

        printf("Enter your choice : \n");
        scanf("%d", &choice);

        makeSelection();

    } while(exited != 1);
}


void makeSelection()
{
    switch(choice){
        case 1 :
            insert();
        break;
        case 2 :
            delete();
        break;
        case 3 :
            display();
        break;
        case 4 :
            exitProgram();
        break;
        default :
            printf("Invalid selection, Please try again...\n");
    }
}


void insert()
{
    if(front == (rear+1) % maxsize)
    {
        printf("\n\n Queue is full. \n\n");
    } else {
        if(front == -1 && rear == -1)
        {
            front++;
        }

        //read item.
        rear  = (rear+1) % maxsize;
        printf("\n Enter the item : ");
        scanf("%d", &item);
        Q[rear] = item;
        printf("%d inserted to the Queue", item);
    }
}

void delete()
{
    if(front == -1)
    {
        printf("\n\n Queue is empty..\n");
    } else {
        if(front == rear)
        {
            front = -1;
            rear = -1;
            printf("\n\n Queue resetted.\n\n");
        }

        item = Q[front];
        printf("%d is deleted from Queue", item);
        front = (front + 1) % maxsize;
    }
}

void display()
{
    if(front == -1)
        printf("\nQueue is empty...\n");
    else
    {
        printf("\n\n Elements in Queue : ");
        if(front <= rear)
        {
            for(i = front; i <= rear; i++)
            {
                printf("%d ", Q[i]);
            }
        } else if(front > rear){
            for(i = front; i <= maxsize-1; i++)
            {
                printf("%d ", Q[i]);
            }
            for(i = 0; i <= rear; i++)
            {
                printf("%d ", Q[i]);
            }
        }
    }
}

void exitProgram()
{
    exited = 1;
    printf("\nBye... ;) \n");
}