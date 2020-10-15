/*************************************************************************
  > File Name: 5.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Tue Sep 22 16:06:04 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define MAX_SIZE 256

int main(int argc, char * argv[])
{
	FILE * fp;
	char line[MAX_SIZE];
	char * find;
//	char ch = argv[1][0]; // not commended. the assignment should after argc process.
	char ch;

	if (argc != 3)
	{
		printf("Usage:argv[0] char filename\n");
		exit(EXIT_FAILURE);
	}
	ch = argv[1][0]; // recommmended

	if ((fp = fopen(argv[2], "r")) == NULL)
	{
		printf("Can't open file %s to read.\n", argv[2]);
		exit(EXIT_FAILURE);
	}

	if (setvbuf(fp, NULL, _IOLBF, MAX_SIZE))
	{
		puts("Can't create line input buffer.\n");
		exit(EXIT_FAILURE);
	}

	//
	//fread(line, sizeof(char), MAX_SIZE, fp); 如果一行不满MAX_SIZE个，会读很多行
	while (fgets(line, MAX_SIZE, fp) && line[0] != EOF)
		//while (fgets(line,BUF,fp) != NULL)
	{
		//fgets 只会读一行。 一行超过256会????下次读？？ 会当成第二行读。
		//printf("%s", line);
		find = strchr(line, ch); // ch 可以是char , 但必须是一个字。
		if(find)
//			printf("%s", line);
			fputs(line, stdout);

		// 文件中的\n也会读进来并且输出为换行
		// 如果使用puts，Puts会自带一个末尾换行，多出一些空行。
		// 使用printf 并且不加\n， 超过256的，第一行也不会换行，跟下一次读进来的连在一起。
	}


	return 0;
}
