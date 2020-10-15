/*************************************************************************
	> File Name: 10.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Thu Sep  3 16:11:04 2020
 ************************************************************************/

#include<stdio.h>

/*
 * Write a function that sets each element in an array to the sum of the corresponding 
 * elements in two other arrays. 
 * That is, if array 1 has the values 2 , 4 , 5 , and 8 
 * and array 2 has the values 1 , 0 , 4 , and 6 , 
 * the function assigns array 3 the values 3 , 4 , 9 , and 14 . 
 * The function should take three array names and an array size as arguments. 
 * Test the function in a simple program. 
 * */

void sumar(const int ar1[], const int ar2[], int ss[], int n);

int main(void)
{
	int foo[4] = {2,4,5,8};
	int bar[4] = {1,0,4,6};
	int baz[4];

	sumar(foo, bar, baz, 4);
	for(int i = 0; i < 4; i++)
		printf("%d%c", baz[i], " \n"[i==3]);
	return 0;
}

void sumar(const int ar1[], const int ar2[], int ss[], int n)
{
	for (int i = 0;i < n; i++)
		ss[i] = ar1[i] + ar2[i];
}
