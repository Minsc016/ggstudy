/*************************************************************************
  > File Name: 13.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Sat Oct 10 15:29:57 2020
 ************************************************************************/

/* 13.  Do Programming Exercise 12, but use variable-length arrays (VLAs) instead of standard arrays
 * */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/* copy of pe 12 */
char corresponding(int );
int main()
{
	int rows = 20, cols = 30;
	int ints[rows][cols];
	char chars[rows][cols+1];

	FILE * fpr, *fpw;
	int * pi = &ints[0][0];
	char * pc = &chars[0][0];

	if ((fpr = fopen("2030", "r")) == NULL)
	{
		printf("can't open file %s to read\n", "2030");
		exit(EXIT_FAILURE);
	}
	if ((fpw = fopen("2030result", "w")) == NULL)
	{
		printf("can't open file %s to write.\n", "2030result");
		exit(EXIT_FAILURE);
	}

	for(int i = 0; i < rows; i++)
	{
		for(int j = 0; j < cols; j++)
		{
			if (fscanf(fpr, "%d", &ints[i][j]) == 1)
			{
				chars[i][j] = corresponding(ints[i][j]);
			}
		}
		chars[i][cols] = '\n';
	}

	for(int i = 0; i < rows; i++)
		for(int j = 0; j < cols+1; j++)
			fprintf(stdout, "%c", *(*(chars+i)+j));

	fclose(fpr);
	fclose(fpw);
	return 0;
}
char corresponding(int i)
{
	char ch;
	switch(i)
	{
		case 0:
			ch = ' ';
			break;
		case 1:
			ch = '.';
			break;
		case 2:
			ch = '\'';
			break;
		case 3:
			ch = ':';
			break;
		case 4:
			ch = '~';
			break;
		case 5:
			ch = '*';
			break;
		case 6:
			ch = '=';
			break;
		case 7:
			ch = '-';
			break;
		case 8:
			ch = '%';
			break;
		case 9:
			ch = '#';
			break;
		default:
			printf("got integer:%d convertint to char %c.\n", i, ch);
			break;
	}

	return ch;
}

