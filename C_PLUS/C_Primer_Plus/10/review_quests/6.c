/*************************************************************************
	> File Name: 6.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 16:31:34 2020
 ************************************************************************/
#include<stdio.h>
int main(void)
{
	int grid[30][100];
//		a.  Express the address of grid[22][56] one way. 
//		b.  Express the address of grid[22][0] two ways. 
//		c.  Express the address of grid[0][0] three ways. 
	printf("%p\n", &grid[22][56]);
	printf("%p %p\n",&grid[22][0], grid+22);
	printf("%p %p %p\n", grid, grid[0], &grid[0][0]);
	printf("%p\n", &grid[0]);
	return 0;
}
