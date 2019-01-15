// All available prediction algorithms
// Cf predictors.cpp for more details
#ifndef __PREDICTORS_H__
#define __PREDICTORS_H__

#include <iostream>
#include <math.h>
#include <cstdlib>
#include <ctime>

using namespace std;

// Predict the opposite of the last one dropped
unsigned short int opposite(unsigned short int *historic, unsigned short int turn);

//convert binary number into decimal number
int binaryToDecimal(short int *historic, int n, unsigned short int turn);

//Predict with a n-bits pattern
unsigned short int n_bits_pattern(unsigned short int *historic, unsigned short int turn, int n, unsigned short int memory, unsigned short int myPrediction);

#endif
