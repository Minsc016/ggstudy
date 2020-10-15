/*************************************************************************
	> File Name: dyn_arr.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  9 10:36:57 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void)
{
	double * ptd;
	int max = 0;
	int number;
	int i = 0;

	puts("What is the maximum number of type double enteries?");
	if(scanf("%d", &max) != 1)
	{
		puts("Number not correctly entered -- bye.");
		exit(EXIT_FAILURE);
	}
	ptd = (double *) malloc(max * sizeof (double));
	if (ptd == NULL)
	{
		puts("Memory allocation failed.Goodbye.");
		exit(EXIT_FAILURE);
	}
	/* ptd now pointes to an array of max elements */
	puts("Enter the values (q to quit):");
	while (i < max && scanf("%lf",&ptd[i]) == 1)
		++i;
	printf("Here are your %d enteries:\n", number = i);
	for (i = 0; i < number; i++)
	{
		printf("%7.2f ", ptd[i]);
		if (i % 7 == 6)
			putchar('\n');
	}
	if (i % 7 != 0)
		putchar('\n');
	puts("Done.");
	free(ptd);

	return 0;
}
