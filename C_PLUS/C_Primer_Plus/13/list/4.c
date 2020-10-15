#include <stdio.h>
#include<stdlib.h>

int main(void)
{
	char ch,file[99];
	FILE * fp;
	long count,last;

	puts("Enter the name of the file to be processed:");
	scanf("%80s", file);
	if ((fp=fopen(file, "rb")) == NULL)
	{
		printf("reverse can't open %s\n", file);
		exit(EXIT_FAILURE);
	}
	fseek(fp, 0L, SEEK_END);
	last = ftell(fp);
	for (count=1L; count <= last; count++)
	{
		fseek(fp, -count, SEEK_END);
		ch = getc(fp);
		if (ch != '\032' && ch != '\r')
			putchar(ch);
	}
	putchar('\n');
	fclose(fp);

	return 0;
}
