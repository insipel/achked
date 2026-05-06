/*
 * Simple thread program to try one producer and one consumer.
 */
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include "../practice_hdr.h"

#define MAX_BUF_SIZE 100
unsigned short bounded_buf[MAX_BUF_SIZE];

/*
 * Lock to use between producer and consumer.
 */
struct _shared_p_c {
    pthread_mutex_t mutex_p_c;
} shared_p_c = { PTHREAD_MUTEX_INITIALIZER };

/*
 * Lock for Producers only.
 */
struct _shared_p {
    pthread_mutex_t mutex_p;
    unsigned int prod_index;
} shared_p = { PTHREAD_MUTEX_INITIALIZER, 0};

/*
 * Lock for consumers only.
 */
struct _shared_c {
    pthread_mutex_t mutex_c;
    unsigned int cons_index;
} shared_c = {PTHREAD_MUTEX_INITIALIZER, 0;

/*
 * Not critical section.
 */
unsigned short prod_ut_buf[MAX_BUF_SIZE];
unsigned short cons_ut_buf[MAX_BUF_SIZE];

void *
producer(void *args)
{
    while(1) {
        printd("%s:%p rep:  %02d\n", __func__, args, *((int *)args));
        if (*((int *)args) > 10) {
            printd("%s returning\n", __func__);
            return NULL;
        }

        *((int *)args)+=1;

        pthread_mutex_lock(&shared_p.mutex);

        bounded_buf[i] = rand() % (1 << sizeof(unsigned short));
        prod_ut_buf[i] = bounded_buf[i];
        prod_idx++;

        pthread_mutex_unlock(&shared.mutex);
    }
}

void *
consumer(void *args)
{
    while(1) {
        printd("%s:%p rep:\t%02d\n", __func__, args, *((int *) args));
        if (*((int *) args) > 10) {
            printd("%s returning\n", __func__);
            return NULL;
        }

        *((int *) args)+=1;

        pthread_mutex_lock(&shared.mutex);
        shared.count += 10;
        pthread_mutex_unlock(&shared.mutex);
    }
}

void
inspect_buffer()
{
    int i = 0;

    for (; i < MAX_BUF_SIZE; i++) {
        if (bounded_buf[i] != 
    }
}

int main(int argc, int *argv)
{
    pthread_t tid_producer, tid_consumer;
    unsigned int reps[] = {0, 0};

    srand(time(NULL));
    /*
     * init the bounded buffer.
     */
    memset(bounded_buf, 0xFF, sizeof(bounded_buf));

    pthread_create(&tid_producer, NULL, producer, &reps[0]);
    pthread_create(&tid_consumer, NULL, consumer, &reps[0]);

    pthread_join(tid_producer, NULL);
    pthread_join(tid_consumer, NULL);
    printd("%s: reps: %d,%d shared.count:%d\n",
            __func__, reps[0], reps[1], shared.count);

    inspect_buffer();
}
