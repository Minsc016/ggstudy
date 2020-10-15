/*************************************************************************
	> File Name: rand0.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep  7 14:26:40 2020
 ************************************************************************/

#include<stdio.h>

/* produces random number */
/* uses ANSI C portable algorithm */
static unsigned long int next = 1; /* the seed */

int rand0(void)
{
	/* magic formula to generate pseudorandom number */
	next = next * 1103515245 + 123456;
	return (unsigned int)(next/65536) % 32768;
}

