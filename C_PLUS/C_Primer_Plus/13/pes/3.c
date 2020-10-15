/*************************************************************************
	> File Name: 3.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 30 10:49:24 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#include<ctype.h>


/*
 * 3.  Write a file copy program that prompts the user to enter the name of a text file to act as 
 * the source file and the name of an output file. The program should use the toupper()
 * function from ctype.h to convert all text to uppercase as it’s written to the output file. 
 * Use standard I/O and the text mode. 
 * */
#define SLEN 81
#define BUFFER_SIZE 64
void fcopy(FILE * src, FILE * tgt);
int main(void)
{

	char filesrc[SLEN], filetgt[SLEN];
	FILE *src, *tgt;
	puts("Enter the name of source file:");
	if (scanf("%s", filesrc) == 1)
	{
		puts("Enter the name of target file:");
		if (scanf("%s", filetgt) == 1)
		{
			if ((src = fopen(filesrc, "r")) == NULL )
			{
				printf("Can not open file %s to read.\n", filesrc);
				exit(EXIT_FAILURE);
			}
			else if ((tgt = fopen(filetgt, "w")) == NULL)
			{
				printf("Can not open file %s to write.\n", filetgt);
				exit(EXIT_FAILURE);
			}
		}
	}

	fcopy(src, tgt);
	if (ferror(src) || ferror(tgt))
	{
		printf("Error occurred at reading/writing files.\n");
	}

	if (fclose(src) || fclose(tgt))
	{
		printf("Errors occurred at closing files.\n");
	}
	return 0;
}

void fcopy(FILE * src, FILE * tgt)
{
	char ch;
	while ((ch = getc(src)) != EOF && (ch = toupper(ch)) )
		putc(ch, tgt);
}
