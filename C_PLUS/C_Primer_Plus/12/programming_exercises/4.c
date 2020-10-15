/*************************************************************************
	> File Name: 4.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep 14 19:57:53 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * Write and test in a loop a function that returns the number of times it has been called. 
 * */

int count = 0;

int func_count();

int main(void)
{
	int randn;

	srand((unsigned int)time(0));
	randn = rand() % 100 + 1;


	for (int i = 0; i < randn; i++)
		func_count();

	printf("func_count has been called \033[31;1m%d\033[0m times. \
			And the rand int num is \033[32;1m%d\033[0m.\n", \
			count, randn);

	return 0;
}

int func_count()
{
	count ++;
}

