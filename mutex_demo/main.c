#include <pthread.h>
#include <stdio.h>

#ifndef LOCK
  #define LOCK 0
#endif

int counter = 0;
pthread_mutex_t mtx;

void *worker(){
  for (int i = 0; i < 1000000; i++){
#if LOCK
    pthread_mutex_lock(&mtx);
#endif
    counter++;
#if LOCK
    pthread_mutex_unlock(&mtx);
#endif
  }
  return NULL;
}

int main(){
  pthread_mutex_init(&mtx, NULL);

  pthread_t t1,t2;
  pthread_create(&t1, NULL, worker, NULL);
  pthread_create(&t2, NULL, worker, NULL);

  pthread_join(t1,NULL);
  pthread_join(t2,NULL);
  pthread_mutex_destroy(&mtx);

  printf("%d",counter);
}

