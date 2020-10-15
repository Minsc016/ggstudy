/*************************************************************************
	> File Name: where.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  9 11:51:49 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/* where's the memory */
int static_store = 30;
const char * pcg = "String Literal";
int main()
{
	int auto_store = 40;
	char auto_string[] = "Auto char array";
	int * pi;
	char * pcl;

	pi = (int *) malloc(sizeof(int));
	*pi = 35;
	pcl = (char *) malloc(strlen("Dynamic String") + 1);
	strcpy(pcl, "Dynamic String");

	printf("static_store: %d at %p\n", static_store, &static_store);
	printf("  auto_store: %d at %p\n", auto_store, &auto_store);
	printf("         *pi: %d at %p\n", *pi, pi);
	printf("\t%s \tat \t%p\n", pcg, pcg);
	printf("\t%s \tat \t%p\n", auto_string, auto_string);
	printf("\t%s \tat \t%p\n", pcl, pcl);
	printf("\t%s \tat \t%p\n", "Quoted String", "Quoted String");

	free(pi);
	free(pcl);

	return 0;
}
