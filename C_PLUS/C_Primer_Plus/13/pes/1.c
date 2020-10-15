/*************************************************************************
  > File Name: 1.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep 30 09:52:54 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * 1.  Modify Listing 13.1 so that it solicits the user to enter the filename and reads the user’s 
 * response instead of using command-line arguments. 
 * */
/* copy 13.1 : count.c */
//Listing 13.1   The count.c Program 
/* count.c -- using standard I/O */
#include <stdio.h>
#include <stdlib.h> // exit() prototype
int main(int argc, char *argv[])
{
	int ch; // place to store each character as read
	FILE *fp; // "file pointer"
	unsigned long count = 0;
	char filename[999];


	if (argc != 1)
	{
		printf("Usage: %s\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	if (printf("Enter the name of file to read:\n") && fscanf(stdin, "%s", filename) != 1)
	{
		printf("filename enter wrong!\n");
		exit(EXIT_FAILURE);
	}
	if ((fp = fopen(filename, "r")) == NULL)
	{
		printf("Can't open %s\n", filename);
		exit(EXIT_FAILURE);
	}
	while ((ch = getc(fp)) != EOF)
	{
		putc(ch,stdout); // same as putchar(ch);
		count++;
	}
	fclose(fp);
	printf("File %s has %lu characters\n", filename, count);
	return 0;
} 
