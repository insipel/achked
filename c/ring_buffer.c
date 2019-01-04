#include <stdio.h>
#include <pthread.h>

#define MAX_SZ (1024/100)
#define MAX_DATA (2000/100)

typedef struct _RingBuff {
    int data[MAX_SZ];
} RingBuff;

RingBuff buffer;
int num_read = 0;
int num_written = 0;

int read_ptr = 0;
pthread_mutex_t read_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t  read_cond = PTHREAD_COND_INITIALIZER;

int write_ptr = 1;
pthread_mutex_t write_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t  write_cond = PTHREAD_COND_INITIALIZER;

/*
 * Algorithm:
 *  Producers will produce buffers in the ring buffer. They will wait
 *  for buffers to be empty if consumers are slow to consume. If there
 *  are more producers, then a lot of them will be blocked either on
 *  the mutex or on the condition variable. When they become
 *  unblocked, it's possible that total data to be written is already
 *  over, so they need to unlock the mutex and return.
 *
 *  Consumers will also need to follow the same concept as producers.
 */

void *
producer(void *arg)
{
    while (num_written < MAX_DATA) {
        pthread_mutex_lock(&write_mutex);
        while ((write_ptr + 1)%MAX_SZ == read_ptr) {
            printf("[%lu]: Buffer full: write_ptr:%d read_ptr:%d\n", (unsigned long) pthread_self(), write_ptr, read_ptr);

            if (num_written >= MAX_DATA) {
                printf("[%lu]: returning\n", (unsigned long) pthread_self());
                pthread_mutex_unlock(&write_mutex);
                return;
            }

            pthread_cond_wait(&write_cond, &write_mutex);

            if (num_written >= MAX_DATA) {
                printf("[%lu]: returning\n", (unsigned long) pthread_self());
                pthread_mutex_unlock(&write_mutex);
                return;
            }
        }

        buffer.data[write_ptr] = rand()%30;
        printf("[%lu]: Generated: index:%d data:%d\n", (unsigned long) pthread_self(), write_ptr, buffer.data[write_ptr]);

        write_ptr = (write_ptr + 1)%MAX_SZ;
        num_written++;
        pthread_cond_signal(&read_cond);
        pthread_mutex_unlock(&write_mutex);
    }

    //pthread_cond_broadcast(&read_cond);
    printf("[%lu]: returning\n", (unsigned long) pthread_self());
}

void *
consumer(void *arg)
{
    while(num_read < MAX_DATA) {
        pthread_mutex_lock(&read_mutex);
        while( (read_ptr+1)%MAX_SZ == write_ptr) {
            printf("\t[%lu]: Buffer empty: write_ptr:%d read_ptr:%d\n", (unsigned long) pthread_self(), write_ptr, read_ptr);

            if (num_read >= MAX_DATA) {
                printf("\t[%lu]: returning\n", (unsigned long) pthread_self());
                pthread_mutex_unlock(&read_mutex);
                return;
            }

            pthread_cond_wait(&read_cond, &read_mutex);

            if (num_read >= MAX_DATA) {
                printf("\t[%lu]: returning\n", (unsigned long) pthread_self());
                pthread_mutex_unlock(&read_mutex);
                return;
            }
        }

        read_ptr = (read_ptr + 1) % MAX_SZ;

        printf("\t[%lu]: Consumed: index:%d data:%d\n", (unsigned long) pthread_self(), read_ptr, buffer.data[read_ptr]);
        buffer.data[read_ptr] = -1;

        pthread_cond_signal(&write_cond);

        num_read++;
        pthread_mutex_unlock(&read_mutex);
    }

    //pthread_cond_broadcast(&write_cond);
    printf("\t[%lu]: returning\n", (unsigned long) pthread_self());
}

int main()
{
    int i;
#define NUM_THREADS 1
#define NUM_PRODUCER_THREADS 20
#define NUM_CONSUMER_THREADS 5

    pthread_t tid_con[NUM_THREADS], tid_prod[NUM_PRODUCER_THREADS];

    srand(time(NULL));
    for(i = 0; i < NUM_THREADS; i++) {
        pthread_create(&tid_con[i], NULL, consumer, NULL);
    }

    for(i = 0; i < NUM_PRODUCER_THREADS; i++) {
        pthread_create(&tid_prod[i], NULL, producer, NULL);
    }

    for(i = 0; i < NUM_THREADS; i++) {
        pthread_join(tid_con[i], NULL);
        printf("Consumer[%d] returned\n", i);
    }


    for(i = 0; i < NUM_PRODUCER_THREADS; i++) {
        pthread_join(tid_prod[i], NULL);
        printf("Producer[%d] returned\n", i);
    }
    printf("Consumer and Producers returned\n");
}

