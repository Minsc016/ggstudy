/*************************************************************************
	> File Name: 7.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 16:35:57 2020
 ************************************************************************/

#include<stdio.h>

/*
 *  Create an appropriate declaration for each of the following variables: 
 *  a.  digits is an array of 10 ints. 
 *  b.  rates is an array of six floats. 
 *  c.  mat is an array of three arrays of five integers. 
 *  d.  psa is an array of 20 pointers to char. 
 *  e.  pstr is a pointer to an array of 20 chars. 
*/

	int digits[10];
	float rates[6];
	int mat[3][5];
	//
	char * psa[20];
	char (*pstr)[20];
	//
int main(void)
{
	int torf[2][2] = { {1,2}, {3,4} };
	int * pt[2];		// a array of 2 pointers
	int (*pd)[2];		// a pointer point to an array with 2 ints

	pd = torf;

	printf("%p %p", pt, pd);






	return 0;
}
