/*************************************************************************
  > File Name: 14_4.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep 16 19:58:31 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
/* reverse.c -- displays a file in reverse order */
#define CNTL_Z '\032' /* eof marker in DOS text files */
#define SLEN 81
int main(void)
{
	char file[SLEN];
	char ch;
	FILE *fp;
	long count, last;
	puts("Enter the name of the file to be processed:");
	scanf("%80s", file);
	if ((fp = fopen(file,"rb")) == NULL)
	{ /* read-only mode */
		printf("reverse can't open %s\n", file);
		exit(EXIT_FAILURE);
	}
	fseek(fp, 0L, SEEK_END); /* go to end of file */
	last = ftell(fp);
	for (count = 1L; count <= last; count++)
	{
		fseek(fp, -count, SEEK_END); /* go backward */
		ch = getc(fp);
		if (ch != CNTL_Z && ch != '\r') /* MS-DOS files */
			putchar(ch);
	}
	putchar('\n');
	fclose(fp);
	return 0;
} 
