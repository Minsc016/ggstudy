/*************************************************************************
	> File Name: s_gets.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep 22 10:28:43 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int main(void)
{
	char * ret_val;
	char * find;
	char st[81];

	printf("test begining: step1 fgets\n");
	ret_val = fgets(st, 81, stdin);
	fprintf(stdout, "ret_val:%p\n",ret_val);
	if (ret_val)
	{
		printf("test going: step2 strchr\n");
		find = strchr(st, '\n');
		printf("test keep going: step3 find:[%p], *find:[%c]\n", find, *find);
		if (find)
		{
			printf("test keep going: step4 finded\n");
			*find = '\0';
			printf("test keep going: step5 find reassingned:*find:[%c]\n", *find);

		}
		else
			while (getchar() != '\n')
				continue;
	}
/*
	fprintf(stdout, "*ret_val:%s\n", *ret_val);
	*/
	return 0;
	
}
