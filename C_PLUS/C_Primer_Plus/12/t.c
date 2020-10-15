/*************************************************************************
	> File Name: t.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  9 09:15:08 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int fuck = 666;
void foo(void);
int main(void)
{
	extern int fuck;
	double * ptd;
	int n = 10;
	int * mai = (int *) malloc(10 * sizeof(int));
	int * cai = (int *) calloc(10, sizeof(int));
	ptd = (double *) malloc(n * sizeof(double)); 
	double * ptdc = (double *) calloc(n, sizeof(double));



	for(int i = 0; i < 10; i++)
		printf("%d%c", mai[i], " \n"[i==9]);
	for(int i = 0; i < 10; i++)
		printf("%d%c", cai[i], " \n"[i==9]);
	for(int i = 0; i < 10; i++)
		printf("%lf%c", ptd[i], " \n"[i==9]);
	for(int i = 0; i < 10; i++)
		printf("%lf%c", ptdc[i], " \n"[i==9]);

	printf("fuck:%d\n", fuck);

	foo();
	extern int six;
// 	printf("six:%d\n",six); 

	free(mai);
	free(cai);
	free(ptd);
	return 0;
}
void foo()
{
	static int six = 666;
	printf("six::::%d\n",six);
}
