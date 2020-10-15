/*************************************************************************
	> File Name: 13_6.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep 22 11:34:56 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/* randbin.c -- random access, binary i/o */

#define ARSIZE 1000

int main()
{
	double numbers[ARSIZE];
	double value;
	const char * file = "number.dat";
	int i;
	long pos;
	FILE * iofile;

	// create a set of double values
	for(i = 0; i < ARSIZE; i++)
		numbers[i] = 100.0 * i + 1.0 / (i + 1);
	// attempt to open file 
	if ((iofile = fopen(file, "wb")) == NULL)
	{
		fprintf(stderr, "Could not open %s for output.\n", file);
		exit(EXIT_FAILURE);
	}
	// write arry in binary format to file
	fwrite(numbers, sizeof (double), ARSIZE, iofile);
	fclose(iofile);
	if ((iofile = fopen(file, "rb")) == NULL)
	{
		fprintf(stderr, "Could not open %s for random access.\n", file);
		exit(EXIT_FAILURE);
	}
	//read selected items from file
	printf("Enter an index in the range 0-%d.\n", ARSIZE -1);
	while (scanf("%d", &i) == 1 && i >= 0 && i < ARSIZE)
	{
		pos = (long) i * sizeof(double); // calculate offset
		fseek(iofile, pos, SEEK_SET);	// go there
		fread(&value, sizeof (double), 1, iofile);
		printf("The value there is %f.\n", value);
		printf("Next index (out of range to quit):\n");
	}

	// finish up
	fclose(iofile);
	puts("Bye!");
	
	
	
	
	return 0;
	
}


