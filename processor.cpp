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
        char path[14] = "/proc/cpuinfo";
        int fd_cpu = open(path,O_RDONLY);
        char buf [512] = "";
        while(getline(fd_cpu,buf)){
                if(strncmp(buf,"model name",10) == 0 || strncmp(buf,"cpu MHz",7) == 0 ||
                        strncmp(buf,"cache size",10) == 0)
                        printf("%s\n",buf);
        }
        return 0;
}


