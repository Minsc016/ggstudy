/*************************************************************************
	> File Name: 12.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 19:42:25 2020
 ************************************************************************/

#include<stdio.h>

void tr_p(int n, double tr[]);
void cl_p(int rs, int cs, short cl[][cs]);
void sh_p(int ls, int rs, int cs, long sh[][rs][cs]);

int main()
{
	double trots[20] = {};
	short clops[10][30] = {};
	long shots[5][10][15] = {};

	/*
	a.  Show a function prototype and a function call for a traditional void function that 
		processes trots and also for a C function using a VLA. 
		b.  Show a function prototype and a function call for a traditional void function that 
		processes clops and also for a C function using a VLA. 
		c.  Show a function prototype and a function call for a traditional void function that 
		processes shots and also for a C function using a VLA.
	*/

	tr_p(20, trots);
	cl_p(10,30,clops);
	sh_p(5,10,15,shots);


	return 0;
}

void tr_p(int n, double tr[])
{
	for (int i = 0; i < n; i++)
		printf("%.0f%c",tr[i]," \n"[i==n-1]);

}

void cl_p(int rs, int cs, short cl[][cs])
{
	for (int i = 0; i < rs; i++)
		for (int j = 0; j < cs; j++)
			printf("%d%c", cl[i][j], ",\n"[cs-1 == j]);
}

void sh_p(int ls, int rs, int cs, long sh[][rs][cs])
{
	for (int i = 0; i < ls; i++)
	{
		for(int j = 0; j < rs; j++)
			for(int k = 0; k < cs; k++)
				printf("%d%c", sh[i][j][k], "^\n"[cs-1 == k]);
		printf("--------------------------------\n");
	}
}

/* ANS
 * a. 
 * void process(double ar[], int n);
 * void processvla(int n, double ar[n]);
 * process(trots, 20);
 * processvla(20, trots); 
 * b. 
 * void process2(short ar2[30], int n);
 * void process2vla(int n, int m, short ar2[n][m]);
 * process2(clops, 10);
 * process2vla(10, 30, clops); 
 * c. 
 * void process3(long ar3[10][15], int n);
 * void process3vla(int n, int m,int k, long ar3[n][m][k]);
 * process3(shots, 5);
 * process3vla(5, 10, 15, shots); 
 * */
