// Circular Queue implementation in Java.

import java.util.Scanner;

public class CircularQueue {
    int front, rear, size;
    int[] queue;

    public CircularQueue(int size) {
        this.size = size;
        front = -1;
        rear = -1;
        queue = new int[size];
    }

    public void insert(int data) {
        if (front == -1 && rear == -1) {
            front = rear = 0;
            queue[rear] = data;
        } else if ((rear + 1) % size == front) {
            System.out.println("Queue is full...");
        } else {
            rear = (rear + 1) % size;
            queue[rear] = data;
        }
    }

    public void delete() {
        if (front == -1 && rear == -1) {
            System.out.println("Queue is empty...");
        } else if (front == rear) {
            front = rear = -1;
        } else {
            front = (front + 1) % size;
        }
    }

    public void display() {
        if (front == -1 && rear == -1) {
            System.out.println("Queue is empty..");
        } else {
            int i = front;
            while (i != rear) {
                System.out.print(queue[i] + " ");
                i = (i + 1) % size;
            }
            System.out.println(queue[rear]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the queue");
        int size = sc.nextInt();
        CircularQueue cq = new CircularQueue(size);
        int choice = 0;
        while (choice != 4) {
            System.out.println("1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.println("Enter your choice : ");
            choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter the data to be inserted : ");
                    int data = sc.nextInt();
                    cq.insert(data);
                    break;
                case 2:
                    cq.delete();
                    break;
                case 3:
                    cq.display();
                    break;
                case 4:
                    System.out.println("Exiting....");
                    break;
                default:
                    System.out.println("Invalid choice...");
            }
        }
    }
}