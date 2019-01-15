// All and only the prediction algorithm codes, no main function, sort of library 

// Historic is the table which contains the 0 and 1 (that we are trying to predict) readed or said by the "opponent" in the apparition order
// Size is it length
// Turn start at zero, it's the total number of prediction attempt   

#include "predictors.h"

unsigned short int opposite(unsigned short int *historic, unsigned short int turn) {
  
  if (turn == 0){
    return 1; // arbitrary, historic table is empty so we decide to predict 1 at first to start  
  }
  else{
    if (historic[turn-1] == 0){
      return 1;
    }
    else{
      return 0;
    }
  }
    
}



//return a decimal number from a binary number
//historic is a table of 1 and 0
//n is th length of the binary number
//k is the index of the end of the binary number in historic
int binaryToDecimal(unsigned short int *historic, int n, unsigned short int turn){
    int decimal = 0;
    for (int i=0 ; i< n ;i++ ){
        decimal += pow(2,i)*historic[turn-1];
	turn--;
    }
    return decimal;
}

unsigned short int n_bits_pattern(unsigned short int *historic, unsigned short int turn, int n, unsigned short int memory, unsigned short int * myPrediction){
    //initilization of memory, the table that will count each pattern in the historic
  static unsigned short int * bitsTab = (unsigned short int *)malloc(sizeof(unsigned short int)*pow(2,n));
  int i;
  /*for (i=0 ; i<pow(2,n); i++){
    bitsTab[i] = 0;
  }
    //evaluation of each pattern in historic
  if (turn >= n){
    if(turn > memory){
      bitsTab[binaryToDecimal(historic, n, )]--;
    }
    for (int k=(n-1); k<turn ; k++){
      int pattern = convert_b_to_d(historic,n,k) ; //pattern is a decimal number
      memory[pattern]++;
      
      if ( memory[ (convert_b_to_d(historic, n-1, turn)+1) *2 ] > memory[ (convert_b_to_d(historic, n-1, turn) *2 +1 )] )
	return 1;
      else
	return 0; //arbitrary 0 if it's equal
    }
    else {
      return rand()%2;
    }
  }
  */
  return 0;
}
