#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
#include <limits.h>

#define EVER (;;)

FILE* loadFile(char *filename);
void closeFile(FILE *inp); 
char encode(char a);
char decode(char a);
         
int main (int argc, char const *argv[])
{
    if(argc < 3)
    {
        printf("Not enough arguments!\n[FILE] [e(ncode) or d(ecode)]");
        return 1;
    }
    FILE *inp = loadFile((char*)argv[1]);
    char *line = calloc(1024, sizeof(char)); 
    while(fgets(line, 1024, inp) != NULL){
        for(size_t i = 0; i < strlen(line); ++i)
        {
            if(strcmp(argv[2], "e") == 0)
            {
                 printf("%c", encode(line[i]));  
            }else if(strcmp(argv[2], "d") == 0)
            {
                 printf("%c", decode(line[i]));           
            }          
        }                                 
    } 
    free(line); 
    closeFile(inp);
    return 0;
}      

FILE* loadFile(char* filename){
    FILE* inp  = fopen(filename, "r");
    if(inp != NULL)
        return inp;
    exit(0);    
}  

void closeFile(FILE* file){
    fclose(file);
} 

char encode(char a){
    if((int)a == 255)
    {
        return a = 1;
    }
    return a + 1;
} 

char decode(char a){
    if((int)a == 1)
    {
        return a = 255;
    }
    return a - 1;
}  