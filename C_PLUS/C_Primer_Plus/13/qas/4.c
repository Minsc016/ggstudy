/*************************************************************************
  > File Name: 4.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Tue Sep 22 15:32:41 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define DEBUG
int main(int argc, char * argv[])
{
	FILE * iof;
	float value, ave;
	float sum = 0.0;
	int count = 0;

	if (argc == 1)
	{
		fprintf(stdout, "NO FILES GIVEN, USE STDIN AS INPUT\n");
		iof = stdin;
	}
	else if (argc == 2)
	{
		if ((iof = fopen(argv[1], "r")) == NULL)
		{
			fprintf(stderr, "Cant open file %s to read.\n", argv[1]);
			exit(EXIT_FAILURE);
		}

	}

	if (setvbuf(iof, NULL, _IOLBF, sizeof(float)))
	{
		fprintf(stderr, "could not create read buffer\n");
		exit(EXIT_FAILURE);
	}

	/* 没读懂题，假设从文件里读浮点型数字，然后计算平均值，再写入文件里。 */
	/* 顺便输出在屏幕上 */

	while ( fscanf(iof, "%f", &value) == 1 )
	{
		sum += value;
		count++;
		ave = sum / count;
		/* debug */
#ifdef DEBUG
		fprintf(stdout, "value:[%f], sum:[%f], ave:[%f]\n", value, sum, ave);
#endif
	}

	if (argc == 1)
	{
		fprintf(stdout, "average:[%f]\n", ave);
		fclose(iof);
	}
	else if (argc == 2)
	{
		if ((iof = fopen(argv[1], "a+")) == NULL)
		{
			fprintf(stderr, "could not open file %s to read.\n", argv[1]);
			exit(EXIT_FAILURE);
		}
		if (setvbuf(iof, NULL, _IOLBF, sizeof(float)))
		{
			fprintf(stderr, "could not create output buffer\n");
			exit(EXIT_FAILURE);
		}

		fprintf(iof, "%f\n", ave);
		if (ferror(iof))
			printf("error in writting to file.\n");

	}
	fclose(iof);

	return 0;
}
