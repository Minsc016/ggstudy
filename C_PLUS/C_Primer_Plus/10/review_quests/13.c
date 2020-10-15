/*************************************************************************
	> File Name: 13.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 20:06:50 2020
 ************************************************************************/

#include<stdio.h>

/* Q
 * Here are two function prototypes: 
 * void show(const double ar[], int n); // n is number of elements
 * void show2(const double ar2[][3], int n); // n is number of rows 
 * a.  Show a function call that passes a compound literal containing the values 8 , 3 , 9, 
 * and 2 to the show() function. 
 * b.  Show a function call that passes a compound literal containing the values 8 , 3, 
 * and 9 as the first row and the values 5 , 4 , and 1 as the second row to the show2()
 * function. 
 */

void show(const double ar[], int n); // n is number of elements
void show2(const double ar2[][3], int n); // n is number of rows

int main(void)
{

	show((double []){ 1,2,3,4,5,6,7,8,9,10 }, 10);
	show2((double [][3]){ {1,2,3},{4,5,6},{7,8,9} }, 3);

}

void show(const double ar[], int n)
{
	for (int i = 0; i < n; i++)
		printf("%.0lf%c", ar[i], "+\n"[n-1==i]);
}

void show2(const double ar2[][3], int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < 3; j++)
			printf("%.0lf%c", ar2[i][j], "-\n"[j==2]);
}

