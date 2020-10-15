/*************************************************************************
	> File Name: 1.c
	> Author: Minsc
	> Mail: qnglsk@163.com 
	> Created Time: Wed Sep  2 16:15:45 2020
 ************************************************************************/

#include<stdio.h>
int main(void)
{
	int ref[] = {8, 4, 0, 2};
	int *ptr;
	int index;

	for (index = 0, ptr = ref; index < 4; index++, ptr++)
		printf("%d %d\n", ref[index], *ptr);

//	printf("%u\n",sizeof ref);
	printf("%p %p\n",ref, &ref[0]);
	printf("%p %p %d %d\n", ref+1, &ref[1], *(ref+1), ref[1]);
	ptr = ref;
	++ptr;
	printf("%p %d\n", ptr, *ptr);
	return 0;
}

