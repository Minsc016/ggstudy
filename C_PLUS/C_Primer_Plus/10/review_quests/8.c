/*************************************************************************
  > File Name: 8.c
  > Author: Minsc
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep  2 16:52:04 2020
 ************************************************************************/

#include<stdio.h>
/*
 * a.  Declare an array of six int s and initialize it to the values 1 , 2 , 4 , 8 , 16 , and 32. 
 * b.  Use array notation to represent the third element (the one with the value 4 ) of the 
 * array in part a. 
 * c.  Assuming C99/C11 rules are in effect, declare an array of 100 int s and initialize it 
 * so that the last element is -1 ; don’t worry about the other elements. 
 * d.  Assuming C99/C11 rules are in effect, declare an array of 100 int s and initialize 
 * it so that elements 5, 10, 11, 12, and 3 are 101 ; don’t worry about the other 
 * elements. 
 * */
int main(void)
{
	int ar[6] = {1,2,4,8,16,32};			 //a
	int lots[100] = { [99] = -1 };			//c
	int pots[100] = { [5] = 101,[10] = 101, [11] = 101, [12] = 101, [3] = 101 };
	int pid[5] = { 5,10,11,12,3 };

	printf("%d\n", ar[2]);					//b

	printf("%d\n",lots[99]);

	for (int i = 0; i < 5; i++)
		printf("%d%c", pots[pid[i]], ",\n"[i==4]);

	return 0;
}

/* ANS
 * a.  int sextet[6] = {1, 2, 4, 8, 16, 32};
 * b.  sextet[2]
 * c.  int lots[100] = { [99] = -1};
 * d.  int pots[100] = { [5] = 101, [10] = 101,
 * 101, 101, 101};
 */
