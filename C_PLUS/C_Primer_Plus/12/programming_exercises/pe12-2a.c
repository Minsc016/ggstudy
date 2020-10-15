#include "pe12-2a.h"

//#define DEBUG
extern int mode;
void set_mode()
{
#ifdef DEBUG
	printf("\033[32;1m--mode in set_mode1:%d--\n\033[0m", mode);
#endif
	if (mode > 1)
	{
		mode = 1;
		printf("Invalid mode specified. Mode 1(US) uesd.\n");
	}
#ifdef DEBUG
	printf("\033[32;1m--mode in set_mode2:%d--\n\033[0m", mode);
#endif
}

void get_info()
{
#ifdef DEBUG
	printf("\033[33;1m--mode in get_info:%d--\n\033[0m", mode);
#endif
	char * spr = "Enter distance traveled in ";
	if (0 == mode)
		printf( "%s%s", spr, "kilometers: " );
	else if ( 1 == mode )
		printf( "%s%s", spr, "miles: " );
	scanf( "%lf", &distance );
	printf("Enter fuel consumed in gallons: ");
	scanf( "%lf", &fuel_consm );
}

void show_info()
{
	double res;
	if ( 0 == mode )
		res = fuel_consm / distance * 100;
	else if ( 1 == mode )
		res =  distance / fuel_consm ;
	printf( "Fuel consumption is %.2lf %s\n", res, (mode?"miles per gallon.":"liters per 100 km"));
}
