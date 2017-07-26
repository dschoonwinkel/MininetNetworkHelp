/*
    Simple udp client
*/
#include <stdio.h> //printf
#include <string.h> //memset
#include <stdlib.h> //exit(0);
#include <arpa/inet.h>
#include <sys/socket.h>
#include <time.h>
 
#define SERVER "127.0.0.1"
#define BUFLEN 1000000  //Max length of buffer
#define PORT 10002   //The port on which to send data
#define RECV_PORT 32415
 
void die(char *s)
{
    perror(s);
    exit(1);
}
 
int main(void)
{
    struct sockaddr_in si_me, si_other;
    int s, r, i, slen=sizeof(si_other);
    char buf[BUFLEN];
    char* message = "Hello World!";
    clock_t start_t, end_t;
    double total_t;
    int optVal = 1;
    long itercount = 100;
 
    if ( (s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        die("socket");
    }

    if ( (r=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        die("socket");
    }

    setsockopt(s, SOL_SOCKET, SO_REUSEADDR, &optVal, sizeof(int));
    setsockopt(r, SOL_SOCKET, SO_REUSEADDR, &optVal, sizeof(int));

    memset((char *) &si_me, 0, sizeof(si_me));
    si_me.sin_family = AF_INET;
    si_me.sin_port = htons(RECV_PORT);

    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(PORT);

    if (bind(s, (struct sockaddr*)&si_me, sizeof(si_me)) == -1) {
        die("bind");
    }

    if (bind(r, (struct sockaddr*)&si_other, sizeof(si_other)) == -1) {
        die("bind receive");
    }
     
    if (inet_aton(SERVER , &si_other.sin_addr) == 0) 
    {
        fprintf(stderr, "inet_aton() failed\n");
        exit(1);
    }

    if (inet_aton(SERVER , &si_me.sin_addr) == 0) 
    {
        fprintf(stderr, "inet_aton() failed\n");
        exit(1);
    }
    start_t = clock();

    for (i = 0; i < itercount; i++) {

        // printf("Sending : \n");
        // fflush(stdout);
        
         
        //send the message
        if (sendto(s, message, strlen(message) , 0 , (struct sockaddr *) &si_other, slen)==-1)
        {
            die("sendto()");
        }
         
        // printf("Received: %s", buf);
         
        // puts(buf);
    // }
    }

    for (i = 0; i < itercount; i++) {
    //receive a reply and print it
        //clear the buffer by filling null, it might have previously received data
        //try to receive some data, this is a blocking call
        if (recvfrom(r, buf, BUFLEN, 0, (struct sockaddr *) &si_other, &slen) == -1)
        {
            die("recvfrom()");
        }
    }

    end_t = clock();
    total_t = (double)(end_t - start_t) / CLOCKS_PER_SEC / itercount * 1000;
    printf("%f ms\n", total_t);
 
    close(s);
    shutdown(s, SHUT_RDWR);
    close(r);
    shutdown(s, SHUT_RDWR);
    return 0;
}