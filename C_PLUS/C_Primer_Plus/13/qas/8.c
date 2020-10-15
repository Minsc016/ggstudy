/*************************************************************************
	> File Name: 8.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Fri Sep 25 11:39:18 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>


/*
 * 8.  What’s the difference among the following? 
 * printf("Hello, %s\n", name);
 * fprintf(stdout, "Hello, %s\n", name);
 * fprintf(stderr, "Hello, %s\n", name); 
 *
 **/

/* printf use screen as output, 
 * and fprintf need user to specify where to output.
 * stdout stderr was set default to screen, 
 * if it was other place the result will be diffent. */

/*ANS::::
 * The first is just a shorthand notation for the second; the third writes to the standard 
 * error. Normally, the standard error is directed to the same place as the standard output, 
 * but the standard error is not affected by standard output redirection. 
 * */
