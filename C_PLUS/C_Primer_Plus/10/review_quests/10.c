/*************************************************************************
  > File Name: 10.c
  > Author: Minsc
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep  2 17:52:22 2020
 ************************************************************************/

#include<stdio.h>

int main()
{
	float rootbeer[10], things[10][5], *pf, value = 2.2;
	int i = 3;

	/*
	 * a.  rootbeer[2] = value;
	 * b.  scanf("%f", &rootbeer );
	 * c.  rootbeer = value;
	 * d.  printf("%f", rootbeer);
	 * e.  things[4][4] = rootbeer[3];
	 * f.   things[5] = rootbeer;
	 * g.  pf = value;
	 * h.  pf = rootbeer;
	 * */

	/*
	 * v
	 * n
	 * n
	 * v-n ************************n is not a float
	 * v
	 * n
	 * v
	 * v *********************** n!!!! pf = &value;
	 * */








	return 0;
}
