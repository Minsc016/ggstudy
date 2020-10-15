/*************************************************************************
	> File Name: 9.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 15:56:03 2020
 ************************************************************************/

#include<stdio.h>

/*
 * Write a program that initializes a two-dimensional 3×5 array-of- double and uses a VLA
 * based function to copy it to a second two-dimensional array. Also provide a VLA-based
 * function to display the contents of the two arrays. The two functions should be capable 
 * in general, of processing arbitrary N×M arrays. 
 * (If you don’t have access to a VLA-capable compiler, use the traditional C approach of functions that can process an N×5 array).
 */
#define ROWS 3
#define COLS 5
void cpar(int rs, int cs, const double arr[][cs], double cpr[][cs]);
void show(int rs, int cs, const double arr[][cs]);
int main(void)
{
	double foo[ROWS][COLS] = {
		{1,2,3,4,5},
		{6,7,8,9,10},
		{11,12,13,14,15}
	};
	double bar[ROWS][COLS];

	cpar(ROWS, COLS, foo, bar);
	show(ROWS, COLS, foo);
	show(ROWS, COLS, bar);

	return 0;

}

void cpar(int rs, int cs, const double arr[][cs], double cpr[][cs])
{
	for(int i = 0; i < rs; i++)
		for(int j = 0; j < cs; j++)
			cpr[i][j] = arr[i][j];
}

void show(int rs, int cs, const double arr[][cs])
{
	for(int i = 0; i < rs; i++)
		for(int j = 0; j < cs; j++)
			printf("%.0lf%c", arr[i][j], " \n"[j == cs-1]);
}
