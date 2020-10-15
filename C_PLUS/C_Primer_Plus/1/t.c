/*************************************************************************
	> File Name: t.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Sat Oct 10 17:20:23 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int main(void)
{
	FILE * fp;
	int fuck;
	if ((fp = fopen("tt", "a+")) == NULL)
		exit(EXIT_FAILURE);

	fseek(fp, -sizeof(int), SEEK_END);
	printf("fuck\n");
	if (fscanf(fp, "%d", &fuck) == 1 )
		printf("%d\n", fuck);

	fclose(fp);

	return 0;
}
