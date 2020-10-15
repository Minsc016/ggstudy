/*
 * 1000 个 double 的数组
 * 每个为 100.0 * i + 1.0 / (i + 1)
 *
 * 以wb 写入文件 "number.dat"
 *
 * 以rb 读取文件, 输入index, 获取 数值。
 * */

#include<stdio.h>
#include<stdlib.h>

#define ARSIZE 1000

int main(void)
{
	FILE * iofile;
	const char * file = "number.dat";
	double numbers[ARSIZE];
	int index;
	double value;
	long pos;

	for (int i = 0; i < ARSIZE; i++)
		numbers[i] = 100.0 * i + 1.0 / (i + 1);

	if ( (iofile = fopen(file, "wb")) == NULL)
	{
		fprintf(stderr, "Could not open file %s to write.\n", file);
		exit(EXIT_FAILURE);
	}

	fwrite(numbers, sizeof (double), ARSIZE, iofile);
	if (ferror(iofile))
	{
		fprintf(stderr, "error in writting file %s.\n", file);
		exit(EXIT_FAILURE);
	}
//##	/* 测试使用 rewind 和 getc 来取数据是否可行 */
//##	fprintf(stdout, "Enter an index in the range 0 - %d.(out range to quit)\n", ARSIZE - 1);
//##	while ( scanf("%d", &index) == 1 && index >=0 && index < ARSIZE)
//##	{
//##		pos = (long) index * sizeof (double);
//##		rewind(iofile);
//##		fseek(iofile, pos, SEEK_SET);
//##		/* printf("The value there is %lf.\n", getc(iofile) ); // getc 不行 */
//##		//fread(&value, sizeof(double), 1, iofile);
//##		printf("The value there is %lf.\n", value);
//##		printf("Next index (out of range to quit):\n");
//##	}
//##	/* 测试结束  wb 模式以fseek 挑至pos 使用 getc 不可， 使用 fread不可*/

	/* 关闭文件再以 rb 打开 */
	fclose(iofile);
	if ((iofile = fopen(file, "rb")) == NULL)
	{
		fprintf(stderr, "could not open file %s to read.\n", file);
		exit(EXIT_FAILURE);
	}
	fprintf(stdout, "Enter an index in the range 0 - %d(out of range to quit):", ARSIZE - 1);
	while (scanf("%d", &index) == 1 && index >= 0 && index < ARSIZE)
	{
		pos = (long) index * sizeof (double) ;

		fseek(iofile, pos, SEEK_SET);
		fread(&value, sizeof (double), 1, iofile);
		printf("The value there is %lf.\n", value);
		printf("Enter the next index (out of range to quit):");
	}
	/* 结束 */

	fclose(iofile);
	return 0;
}
