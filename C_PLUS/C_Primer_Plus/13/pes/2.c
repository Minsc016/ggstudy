/*************************************************************************
	> File Name: 2.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 30 10:04:04 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define BUFFER_SIZE 4096
/*
 * 2.  Write a file-copy program that takes the original filename and the copy file from the * command line. Use standard I/O and the binary mode, if possible.
 * */

int main(int argc, char * argv[])
{
	FILE *fpi, *fpo;
	static char buffer[4096];
	size_t bytes;

	if ( argc != 3)
	{
		printf("Usage:%s filename<source> filename<target>\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	if (! strcmp(argv[1], argv[2]))
	{
		printf("Can't append file to itself.\n");
		exit(EXIT_FAILURE);
	}
	if ((fpi = fopen(argv[1], "rb")) == NULL)
	{
		printf("Can not open file %s to read.\n", argv[1]);
		exit(EXIT_FAILURE);
	}
	if ((fpo = fopen(argv[2], "wb")) == NULL)
	{
		printf("Can not open file %s to write.\n", argv[2]);
		exit(EXIT_FAILURE);
	}
	if (setvbuf(fpi, NULL, _IOFBF, BUFFER_SIZE) || setvbuf(fpo, NULL, _IOFBF, BUFFER_SIZE))
	{
		printf("Can not create read/write buffer.\n");
		exit(EXIT_FAILURE);
	}

	while ((bytes = fread(buffer, sizeof (char), BUFFER_SIZE, fpi)) > 0) 
	{
		fwrite(buffer, sizeof (char), BUFFER_SIZE, fpo);
	}
	if (ferror(fpi) || ferror(fpo))
		printf("error in reading/writints files.\n");

	if (fclose(fpi) || fclose(fpo))
		puts("Error occurred at closing files.");


	return 0;
}
