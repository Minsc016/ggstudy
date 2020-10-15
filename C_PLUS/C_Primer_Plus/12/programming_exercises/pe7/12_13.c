/*************************************************************************
  > File Name: 7.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Mon Sep 14 20:48:47 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * Write a program that behaves like the modification of Listing 12.13 , which we discussed 
 * after showing the output of Listing 12.13 . That is, have the program produce output like 
 * the following: 
 * Enter the number of sets; enter q to stop : 18 
 * How many sides and how many dice? 6 3 
 * Here are 18 sets of 3 6-sided throws.
 * 12 10 6 9 8 14 8 15 9 14 12 17 11 7 10
 * 13 8 14
 * How many sets? Enter q to stop: q 
 *
 * */

/* copy 12.13 */
/* manydice.c -- multiple dice rolls */
/* compile with diceroll.c */
#include <stdio.h>
#include <stdlib.h> /* for library srand() */
#include <time.h> /* for time() */
#include "12_12.h" /* for roll_n_dice() */
/* and for roll_count */
int main(void)
{
	int dice,roll;
	int sides;
	int sets;
	srand((unsigned int) time(0)); /* randomize seed */

	printf("Enter the number of sets; enter q to stop:");
	while (scanf("%d", &sets) == 1 && sets > 0)
	{
		printf("How many sides and how many dice?");
		if (scanf("%d %d", &sides, &dice) == 2 && sides > 0 && dice > 0)
		{
			printf("Here are %d sets of %d %d-sided throws.\n", sets, dice, sides);
			for (int i = 0; i < sets; i++)
			{
				roll = roll_n_dice(dice, sides);
				printf("%d%c", roll_n_dice(dice,sides), " \n"[(i+1)%dice==0]);
			}
		}
		else
			printf("please check the input out.\n");
		printf("\nhow many sets?Enter q to stop:");
	}

	return 0;
}
