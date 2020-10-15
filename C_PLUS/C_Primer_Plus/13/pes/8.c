/*************************************************************************
  > File Name: 8.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Fri Oct  9 16:54:17 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * 8.  Write a program that takes as command-line arguments a character and zero or more 
 * filenames. If no arguments follow the character, have the program read the standard 
 * input. Otherwise, have it open each file in turn and report how many times the character 
 * appears in each file. The filename and the character itself should be reported along with 
 * the count. Include error-checking to see whether the number of arguments is correct and 
 * whether the files can be opened. If a file can’t be opened, have the program report that 
 * fact and go on to the next file.
 * */

#define SLEN 81

char * s_gets(char * st, int n);
int main(int argc, char * argv[])
{
	char chf, chr;
	char filename[SLEN];
	FILE * fp;
	int count = 0, sum = 0;

	if (2 <= argc)
	{
		if (argv[1][1] != '\0')
		{
			printf("arguments error. Usage: %s character [filenames]\n", argv[0]);
			exit(EXIT_FAILURE);
		}
		chf = argv[1][0];
	}
	else
	{
		printf("Usage:%s character [filenames]\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if ( 2 == argc)
	{
		puts("Enter the first filename of file to read(empty to quit):");
		while (s_gets(filename, SLEN) && filename[0] != '\0')
		{
			count = 0;
			if ((fp = fopen(filename, "r")) == NULL)
			{
				printf("can not open file %s to read.\n", filename);
				puts("Please reenter the filename(empty to quit):");
				continue;
			}

			while ((chr = getc(fp)) != EOF)
				if (chf == chr)
					count++;

			fclose(fp);
			sum += count;
			printf("%d char %c finded in file %s, totally finded %d in all files.\n", \
					count, chf, filename, sum);
			puts("Enter the next file to read(empty to quit):");
		}

	}
	else
	{
		for (int i = 2; i < argc; i++)
		{
			count = 0;
			if ((fp = fopen(argv[i], "r")) == NULL)
			{
				printf("can not open file %s to read, skipped.\n", argv[i]);
				continue;
			}
			while ((chr = getc(fp)) != EOF)
				if (chf == chr)
					count ++;

			fclose(fp);
			sum += count;
			printf("%d char %c finded in file %s, totally finded %d in all files.\n", \
					count, chf, argv[i], sum);
		}
	}



	return 0;
}

char * s_gets(char * st, int n)
{
	char * ret_val;
	char * find;

	ret_val = fgets(st, n, stdin);
	if (ret_val)
	{
		find = strchr(st, '\n');
		if (find)
			*find = '\0';
		else
			while (getchar() != '\n')
				continue;
	}

	return ret_val;
}
