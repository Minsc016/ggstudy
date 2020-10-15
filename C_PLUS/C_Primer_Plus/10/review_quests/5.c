/*************************************************************************
	> File Name: 5.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 16:27:43 2020
 ************************************************************************/

#include<stdio.h>

int main(void)
{
	int (*ptr)[2];
	int torf[2][2] = {12, 14, 16};
	int fort[2][2] = { {12}, {14,16} };
	ptr = torf; 
	// **ptr **(ptr+1)
	printf("%d %d\n", **ptr, **(ptr+1));
	
	ptr = fort; 
	printf("%d %d\n", **ptr, **(ptr+1));

	return 0;
}
