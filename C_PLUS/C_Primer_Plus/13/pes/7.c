/*************************************************************************
	> File Name: 7.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 30 16:46:52 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * 7.  Write a program that opens two files. You can obtain the filenames either by using 
 * command-line arguments or by soliciting the user to enter them. 
 * a.  Have the program print line 1 of the first file, line 1 of the second file, line 2 of the 
 * first file, line 2 of the second file, and so on, until the last line of the longer file (in 
 * terms of lines) is printed. 
 * b.  Modify the program so that lines with the same line number are printed on the 
 * same line.  
 *
 * */


int main(int argc, char * argv[])
{
	char filename1[81];
	char filename2[81];
	FILE *fp1, *fp2;
	char buffer1[256],buffer2[256];

	char ch;
	int ob_flag = 1;



	if (3 == argc)
	{
		strcpy(filename1, argv[1]);
		strcpy(filename2, argv[2]);
		printf("filename %s and %s obtained by argv.\n", filename1, filename2);
	}
	else if (1 == argc)
	{
		printf("Enter the name of first file:");
		if (scanf("%s", &filename1) == 1 && filename1[0] != '\0')
			printf("\nfilename %s entered.\n", filename1);
		else
			exit(EXIT_FAILURE);
		printf("Enter the name of second file:");
		if (scanf("%s", &filename2) == 1 && filename2[0] != '\0')
			printf("\nfilename %s entered.\n", filename2);
		else
			exit(EXIT_FAILURE);

	}
	else
	{
		printf("Usage:%s [filename1 filename2]\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if ((fp1 = fopen(filename1, "r")) == NULL || (fp2 = fopen(filename2, "r")) == NULL)
	{
		printf("can not open file %s or %s to read.\n", filename1, filename2);
		exit(EXIT_FAILURE);
	}


	// print   getc
	while ( ob_flag )
	{
		if ( 1 == ob_flag )
		{
			ch = getc(fp1);
			if ('\n' == ch || EOF == ch)
				ob_flag = 2;
			else
				putchar(ch);
			
		}

		if ( 2 == ob_flag )
		{
			ch = getc(fp2);
			if ('\n' == ch)
				ob_flag = 1;
			if (EOF == ch)
				ob_flag = 0;
			else
				putchar(ch);

		}
	}
	fclose(fp1);
	fclose(fp2);


	return 0;
}
