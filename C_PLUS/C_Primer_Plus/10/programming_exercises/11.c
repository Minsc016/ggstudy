/*************************************************************************
  > File Name: 11.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Thu Sep  3 16:17:06 2020
 ************************************************************************/

#include<stdio.h>
//#define DEBUG

/*
 * Write a program that declares a 3×5 array of int and initializes it to some values of 
 * your choice. Have the program print the values, double all the values, and then display 
 * the new values. Write a function to do the displaying and a second function to do the 
 * doubling. Have the functions take the array name and the number of rows as arguments.
 *
 */

void doubar(int ar[][5], int n);
void display(int ar[][5], int n);

int main(void)
{
#ifdef DEBUG
	int n;
#endif
	int ar[3][5] = {
		{1,2,3,4,5},
		{5,4,3,2,1},
		{6,6,6,6,6}
	};
#ifdef DEBUG
	printf("%u %u\n",sizeof ar, sizeof n);
#endif

	display(ar, 3);
	doubar(ar, 3);
	display(ar, 3);

	return 0;
}

void doubar(int ar[][5], int n)
{
#ifdef DEBUG
	printf("%u %u\n",sizeof ar, sizeof n);
#endif
	int *p = ar[0];
	for (int i = 0; i < 5*n; i++, p++ )
		*p *= 2;

}

void display(int ar[][5], int n)
{
	for ( int i = 0; i < n; i++)
		for( int j = 0; j< 5; j++)
			printf("%d%c", *(*(ar+i)+j), " \n"[4==j]);
}
