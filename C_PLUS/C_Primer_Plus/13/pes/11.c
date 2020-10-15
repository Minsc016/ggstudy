/*************************************************************************
	> File Name: 11.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Sat Oct 10 12:07:41 2020
 ************************************************************************/

/* 11.  Write a program that takes two command-line arguments. 
 * The first is a string; 
 * the second is the name of a file. 
 * The program should then search the file, printing all lines containing the string. 
 * Because this task is line oriented rather than character oriented, 
 * use fgets() instead of getc() . Use the standard C library function strstr() (briefly 
 * described in exercise 7 of Chapter 11 ) to search each line for the string. 
 * Assume no lines are longer than 255 characters.  
 * */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define BUFFSIZE 256

int main(int argc, char * argv[])
{
	FILE * fp;
	char line[BUFFSIZE];

	if (3 != argc)
	{
		printf("Usage:%s string filename\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	
	if ((fp = fopen(argv[2], "r")) == NULL)
	{
		printf("can not open file %s to read.\n", argv[2]);
		exit(EXIT_FAILURE);
	}
	while (fgets(line, BUFFSIZE, fp) && line[0] != EOF)
	{
		if (strstr(line, argv[1]))
			fputs(line, stdout);
	}

	return 0;
}
