#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int getline(int fd,char *buf)
{
        char c[2] = "";
        char inner_buf [512] = "";
        int num_read = 0;
        while(read(fd,c,1) != 0)
        {
                if(c[0] == '\n') break;
                strcat(inner_buf,c);
                num_read++;
        }
        strcpy(buf,inner_buf);
        return num_read;
}

int main(){
        char path[14] = "/proc/meminfo";
        int fd_mem = open(path,O_RDONLY);
        char buf [512] = "";
        unsigned long total_memory = 0, free_memory = 0;
        while(getline(fd_mem,buf)){
                if(strncmp(buf,"MemTotal",8) == 0){
                        sscanf(buf,"MemTotal: %lu",&total_memory);
                }
                if(strncmp(buf,"MemFree",7) == 0){
                        sscanf(buf,"MemFree: %lu",&free_memory);
                }
        }
        printf("Total Memory:\t%lu (kB)\nUsed Memory:\t%lu (kB)\nFree Memory:\t%lu (kB)\n",        
                total_memory,total_memory - free_memory, free_memory);
        return 0;
}

