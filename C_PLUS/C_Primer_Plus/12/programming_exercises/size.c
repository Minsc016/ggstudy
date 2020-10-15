/*************************************************************************
	> File Name: size.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 16 11:23:58 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>


int main(void)
{
	char tmp[100];
	scanf("%s", tmp);
	printf("size of tmp:[%u]\nstrlen of tmp:[%d]\n", sizeof tmp, strlen(tmp));

	return 0;
}
