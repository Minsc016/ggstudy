/*************************************************************************
  > File Name: 14.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Sat Oct 10 15:34:17 2020
 ************************************************************************/
/*
 * 14.  Digital images, particularly those radioed back from spacecraft, may have glitches. Add a de-glitching function to programming exercise 12. 
 * It should compare each value to its immediate neighbors to the left and right, above and below. If the value differs by more than 1 from each of its neighbors, 
 * replace the value with the average of the neighboring values. 
 * You should round the average to the nearest integer value. 
 * Note that the points along the boundaries have fewer than four neighbors, so they require special handling.  
 * */


#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#include<math.h>

void degliching(int row, int col, int array[row][col]);
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
				//chars[i][j] = corresponding(ints[i][j]);
				printf("%d ", ints[i][j]);
			}
		}
		//		chars[i][cols] = '\n';
		printf("\n");
	}
	printf("\n\n");
	degliching(rows, cols, ints);
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			printf("%d ", ints[i][j]);
			chars[i][j] = corresponding(ints[i][j]);
		}
		printf("\n");
		chars[i][cols] = '\n';
	}

	printf("\n\n");

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

void degliching(int row, int col, int array[row][col])
{
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			if (0 == i)
			{
				if(0 == j)
				{
					if (abs(array[i][j] - array[i][j+1]) > 1 && abs(array[i][j] - array[i+1][j]) > 1 )
						array[i][j] = round((array[i][j+1] + array[i+1][j]) / 2);
				}
				else if (col -1 == j)
				{
					if (abs(array[i][j] - array[i][j-1]) >1 && abs(array[i][j] - array[i+1][j]) > 1)
						array[i][j] = round((array[i][j-1] + array[i+1][j]) / 2);
				}
				else
				{
					if (abs(array[i][j] - array[i+1][j]) > 1 && abs(array[i][j] - array[i][j-1]) > 1 && abs(array[i][j] - array[i][j+1]) > 1)
						array[i][j] = round((array[i+1][j] + array[i][j-1] + array[i][j+1]) / 3);
				}
			}
			else if (row -1 == i)
			{
				if(0 == j)
				{
					if (abs(array[i][j] - array[i][j+1]) > 1 && abs(array[i][j] - array[i-1][j]) > 1 )
						array[i][j] = round((array[i][j+1] + array[i-1][j]) / 2);
				}
				else if (col -1 == j)
				{
					if (abs(array[i][j] - array[i][j-1]) >1 && abs(array[i][j] - array[i-1][j]) > 1)
						array[i][j] = round((array[i][j-1] + array[i-1][j]) / 2);
				}
				else
				{
					if (abs(array[i][j] - array[i-1][j]) > 1 && abs(array[i][j] - array[i][j-1]) > 1 && abs(array[i][j] - array[i][j+1]) > 1)
						array[i][j] = round((array[i-1][j] + array[i][j-1] + array[i][j+1]) / 3);
				}

			}
			else if (0 == j)
			{
				if (abs(array[i][j] - array[i][j+1]) > 1 && abs(array[i][j] - array[i-1][j]) > 1 && abs(array[i][j] - array[i+1][j]) > 1)
					array[i][j] = round((array[i][j+1] + array[i-1][j] + array[i+1][j]) / 3);
			}
			else if (col - 1 == j)
			{
				if (abs(array[i][j] - array[i][j-1]) > 1 && abs(array[i][j] - array[i-1][j]) > 1 && abs(array[i][j] - array[i+1][j]) > 1)
					array[i][j] = round((array[i][j-1] + array[i-1][j] + array[i+1][j]) / 3);
			}
			else
				if ( abs(array[i][j] - array[i][j-1]) > 1 && abs(array[i][j] - array[i][j+1]) > 1 && abs(array[i][j] - array[i-1][j]) > 1 && abs(array[i][j] - array[i+1][j]) > 1)
					array[i][j] = round((array[i][j-1] + array[i][j+1] + array[i-1][j] + array[i+1][j]) / 4);

		}
	}
}

