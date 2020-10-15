/*************************************************************************
	> File Name: 9.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Sat Oct 10 10:02:11 2020
 ************************************************************************/

/*
 * 9.  Modify the program in Listing 13.3 so that each word is numbered according to the order 
 * in which it was added to the list, starting with 1. Make sure that, when the program is 
 * run a second time, new word numbering resumes where the previous numbering left off. 
 * */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#define MAX 41
int main(void)
{
	FILE *fp, *fpc;
	char words[MAX];
	int num = 0;
	char ch;
	long total = 0L;
	if ((fp = fopen("wordy", "a+")) == NULL)
	{
		fprintf(stdout, "Can't open \"wordy\" file.\n");
		exit(EXIT_FAILURE);
	}
	if ((fpc = fopen("wordy_num", "r")) == NULL)
	{
		fprintf(stdout, "can not open \"wordy_num\" file.\n");
		exit(EXIT_FAILURE);
	}


	/* read num */
	if ( fscanf(fpc, "%d", &num) == 1 )
		printf("num read:%d\n", num);
	else
	{
		printf("num %d read error, set it to 0\n", num);
		num = 0;
	}
	fclose(fpc);
	/* end read */
	if ((fpc = fopen("wordy_num","w")) == NULL)
	{
		fprintf(stdout, "can not open \"wordy_num\" file to write.\n");
		exit(EXIT_FAILURE);
	}

	puts("Enter words to add to the file; press the # key at the beginning of a line to terminate.");
	while ((fscanf(stdin, "%40s", words) == 1) && (words[0] != '#'))
	{
		fprintf(fp, "%s\n", words);
		num++;
	}
	fprintf(fpc, "%d\n", num);
	puts("File contents:");
	rewind(fp);				/* go back to beginning of file */
	while (fscanf(fp, "%s", words) == 1)
		puts(words);
	puts("Done!");


	if (fclose(fp))
		fprintf(stderr, "Error closing wordy file.\n");
	if (fclose(fpc))
		fprintf(stderr, "Error closing num file.\n");
	return 0;
}
