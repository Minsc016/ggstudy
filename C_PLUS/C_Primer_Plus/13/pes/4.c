/*************************************************************************
	> File Name: 4.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 30 11:34:17 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * 4.  Write a program that sequentially displays onscreen all the files listed in the command 
 * line. Use argc to control a loop. 
 * */

void display (const char *);
int main(int argc, char * argv[])
{
	if (argc < 2)
	{
		printf("no files entered. program shutdown now.\n");
		exit(EXIT_FAILURE);
	}
	for (int i = 1; i < argc; i++)
	{
		printf("showing the file %s now.\n", argv[i]);
		display(argv[i]);
		printf("\n");
	}

	return 0;
}

void display (const char * file)
{
	FILE * fp;
	char temp[256];
	if ((fp = fopen(file, "r")) == NULL)
	{
		printf("can't open file %s to read.\n", file);
	}

	while (fgets(temp, 256, fp) && temp[0] != EOF)
	{
		fputs(temp, stdout);
	}
}

