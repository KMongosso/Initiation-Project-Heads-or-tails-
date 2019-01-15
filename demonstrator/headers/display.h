// Display functions available 

#ifndef __DISPLAY_H__
#define __DISPLAY_H__


#include <iostream>

using namespace std;

// Display the welcome message and information about the project 
void displayHeader();

// Ask for the benchmark file name(s) and return them to allow us to open and read them
string askForBenchmark();

void displayTab(unsigned short int * tab, unsigned short int size);

#endif
