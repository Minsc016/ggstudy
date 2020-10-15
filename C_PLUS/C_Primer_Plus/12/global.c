/*************************************************************************
	> File Name: global.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Fri Sep  4 11:57:06 2020
 ************************************************************************/

#include<stdio.h>

int units = 0;		/* an external variable */
void critic(void);
int main(void)
{
	extern int units; /* an optional redeclaration */

	printf("How many pounds to a firkin of butter?\n");
	scanf("%d", &units);
	while ( units != 56)
		critic();
	printf("You must have looked it up!\n");

	return 0;
}

void critic(void)
{
	/* optional redeclaration omitted */
	printf("No luck, my friend. Try again.\n");
	scanf("%d", &units);
}
