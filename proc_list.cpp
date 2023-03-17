#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <dirent.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
int main(){
        struct dirent* dent;
        DIR* srcdir = opendir("/proc");
        while((dent = readdir(srcdir)) != NULL){
        if(strcmp(dent->d_name , ".") == 0 || strcmp(dent->d_name, "..") == 0
                 || strcmp(dent->d_name, ":") > 0)
                continue;
        char dir_path[256] = "/proc/";
        strcat(dir_path,dent->d_name);
        strcat(dir_path,"/status");
        int  fd_stat = open(dir_path,O_RDONLY);
        char first_line [256] = "";
        char read_char [2] = "";
        while(read(fd_stat,read_char,1) != 0){
                strcat(first_line,read_char);
                if(read_char[0] == '\n')
                        break;
        }
        printf("PID:\t%s\t%s",dent->d_name,first_line);
        close(fd_stat);
        }
        closedir(srcdir);
        return 0;
}
