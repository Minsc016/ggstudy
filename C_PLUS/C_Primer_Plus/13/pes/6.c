/*************************************************************************
  > File Name: 6.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Wed Sep 30 15:42:22 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/* 6.  Programs using command-line arguments rely on the user’s memory of how to use them 
 * correctly. Rewrite the program in Listing 13.2 so that, instead of using command-line 
 * arguments, it prompts the user for the required information.
 *
 * */

/* copy of 13.2 Listing 13.2   The reducto.c Program */
// reducto.c -- reduces your files by two-thirds!
#include <stdio.h>
#include <stdlib.h> // for exit()
#include <string.h>
#define LEN 81
//int main(int argc, char *argv[])
int main(void)
{
	FILE *in, *out; // declare two FILE pointers
	int ch;
	char name[LEN]; // storage for output filename
	char name_1[LEN]; // storage for input filename
	int count = 0;
	// check for command-line arguments
	/*if (argc < 2)
	{
		fprintf(stderr, "Usage: %s filename\n", argv[0]);
		exit(EXIT_FAILURE);
	}*/
	printf("Enter the name of file to reduce:\n");
	fscanf(stdin, "%s", name_1);
	// set up input
	//if ((in = fopen(argv[1], "r")) == NULL)
	if ((in = fopen(name_1, "r")) == NULL)
	{
		fprintf(stderr, "I couldn't open the file \"%s\"\n",
				name_1);
		exit(EXIT_FAILURE);
	}
	// set up output
	strncpy(name,name_1, LEN - 5); // copy filename
	name[LEN - 5] = '\0';
	strcat(name,".red"); // append .red
	if ((out = fopen(name, "w")) == NULL)
	{ // open file for writing
		fprintf(stderr,"Can't create output file.\n");
		exit(3);
	}
	// copy data
	while ((ch = getc(in)) != EOF)
		if (count++ % 3 == 0)
			putc(ch, out); // print every 3rd char
	// clean up
	if (fclose(in) != 0 || fclose(out) != 0)
		fprintf(stderr,"Error in closing files\n");
	return 0;
} 

