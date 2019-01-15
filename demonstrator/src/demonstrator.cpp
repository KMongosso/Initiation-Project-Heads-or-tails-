#include "demonstrator.h"

unsigned short int loadBenchmark(string benchmarkName, unsigned short int ** historic){

  ifstream benchmark(benchmarkName.c_str(), ios::in);
  if(!benchmark.fail()){

    unsigned short int size = 0;
    benchmark >> size;
    *historic = new(nothrow) unsigned short int[size]; 

    if(*historic){
      int i;
      for (i=0; i<size; i++){
	benchmark >> (*historic)[i];
      }
      return size;
    }
    else{
      cerr << " Impossible to make memory allocation ! " << endl;
    }

    benchmark.close();
  }
  else {
    cerr << "Impossible to open the file !" << endl;
  }

  return 0;
}
