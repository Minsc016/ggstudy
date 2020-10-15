/*************************************************************************
	> File Name: partb.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep  7 11:08:50 2020
 ************************************************************************/

#include<stdio.h>
//partb.c -- rest of the program
//compile with parta.c

extern int count;		//reference declaration, external linkage

static int total = 0;		//static definition, internal linkage
void accumulate(int k);		//prototype

void accumulate(int k)		//k has block scope, no linkage
{
	static int subtotal = 0;		//static, no linkage
	if (k < 0)
	{
		printf("loop cycle: %d\n", count);
		printf("subtotal:%d;total;%d\n", subtotal, total);
		subtotal = 0;
	}
	else
	{
		subtotal += k;
		total += k;
	}
}
