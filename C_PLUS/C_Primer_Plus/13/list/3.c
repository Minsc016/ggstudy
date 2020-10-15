/*************************************************************************
	> File Name: 3.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 16 19:40:50 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define MAX 41
int main(void)
{
	FILE *fp;
	char words[MAX];

	//if ((fp = fopen("wordy", "a+")) == NULL)
	if ((fp = stdout ) == NULL)
	{
		fprintf(stdout, "can not open \"wordy\" file.\n");
		exit(EXIT_FAILURE);
	}
	puts("Enter words to add to the file; press the #");
	puts("key at the begining of a line to terminate.");
	while ((fscanf(stdin, "%40s", words) == 1) && (words[0] != '#'))
		fprintf(fp,"%s\n", words);

	puts("File contents:");
	rewind(fp);
	while (fscanf(fp, "%s", words) == 1)
		puts(words);
	puts("Done!");
	if (fclose(fp) != 0)
	{
		fprintf(stderr, "Error closing file\n");
	}
	return 0;
}
