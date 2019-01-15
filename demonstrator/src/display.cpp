// Display functions 
// cf display.h for more details 

#include "display.h"

void displayHeader(){

  cout << endl << endl << "INITIATION PROJECT - POLYTECH SORBONNE - MAIN - S6" << endl;
  cout << "BY FELIX CHOI - KARL MONGOSSO - JORDY AJANOHOUN" << endl;
  cout << "PROJECT MANAGER : JULIEN BRAJARD " << endl;
  cout << endl << "HEADS or TAILS " << endl << endl << endl;
}

string askForBenchmark(){

  string benchmarkName;

  cout << "Please, indicate the benchmark(s) you have choose (absolute or relative path !). They have to be \".txt\" files : ";
  cin >> benchmarkName;

  return benchmarkName;

}


void displayTab(unsigned short int * tab, unsigned short int size){

  int i;
  for(i=0;i<size;i++){
    cout << tab[i] << " ";
  }
  cout << endl;
}
