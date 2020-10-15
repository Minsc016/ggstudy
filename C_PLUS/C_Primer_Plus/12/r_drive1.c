/*************************************************************************
	> File Name: r_drive1.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep  7 15:04:28 2020
 ************************************************************************/

#include<stdio.h>

/* r_drive1.c -- test rand1() and srand1() */
/* compile with s_and_r.c */

extern void srand1(unsigned int x);
extern int rand1(void);

int main(void)
{
	int count;
	unsigned seed;

	printf("Please enter your choice for seed.\n");
	while (scanf("%u",&seed) == 1)
	{
		srand1(seed);		/* reset seed */
		for (count = 0; count < 5; count++)
			printf("%d\n", rand1());
		printf("Please enter next seed(q to quit):\n");
	}
	printf("Done\n");

	return 0;
}

/*
 * time
 * #include<time.h>
 * srand1((unsigned int)time(0));  initialize seed 
*/



