/*************************************************************************
  > File Name: 12.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Thu Sep  3 16:49:10 2020
 ************************************************************************/

#include<stdio.h>
/*
 * Rewrite the rain program in Listing 10.7 so that the main tasks are performed by 
 * functions instead of in main(). 
 */

#define MONTHS 12 // number of months in a year
#define YEARS 5 // number of years of data

void cal(const float rain[][MONTHS]);
void ava(const float rain[][MONTHS]);
int main(void)
{
	// initializing rainfall data for 2010 - 2014
	const float rain[YEARS][MONTHS] =
	{
		{4.3,4.3,4.3,3.0,2.0,1.2,0.2,0.2,0.4,2.4,3.5,6.6},
		{8.5,8.2,1.2,1.6,2.4,0.0,5.2,0.9,0.3,0.9,1.4,7.3},
		{9.1,8.5,6.7,4.3,2.1,0.8,0.2,0.2,1.1,2.3,6.1,8.4},
		{7.2,9.9,8.4,3.3,1.2,0.8,0.4,0.0,0.6,1.7,4.3,6.2},
		{7.6,5.6,3.8,2.8,3.8,0.2,0.0,0.0,0.0,1.3,2.6,5.2}
	};

	cal( rain );
	ava(rain);
	return 0;
} 

void cal(const float rain[][MONTHS])
{
	float subtot, total;
	const float * pf = &rain[0][0];
	const float (*p_year)[MONTHS] = rain;
	printf("YEAR\t\tRAINFALL(inches)\n");
	int i = 0, j = 0;
	for(i = 0, total = 0; i < YEARS; i++ )	
	{
		for (j = 0, subtot = 0; j < MONTHS; j++, pf++)
			subtot += (*pf);
		total += subtot;
		printf("%d\t\t%.1f\n", 2010 + i, subtot);
	}
	printf("\nThe yearly average is %.1f inches.\n\n",
			total/YEARS);

}
void ava(const float rain[][MONTHS])
{
	float subtot;
	int i = 0, j = 0;
	const float (*p_year)[MONTHS] = rain;
	printf("MONTHLY AVERAGES:\n\n");
	printf(" Jan Feb Mar Apr May Jun Jul Aug Sep Oct ");
	printf(" Nov Dec\n");
	for(i = 0, p_year = rain; i < MONTHS; i++)
	{
		for(j = 0, subtot = 0; j < YEARS; j++)
			//subtot += *p_year[i];
			subtot += *((*(p_year+j)) + i);
		printf("%.2lf ", subtot/YEARS);
	}
}
