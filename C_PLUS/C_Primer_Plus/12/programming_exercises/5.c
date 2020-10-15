/*************************************************************************
  > File Name: 5.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Mon Sep 14 20:07:37 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * Write a program that generates a list of 100 random numbers in the range 1–10 
 * in sorted decreasing order. (You can adapt the sorting algorithm from Chapter 11 , 
 * “Character Strings and String Functions,” to type int . In this case, just sort the numbers 
 * themselves.)
 *
 * */
#define SIZE 100
int gen_num();
void sort_dec(int arr[], int size);
void show_arr(const int arr[], int size);
int main(void)
{
	srand((unsigned int)time(0));
	int randnn[SIZE];
	for (int i = 0; i < SIZE; i++)
		randnn[i] = gen_num();

	printf("100个随机数生成如下：\n");
	show_arr(randnn, SIZE);
	sort_dec(randnn, SIZE);

	printf("\n100个随机数倒序排序如下:\n");
	show_arr(randnn, SIZE);



	return 0;
}

int gen_num()
{
	return rand() % 10 + 1;
}

void sort_dec(int arr[], int size)
{
	int tmp;
	for (int i = 0; i < size; i++)
		for (int j = i+1; j < size; j++)
			if (arr[i] < arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
}

void show_arr(const int arr[], int size)
{
	for (int i = 0; i < size; i++)
		printf("%d%c", arr[i], " \n"[0==(i+1)%10]);
}
