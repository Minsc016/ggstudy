/*************************************************************************
	> File Name: 7.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Fri Sep 25 11:37:13 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * 7.  a.   What is the difference between saving 8238201 by using 
 * fprintf() and saving it by using fwrite()? 
 * b.  What is the difference between saving the character S by using putc() and saving 
 * it by using fwrite()? 
 * */



/*
 * a. frpintf save number as character, fwrite save it as binary
 * b.same as above.
 *
 * 
 * ANS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 * a. When 8238201 is saved using fprintf(), it's saved as seven characters stored in 7 bytes.
 * When fwrite() is used, it's saved as a 4-byte integer using the binary representaion of that numberic value.
 *
 *
 *
 * b.  No difference; in each case it’s saved as a 1-byte binary code
 * ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::END ANS
 *
 *
 * *.
 *
 * */

int main(void)
{
	int n = 8238201;
	FILE * fpt;
	int nn;

	if ((fpt = fopen("7t.log", "w")) == NULL)
	{
		puts("Can not open file to write.\n");
		exit(EXIT_FAILURE);
	}
	fprintf(fpt, "%d\n", n);  // 7个数字 + 1个 \n 一共8个字符
	fwrite(&n, sizeof (int), 7, fpt);

	fclose(fpt);

	if ((fpt = fopen("7t.log", "r")) == NULL)
	{
		puts("Can't open file for reading.\n");
		exit(EXIT_FAILURE);
	}
	//while((fread(&nn, sizeof (int), 7, fpt) != EOF))
	fseek(fpt, 0L, SEEK_END);
	nn = ftell(fpt);
	printf("wc -c:[%d]\n", nn);
	fseek(fpt, 0L, SEEK_SET);
	fscanf(fpt, "%d", &nn);
	printf("nn:[%d]\n", nn);
	
	fseek(fpt, 8L, SEEK_SET); //  第一行的数字有个\n在.
	fread(&nn, sizeof (int), 7, fpt);
	printf("nn:[%d]\n", nn);

	fclose(fpt);

	return 0;
}
