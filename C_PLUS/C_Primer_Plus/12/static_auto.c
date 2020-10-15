/*************************************************************************
	> File Name: static_auto.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Fri Sep  4 11:48:13 2020
 ************************************************************************/

#include<stdio.h>

/* Example 1 */
int Hocus = 4;
int magic();
int main(void)
{
	//extern int Hocus; //Hocus declared external
	int Hocus; //Hocus declared external

	printf("Hocus in main:%d\n", Hocus);
	magic();
	printf("Hocus in main:%d\n", Hocus);


	return 0;
}

int Pocus;
int magic()
{
	//extern int Hocus; // same as above
	auto int Hocus;

	printf("Hocus in magic:%d\n", Hocus);
	Hocus = 6;
	printf("Hocus in magic:%d\n", Hocus); // 可以改变它的值.
}
