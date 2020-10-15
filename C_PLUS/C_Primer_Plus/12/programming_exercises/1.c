/*************************************************************************
  > File Name: 1.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Mon Sep 14 09:15:04 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
/* 1.  Rewrite the program in Listing 12.4 so that it does not use global variables. */
//int units = 0; /* an external variable */
int critic(void);
int main(void)
{
	int units; 
	printf("How many pounds to a firkin of butter?\n");
	scanf("%d", &units);
	while ( units != 56)
		units = critic();
	printf("You must have looked it up!\n");
	return 0;
}
int critic(void)
{
	int units;
	printf("No luck, my friend. Try again.\n");
	scanf("%d", &units);
	return units;
} 


