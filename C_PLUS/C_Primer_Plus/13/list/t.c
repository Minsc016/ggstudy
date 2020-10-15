/*************************************************************************
	> File Name: t.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep 21 11:13:04 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int main(void)
{
	FILE * fp;
	char * file = "test";
	long last, count, loc;
	char ch;

	if ((fp = fopen(file,"rb")) == NULL)
	{
		printf("can not open file %s\n", file);
		exit(EXIT_FAILURE);
	}
	/*
	fseek(fp, 0L, SEEK_END);
	last = ftell(fp);
	ch = getc(fp);
	printf("last:[%ld]\t", last);
	printf("ch:[%c]\n", ch);
	*/

/*
	for (count = 0L; count <= last; count++)
	{
		fseek(fp, count, SEEK_SET);
		ch = getc(fp);
		printf("location[%ld],charater[%c]\n", count, ch);
	}
*/	
/*
	fpos_t * pos;
	fgetpos(fp, pos);
	last = ftell(fp);
	ch = getc(fp);
	printf("[%ld],[%c]\n", last, ch);
	fsetpos(fp, pos);
	last = ftell(fp);
	ch = getc(fp);
	printf("[%ld],[%c]\n", last, ch);
	fsetpos(fp, pos);
*/

	fseek(fp, 0L, SEEK_SET);
	loc = ftell(fp);
	ch = getc(fp);
	printf("[%ld]:[%c]\n", loc, ch);
	ungetc('o', fp);
	loc = ftell(fp);
	printf("[%ld]:[%c]\n", loc, ch);
	ch = getc(fp);
	loc = ftell(fp);
	printf("[%ld]:[%c]\n", loc, ch);

	printf("\n");
	fclose(fp);
	return 0;
}
