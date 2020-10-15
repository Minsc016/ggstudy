/*************************************************************************
	> File Name: zippo2.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep  1 12:05:14 2020
 ************************************************************************/

#include<stdio.h>

int main(void)
{
	int zippo[4][2] = { {2,4}, {6,8}, {1,3}, {5,7} };
	int (*pz)[2];
	pz = zippo;

	printf("pz = %p,\tpz + 1 = %p\n", pz, pz + 1);
	printf("pz[0] = %p,\tpz[0] + 1 = %p\n", pz[0], pz[0] + 1);
	printf("*pz=%p,\t*pz + 1 = %p\n", *pz, *pz + 1);
	
	printf("pz[0][0] = %d\t,**pz = %d\n", pz[0][0], *pz[0]);
	printf("pz[2][1] = %d,\t*(*(pz+2) + 1) = %d\n", pz[2][1], *(*(pz+2)+1));

	return 0;
}
