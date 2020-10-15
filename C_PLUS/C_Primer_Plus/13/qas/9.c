/*************************************************************************
	> File Name: 9.c
	> Author: Crow
	> Mail: qnglsk@163.com 
	> Created Time: Fri Sep 25 11:41:32 2020
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

/*

9.  The "a+" , "r+" , and "w+" modes all open files for both reading and writing. Which one 
is best suited for altering material already present in a file?""""""
 **/


/* a+ append 
 * r+ read
 * w+ write
 *
 * a+ is best choice.   ？？？？
 **/ 

/*
 * r open a file to read, fail if not exists.
 * w open a file to write, truncate if exists , create if not.
 * a open a file to write, only at the end. create if not exists
 *
 * r+ open a file for both read and write , fail if not exists
 * w+ open a file for both read and write, truncate if exists, create if not.
 * a+ open a file for both read and write, only can be written at the end. create if not exists.
 *
 * +x :fail if file exists, AND OPEN THE FILE is exclusive mode.
 * (独占模式，不允许其他用户/程序使用此文件。)
 * */

// so the best answer is r+.
