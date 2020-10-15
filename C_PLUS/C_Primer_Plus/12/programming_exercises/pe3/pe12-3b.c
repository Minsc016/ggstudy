/*************************************************************************
  > File Name: 2.c
  > Author: Crow
  > Mail: qnglsk@163.com 
  > Created Time: Mon Sep 14 09:19:48 2020
 ************************************************************************/


/*    2.  Gasoline consumption commonly is computed in miles per gallon in the U.S. and in 
	  liters per 100 kilometers in Europe. What follows is part of a program that asks the user 
	  to choose a mode (metric or U.S.) and then gathers data and computes fuel consumption: 
	  */

// pe12-3b.c
// compile with pe12-2a.c

//#define DEBUG

#include "pe12-3a.h"
int main(void)
{
	int mode;
	double var[2] = {0,0};

	printf("Enter 0 for metric mode, 1 for US mode: ");
	scanf("%d", &mode);
#ifdef DEBUG
	printf("\033[31;1m--mode in main after enter::%d--\n\033[0m", mode);
#endif
	while (mode >= 0)
	{
		mode = set_mode(mode);
#ifdef DEBUG
	printf("\033[31;1m--mode in main after set::%d--\n\033[0m", mode);
#endif
		get_info(mode, var);
		show_info(mode,var[0],var[1]);
		printf("Enter 0 for metric mode, 1 for US mode");
		printf(" (-1 to quit): ");
		scanf("%d", &mode);
#ifdef DEBUG
	printf("\033[31;1m--mode in main after enter::%d--\n\033[0m", mode);
#endif
	}
	printf("Done.\n");
	return 0;
} 

/* Here is some sample output: 
   Enter 0 for metric mode, 1 for US mode: 0
   Enter distance traveled in kilometers: 600
   Enter fuel consumed in liters: 78.8
   Fuel consumption is 13.13 liters per 100 km.
   Enter 0 for metric mode, 1 for US mode (-1 to quit): 1
   Enter distance traveled in miles: 434
   Enter fuel consumed in gallons: 12.7
   Fuel consumption is 34.2 miles per gallon.
   Enter 0 for metric mode, 1 for US mode (-1 to quit): 3
   Invalid mode specified. Mode 1(US) used.
   Enter distance traveled in miles: 388
   Enter fuel consumed in gallons: 15.3
   Fuel consumption is 25.4 miles per gallon.
   Enter 0 for metric mode, 1 for US mode (-1 to quit): -1
   Done. 
   If the user enters an incorrect mode, the program comments on that and uses the most 
   recent mode. Supply a pe12-2a.h header file and a pe12-2a.c source code file to make 
   this work. The source code file should define three file-scope, internal-linkage variables. 
   One represents the mode, one represents the distance, and one represents the fuel 
   consumed. The get_info() function prompts for data according to the mode setting 
   and stores the responses in the file-scope variables. The show_info() function calculates 
   and displays the fuel consumption based on the mode setting. You can assume the user 
   responds with numeric input.
*/
