/*************************************************************************
	> File Name: t.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Sat Oct 10 11:30:26 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int main(void)
{

	char * file = "2030";
	FILE * fp;
	int num;
	if ((fp = fopen(file, "r")) == NULL )
	{
		printf("error.\n");
		exit(EXIT_FAILURE);
	}
	for(int i = 0; i < 20; i++)
		for (int j = 0; j < 30; j++)
		{
			fscanf(fp, "%d", &num);
			printf("num read:[%d]\n", num);
		}

	return 0;
}
