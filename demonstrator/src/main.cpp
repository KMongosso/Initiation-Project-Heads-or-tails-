/***    Demonstrator main code
 * Demonstrator : takes two type of inputs, the first one is the predictor and then different benchmarks
 * all benchmark files are .txt files only full of 0 and 1 separated by a space
 * Shows the final and current success percentage in predictoring in if the following benchmark number will be a 0 or a 1
***/

#include "demonstrator.h"     // All functions used in the main
#include "display.h"          // All display functions (header, ask for the name of the benchmark file...)
#include "predictors.h"

int main(){
  srand(time(NULL));
  
  displayHeader();
  string benchmarkName = askForBenchmark();

  //ifstream benchmark(benchmarkName.c_str(), ios::in); // benchmark (.txt files) opening(s) for reading
  //if (!benchmark.fail()){     // if the opening was successful 
    
  //benchmark.close();
  //}
  //else {             // else
  //cerr << "Impossible to open the file !" << endl;
  //}
  
  unsigned short int * historic = NULL;
  unsigned short int size = loadBenchmark(benchmarkName, &historic);
  unsigned short int turn = 0;
  
  unsigned short int * results = (unsigned short int *) malloc(sizeof(unsigned short int)*size);
    
  int i;
  for(i=0;i<size;i++){
    results[i] = opposite(historic,turn);
    turn++;
  }

  string resultFileName;
  cin >> resultFileName;
  resultFileName = "results/"+resultFileName;
  
  ofstream resultsFile(resultFileName.c_str(), ios::out | ios::trunc);

  if(resultsFile){
    int i;
    for(i=0;i<size;i++){
      resultsFile << results[i] << " ";
    }
    resultsFile.close();
  }
  else{
    cerr << "Impossible to open the file !" << endl;
  }
  
  free (results);
  free (historic);
   
  return 0;

}
