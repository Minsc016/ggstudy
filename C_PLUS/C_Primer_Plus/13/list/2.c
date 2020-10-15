/*************************************************************************
	> File Name: 2.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 16 19:30:41 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define LEN 9
int main(int argc, char * argv[])
{
	FILE *in, *out;
	int ch;
	char name[LEN];
	int count = 0;

	if (argc < 2)
	{
		printf("Usage: %s filename\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	if ((in = fopen(argv[1], "r")) == NULL)
	{
		fprintf(stderr, "couldn't open file \"%s\"\n", argv[1]);
		exit(EXIT_FAILURE);
	}
	strncpy(name, argv[1], LEN - 5);
	name[LEN-5] = '\0';
	strcat(name,".red");

	if ((out = fopen(name, "w")) == NULL)
	{
		fprintf(stderr,"can not create output file");
		exit(3);
	}

	while ((ch = getc(in)) != EOF)
		if (0 == count++ % 3)
			putc(ch, out);

	if (fclose(in) != 0 || fclose(out) != 0)
		fprintf(stderr, "Error in closing files\n");
	return 0;
}
