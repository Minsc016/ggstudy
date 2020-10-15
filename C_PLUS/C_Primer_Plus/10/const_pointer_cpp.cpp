/*************************************************************************
	> File Name: const_pointer_cpp.cpp
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Tue Sep  1 15:33:48 2020
 ************************************************************************/

#include<iostream>
using namespace std;
#include<string>
#include<vector>
#include<cstdlib>
#include<fstream>
#include<algorithm>

int main(void)
{
	const int y = 4;
	const int * p2 = &y;
	int * p1;
	p1 = p2;

	cout << "*p1:" << *p1 << endl;; 

	return 0;
}
