#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>


struct proc_stat{
        int pid;                                                               
        char comm [256];
        char state;                                                                
        int ppid;
        int pgrp;                                                       
        int session;
        int tty_nr;                                                             
        int tpgid;
        unsigned int flags;
        unsigned long minflt;                                                    
        unsigned long cminflt;
        unsigned long majflt;
        unsigned long cmajflt;
        unsigned long utime;
        unsigned long stime;
        long cutime;
        long cstime;
        long priority;
        long nice;
        long num_threads;
        long itrealvalue;
        unsigned long long starttime;
        unsigned long vsize;
        long rss;
};


int main(int argc, char* argv[]){
        if(argc == 2){
                char path [256] = "/proc/";
                strcat(path, argv[1]);
                char stat_path[256];
                strcpy(stat_path,path);
                strcat(stat_path,"/stat");
                struct proc_stat ps;
                FILE*  stat_file = fopen(stat_path,"r");
                fscanf(stat_file,"%d %s %c",&ps.pid, &ps.comm, &ps.state);
                fscanf(stat_file,"%d %d %d %d %d %u",&ps.ppid,&ps.pgrp,&ps.session,&ps.tty_nr,     
                                &ps.tpgid,&ps.flags);
                fscanf(stat_file,"%lu %lu %lu %lu %lu",&ps.minflt,&ps.cminflt,&ps.majflt,        
                                &ps.cmajflt,&ps.utime);
                fscanf(stat_file,"%lu %ld %ld %ld %ld",&ps.stime, &ps.cutime, &ps.cstime,        
                                &ps.priority,&ps.nice);
                fscanf(stat_file,"%ld %ld %llu %lu %ld",&ps.num_threads,&ps.itrealvalue,
                                &ps.starttime,&ps.vsize, &ps.rss);
                fclose(stat_file);
                printf("Filename = %s\nVirtual memory size = %lu\n",ps.comm,ps.vsize);
                char para_path[256];
                strcpy(para_path,path);
                strcat(para_path,"/cmdline");
                int fd_param = open(para_path, O_RDONLY);
                char buf[256] = "";
                printf("Arguments: ");
                while(read(fd_param, buf,255)!= 0)
                        printf("%s",buf);
                printf("\n");
                close(fd_param);
                char env_path[256];
                strcpy(env_path,path);
                strcat(env_path,"/environ");
                int fd_env = open(env_path,O_RDONLY);
                printf("Environment Variables: ");
                while(read(fd_env,buf,255)!= 0)
                        printf("%s",buf);
                printf("\n");
                close(fd_param);
        }
        return 0;
}