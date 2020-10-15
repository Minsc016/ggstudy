/*************************************************************************
	> File Name: 10.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Sat Oct 10 11:23:23 2020
 ************************************************************************/
/*
 * 10.  Write a program that opens a text file whose name is obtained interactively. Set up a 
 * loop that asks the user to enter a file position. The program then should print the part of 
 * the file starting at that position and proceed to the next newline character. Let negative 
 * or nonnumeric input terminate the user-input loop. 
 * */


#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define SLEN 81

int main(void)
{
	char txt[SLEN];
	FILE * fp;
	long position = 0L;
	char ch;

	fputs("Enter the name of a text file:", stdout);
	if (fscanf(stdin, "%s", txt) == 1)
	{
		if ((fp = fopen(txt, "r")) == NULL)
		{
			printf("can not open file %s to read.\n", txt);
			exit(EXIT_FAILURE);
		}
	}
	else
		fputs("filename entered error\n", stdout);


	fputs("Enter the position of the file you wanna print(negative or nonumeric input to quit):\n", stdout);
	while( (fscanf(stdin, "%ld", &position) == 1 ) && position > 0 )
	{
		printf("pos read:%ld\n", position);
		for (long i = position; ; i ++)
		{
			fseek(fp, i, SEEK_SET);
			ch = getc(fp);
			putc(ch, stdout);
			if ('\n' == ch)
				break;
		}
		fputs("Enter a new position(negative or nonumeric to quit):\n", stdout);
	}




	return 0;
}
