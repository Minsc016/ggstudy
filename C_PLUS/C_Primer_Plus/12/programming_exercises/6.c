/*************************************************************************
	> File Name: 6.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Mon Sep 14 20:35:21 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * Write a program that generates 1,000 random numbers in the range 1–10. Don’t save or 
 * print the numbers, but do print how many times each number was produced. Have the 
 * program do this for 10 different seed values. Do the numbers appear in equal amounts? 
 * You can use the functions from this chapter or the ANSI C rand() and srand()
 * functions, which follow the same format that our functions do. This is one way to 
 * examine the randomness of a particular random-number generator. 
 * */
#define SIZE 1000

void gen_randn(int arr[]);
int main(void)
{
	int rand_times[10] = {0};
	srand((unsigned int)time(0));

	for (int i = 0; i < SIZE; i++)
		gen_randn(rand_times);

	for (int i = 0; i < 10; i++)
		printf("gen %d %d times\n", i+1, rand_times[i]);


	return 0;
}

void gen_randn(int arr[])
{
	//int randn;
	//randn = rand() % 10 + 1;
	arr[ rand () % 10 ] += 1;

}
