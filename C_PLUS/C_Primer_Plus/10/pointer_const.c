/*************************************************************************
	> File Name: pointer_const.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep  1 10:12:49 2020
 ************************************************************************/

#include<stdio.h>

int main(void)
{
	double rates[5] = {88.99,100.12,59.45,183.11,340.5};
	const int num[5] = {1,2,3,4,5};
	double *pc1 = rates;
	double const * pc2 = rates;
	const int * pd = num;
	const double * const pc3 = rates;



	/*************************************************************************************
	 *	声明定义函数的时候，参数使用const，则函数内不会因为传进来的是地址改变值
	 *	const double * pd = rates;  pd指向的值是const不能 被改变，但rates[0]可以改变。
	 *	const int * pd = num; 非const指针不可以指向const变量
	 *	会改变指针所指向的值的函数，不应该接收指向const值的指针。
	 *	double * const pc = rates; pc 不可以指向别处，但pc指向的值可以改变
	 *	const double * const pc = rates; pc 不可以指向别处，也不能用pc改变pc指向的值。
	 *
	 * ***********************************************************************************/


	return 0;
}
