/*************************************************************************
	> File Name: zippo1.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep  1 11:13:46 2020
 ************************************************************************/

#include<stdio.h>
int main(void)
{
	int zippo[4][2] = { {2,4}, {6,8}, {1,3}, {5,7} };
	printf("zippo = %p,\tzippo + 1 = %p\n", zippo, zippo + 1);
	printf("zippo[0] = %p,\tzippo[0] + 1 = %p\n",zippo[0], zippo[0] + 1);

	printf("*zippo = %p,\t*zippo + 1 = %p\n", *zippo, *zippo + 1);
	printf("zippo[0][0] = %d,\t", zippo[0][0]);
	printf("**zippo = %d\n", **zippo);

	printf("zippo[2][1] = %d,\t*(*(zippo+2)+1) = %d\n", zippo[2][1],*(*(zippo+2)+1));

	return 0;
}
