/*************************************************************************
	> File Name: s_and_r.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep  7 15:01:19 2020
 ************************************************************************/

#include<stdio.h>

/* file for rand() and srand() */
/* use ANSI C protable algorithm */

static unsigned long int next = 1; /* the seeed */
int rand1(void)
{
	/* magic formula to generate pseudorandom number */
	next = next * 1103515245 + 12345;
	return (unsigned int)(next/65536) % 32768;
}

void srand1(unsigned int seed)
{
	next = seed;
}

	
