/*************************************************************************
	> File Name: pe8b.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 16 10:04:13 2020
 ************************************************************************/


#include "pe8.h"
int * make_array(int elem, int val)
{
	int * ar = (int *) malloc(elem * sizeof(int));
	for (int i = 0; i < elem; i++)
		ar[i] = val;
	return ar;
}

void show_array(const int ar[], int n)
{
	for (int i = 0; i < n; i++)
		printf("%d%c", ar[i], " \n"[(0 == (i+1)%8) || (n-1) == i] );
}
