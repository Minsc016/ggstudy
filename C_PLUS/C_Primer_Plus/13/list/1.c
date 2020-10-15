/*************************************************************************
	> File Name: 1.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 16 19:26:41 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int main(int argc, int *argv[])
{
	int ch;
	FILE *fp;
	unsigned long count = 0;
	if (argc != 2)
	{
		printf("Usage: %s filename\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	if ((fp = fopen(agv[1],"r")) == NULL)
	{
		printf("Can't open %s\n", argv[1]);
		exit(EXIT_FAILURE);
	}
	while ((ch = getc(fp)) != EOF)
	{
		putc(ch, stdout);
		count++;
	}

	fclose(fp);
	printf("FIle %s has %lu characters\n", argv[1], count);
	return 0;
}
