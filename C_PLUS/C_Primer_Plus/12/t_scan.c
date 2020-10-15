/*************************************************************************
	> File Name: t_scan.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep 16 09:48:44 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>


int main(void)
{
	int foo,status;
	while (1)
	{
		printf("please enter any characters to test:");
		if ((status = scanf("%d", &foo)) != 1)
		{
			if (status == EOF)
				printf("status:[EOF]\n");
			else
			{
				printf("the input is not an integer and the status[%d].\n", status);
				while (getchar() != '\n')
					continue; /* dispose of bad input */

			}
		}
	}

	return 0;
}
