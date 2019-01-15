#include <fstream>
#include <cstdlib>
#include <iostream>
#include <ctime>
#include <string>

using namespace std;

int main(){
	
	srand(time(NULL));
	
	unsigned short int size;
	string benchmarkName;
	
	cout << "Please enter the name that your benchmark will have : " << endl;
	cin >> benchmarkName;

	cout << " What length do you want for the benchmark ? " << endl;
	cin >> size;

	unsigned short int * benchmarkTab = (unsigned short int *) malloc(sizeof(unsigned short int)*(size+1));
	if (benchmarkTab){

		benchmarkTab[0] = size;
		int i;
		for(i=1; i<size+1; i++){
			benchmarkTab[i] = rand() % 2;
		}
	}
	else{
	cerr << " Impossible to make memory allocation ! " << endl;
	}
	
	ofstream benchmarkFile(benchmarkName.c_str(), ios::out | ios::trunc);
	if(benchmarkFile){
	  benchmarkFile << size << " ";
	  int i;
	  for(i=1;i<size+1; i++){
	    benchmarkFile << benchmarkTab[i] << " ";
	  }
	  benchmarkFile.close();
	}
	else{
	  cerr << " Impossible to open the file !" << endl;
	}
	 
	return 0;
}
