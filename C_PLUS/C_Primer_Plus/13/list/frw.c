#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define BUFSIZE 4096
#define SLEN 81

void append(FILE * src, FILE * app);
char * s_gets(char * st, int n);

int main(void)
{
	FILE * fs, *fa;
	char file_src[SLEN], file_app[SLEN];
	int files = 0;
	char ch;

	fputs("Enter the destination file(empty to quit):", stdout);
	if ((fa = fopen(s_gets(file_app, SLEN), "a+")) == NULL )
	{
		fprintf(stderr,"can not open file %s to write", file_app);
		exit(EXIT_FAILURE);
	}
	if (setvbuf(fa, NULL, _IOFBF, BUFSIZE) != 0)
	{
		fputs("can not create write buffer\n", stdout);
		exit(EXIT_FAILURE);
	}
	fputs("Enter the name of first source file (empty to quit):", stdout);
	while (s_gets(file_src, SLEN) && file_src[0] != '\0')
	{
		if (strcmp(file_src, file_app) == 0)
			fprintf(stderr, "can not append %s to itself\n", file_src);
		else if ((fs = fopen(file_src, "r")) == NULL)
			fprintf(stderr, "cant open file %s to read.\n", file_src);
		else if (setvbuf(fs, NULL, _IOFBF, BUFSIZE))
			fputs("can not create read buffer", stderr);
		else
		{
			append(fs, fa);
			if (ferror(fs))
				fprintf(stderr, "Error in reading file %s\n", file_src);
			if (ferror(fa))
				fprintf(stderr, "Error in writing file %s.\n", file_app);
			files++;
			fclose(fs);
			fprintf(stdout, "file %s appended\n", file_src);
		}
		fputs("enter next source file (empty to quit):",stdout);
	}

	fprintf(stdout, "Done appending. %d files appended\n", files);
	fputs("displaying the contents:\n", stdout);
	rewind(fa);
	while ((ch = getc(fa)) != EOF)
		putc(ch, stdout);
	fputs("Done displaying. \n", stdout);
	fclose(fa);

	return 0;


}




void append(FILE *src, FILE *app)
{
	size_t bytes;
	static char temp[BUFSIZE];
	while ((bytes = fread(temp, sizeof (char), BUFSIZE, src)) > 0)
		fwrite(temp, sizeof(char), bytes, app); // bytes. not BUFSIZE
}

char * s_gets(char *st, int n)
{
	char * ret_val;
	char * find;

	ret_val = fgets(st, n, stdin);
	if (ret_val)
	{
		find = strchr(st, '\n');
		if (find)
			*find = '\0';
		else
			while (getchar() != '\n')
				continue;
	}

	return ret_val;
}
