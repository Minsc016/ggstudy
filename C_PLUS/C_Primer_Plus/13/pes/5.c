/*************************************************************************
  > File Name: 5.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep 30 15:15:16 2020
 ************************************************************************/

/*
 * 5.  Modify the program in Listing 13.5 so that it uses a command-line interface instead of an 
 * interactive interface. 
 * */


/* copy of 13.5 */

/* Listing 13.5   The append.c Program  */
/* append.c -- appends files to a file */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFSIZE 4096
#define SLEN 81
void append(FILE *source, FILE *dest);
char * s_gets(char * st, int n);
int main(int argc, char * argv[])
{
	FILE *fa, *fs; // fa for append file, fs for source file
	int files = 0; // number of files appended
	char file_app[SLEN]; // name of append file
	char file_src[SLEN]; // name of source file
	int ch;

	if (argc < 3)
	{
		printf("Usage: %s filename<destination> filename<source1> filename<source2> ....",argv[0]);
		exit(EXIT_FAILURE);
	}

	printf("use the first para[%s] as the name of destination file.\n", argv[1]);
	//s_gets(file_app, SLEN);
	strcpy(file_app, argv[1]);
	if ((fa = fopen(file_app, "a+")) == NULL)
	{
		fprintf(stderr, "Can't open %s\n", file_app);
		exit(EXIT_FAILURE);
	}
	if (setvbuf(fa, NULL, _IOFBF, BUFSIZE) != 0)
	{
		fputs("Can't create output buffer\n", stderr);
		exit(EXIT_FAILURE);
	}
	puts("use the other paras as the name of source files.\n");
	printf("first source file[%s].\n", argv[2]);

//	while (s_gets(file_src, SLEN) && file_src[0] != '\0')
	for (int i = 2; i < argc; i++)	
	{
		printf("Now appending file[%s]:", argv[i]);
		strcpy(file_src, argv[i]);

		if (strcmp(file_src, file_app) == 0)
			fputs("Can't append file to itself\n",stderr);
		else if ((fs = fopen(file_src, "r")) == NULL)
			fprintf(stderr, "Can't open %s\n", file_src);
		else
		{
			if (setvbuf(fs, NULL, _IOFBF, BUFSIZE) != 0)
			{
					fputs("Can't create input buffer\n",stderr);
				continue;
			}
			append(fs, fa);
			if (ferror(fs) != 0)
				fprintf(stderr,"Error in reading file %s.\n",
						file_src);
			if (ferror(fa) != 0)
				fprintf(stderr,"Error in writing file %s.\n",
						file_app);
			fclose(fs);
			files++;
			printf("File %s appended.\n", file_src);
		}
	}
	printf("Done appending. %d files appended.\n", files);
	rewind(fa);
	printf("%s contents:\n", file_app);
	while ((ch = getc(fa)) != EOF)
		putchar(ch);
	puts("Done displaying.");
	fclose(fa);
	return 0;
}
void append(FILE *source, FILE *dest)
{
	size_t bytes;
	static char temp[BUFSIZE]; // allocate once
	while ((bytes = fread(temp,sizeof(char),BUFSIZE,source)) > 0)
		fwrite(temp, sizeof (char), bytes, dest);
}
char * s_gets(char * st, int n)
{
	char * ret_val;
	char * find;
	ret_val = fgets(st, n, stdin);
	if (ret_val)
	{
		find = strchr(st, '\n'); // look for newline
		if (find) // if the address is not NULL,
			*find = '\0'; // place a null character there
		else
			while (getchar() != '\n')
				continue;
	}
	return ret_val;
} 
