/*************************************************************************
	> File Name: 4.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 16:24:03 2020
 ************************************************************************/

#include<stdio.h>

int main(void)
{
	int * ptr;
	int torf[2][2] = {12,14,16};
	int fort[2][2] = { {12},{14,16} };

	ptr = torf[0];
	printf("%d %d\n", *ptr, *(ptr+2));

	ptr = fort[0];
	printf("%d %d\n", *ptr, *(ptr+2));

	printf("%d\n", *(ptr+1));
	return 0;
}
