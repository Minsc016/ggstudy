/*************************************************************************
	> File Name: 12.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Sat Oct 10 12:18:44 2020
 ************************************************************************/

/*
 * 12.  Create a text file consisting of 20 rows of 30 integers. 
 * The integers should be in the range 0–9 and be separated by spaces. 
 * The file is a digital representation of a picture, 
 * with the values 0 through 9 representing increasing levels of darkness. 
 *
 * Write a program that reads the contents of the file into a 20-by-30 array of ints. 
 * In a crude approach toward converting this digital representation to a picture, 
 * have the program use the values in this array to initialize a 20-by-31 array of char s, with a 0 value corresponding to a space character, a 1 value to the period character, and so on, with each larger number represented by a character that occupies more space. 
 * For example, you might use # to represent 9. 
 * The last character (the 31st) in each row should be a null character, making it an array of 20 strings. 
 * Have the program display the resulting picture (that is, print the strings) and also store the result in a text file. 
 *
 * For example, suppose you start with this 
 * data: 
 * 0 0 9 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 2 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 9 0 0 0 0 0 0 0 5 8 9 9 8 5 5 2 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 1 9 8 5 4 5 2 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 9 0 0 0 0 0 0 0 5 8 9 9 8 5 0 4 5 2 0 0 0 0 0 0 0 0
 * 0 0 9 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 0 0 4 5 2 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 9 1 8 5 0 0 0 4 5 2 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 0 0 0 0 4 5 2 0 0 0 0 0
 * 5 5 5 5 5 5 5 5 5 5 5 5 5 8 9 9 8 5 5 5 5 5 5 5 5 5 5 5 5 5
 * 8 8 8 8 8 8 8 8 8 8 8 8 5 8 9 9 8 5 8 8 8 8 8 8 8 8 8 8 8 8
 * 9 9 9 9 0 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 3 9 9 9 9 9 9 9
 * 8 8 8 8 8 8 8 8 8 8 8 8 5 8 9 9 8 5 8 8 8 8 8 8 8 8 8 8 8 8
 * 5 5 5 5 5 5 5 5 5 5 5 5 5 8 9 9 8 5 5 5 5 5 5 5 5 5 5 5 5 5
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 0 0 0 0 6 6 0 0 0 0 0 0
 * 0 0 0 0 2 2 0 0 0 0 0 0 5 8 9 9 8 5 0 0 5 6 0 0 6 5 0 0 0 0
 * 0 0 0 0 3 3 0 0 0 0 0 0 5 8 9 9 8 5 0 5 6 1 1 1 1 6 5 0 0 0
 * 0 0 0 0 4 4 0 0 0 0 0 0 5 8 9 9 8 5 0 0 5 6 0 0 6 5 0 0 0 0
 * 0 0 0 0 5 5 0 0 0 0 0 0 5 8 9 9 8 5 0 0 0 0 6 6 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 5 8 9 9 8 5 0 0 0 0 0 0 0 0 0 0 0 0 
 * For one particular choice of output characters, the output looks like this: 
 * # *%##%*'
 * # *%##%**'
 * *%.#%*~*'
 * # *%##%* ~*'
 * # *%##%* ~*'
 * *%#.%* ~*'
 * *%##%* ~*'
 * *************%##%*************
 * %%%%%%%%%%%%*%##%*%%%%%%%%%%%%
 * #### #################:#######
 * %%%%%%%%%%%%*%##%*%%%%%%%%%%%%
 * *************%##%*************
 * *%##%*
 * *%##%* ==
 * '' *%##%* *= =*
 * :: *%##%* *=....=*
 * ~~ *%##%* *= =*
 * ** *%##%* ==
 * *%##%*
 * *%##%* 
 *
 * */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
char corresponding(int );
int main()
{
	int ints[20][30];
	char chars[20][31];
	
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

	for(int i = 0; i < 20; i++)
	{
		for(int j = 0; j < 30; j++)
		{
			if (fscanf(fpr, "%d", &ints[i][j]) == 1)
			{
				chars[i][j] = corresponding(ints[i][j]);
			}
		}
		chars[i][30] = '\n';
	}
	
	for(int i = 0; i < 20; i++)
		for(int j = 0; j < 31; j++)
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

