/*************************************************************************
  > File Name: pe9.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep 16 10:35:22 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*
 * 

 Write a program with the following behavior. First, it asks you how many words you 
 wish to enter. Then it has you enter the words, and then it displays the words. Use 
 malloc() and the answer to the first question (the number of words) to create a dynamic 
 array of the corresponding number of pointers-to- char . (Note that because each element 
 in the array is a pointer-to- char , the pointer used to store the return value of malloc()
 should be a pointer-to-a-pointer-to- char .) When reading the string, the program should 
 read the word into a temporary array of char , use malloc() to allocate enough storage 
 to hold the word, and store the address in the array of char pointers. Then it should 
 copy the word from the temporary array into the allocated storage. Thus, you wind up 
 with an array of character pointers, each pointing to an object of the precise size needed 
 to store the particular word. A sample run could look like this: 
 How many words do you wish to enter? 5 
 Enter 5 words now:
 I enjoyed doing this exerise 
 Here are your words:
 I
 enjoyed
 doing
 this
 exercise 
 */
#define SIZE 100
int main(void)
{
	int words_num;
	char temp[SIZE];


	printf("How many words you wish to enter:");
	if (scanf("%d", &words_num) == 1 && words_num > 0)
	{
		char **pis = (char **)malloc(5 * sizeof(char *));
		printf("Enter %d words now:", words_num);
		for (int i = 0; i < words_num; i++)
		{
			scanf("%s", temp );
			pis[i] = (char *)malloc(strlen(temp) * sizeof(char));
			strcpy(pis[i], temp);
		}
		for (int i = 0; i< words_num; i++)
		{
			printf("%s\n", pis[i]);
			free(pis[i]);
		}
		free(pis);

	}

	return 0;
}
