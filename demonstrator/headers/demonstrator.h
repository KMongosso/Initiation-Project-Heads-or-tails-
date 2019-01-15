// Necessary functions for the conduct, operation, of the demonstrator
// All functions needed except display and prediction functions 

#ifndef __DEMONSTRATOR_H__
#define __DEMONSTRATOR_H__

#include <iostream>
#include <fstream>          // To open files in input (we have to read the 0 and 1 in the benchmark)
#include <string>           // usefull for .c_str() function to "convert" a string in a char tab[] for then use it in ifstream
//
//#include "predictors.h"     // All prediction algorithms for the game 
#include <stdlib.h>

using namespace std;

unsigned short int loadBenchmark(string benchmarkName, unsigned short int ** historic);

#endif
