#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;


int main()
{
    srand(time(NULL));

    int choice;
    int bit, pattern;
    string pattern_string = "";
    int space, appearance, counter;
    int temporaire, aleatoire;
    string benchmark_name,test,pattern_space;
    int sequence_choice,sequence_length,sequence_length_temp,pattern_length,pattern_integer;


    cout << "Do you want to access to the benchmark bank (1) or create your own sequence (2) ?" << endl;
    cin >> choice;

    while(choice!=1 and choice!=2){
        cout <<"Error! Type 1 or 2 : " ;
        cin >> choice;
    }

    cout << "How do you want to call your benchmark ?" << endl;
    cin >> benchmark_name;

    benchmark_name = "/Users/mac/Documents/Pile_ou_Face/Benchmarks/" + benchmark_name + ".txt";

    ofstream fichier(benchmark_name,ios::out | ios::trunc); //deplacer au debut

    if(choice == 1){    //demander a l'utilisateur un nom de benchmark
        cout << "What kind of benchmark do you want ? " << endl;
        cout << "   1 - 0000011111 type" << endl;
        cout << "   2 - 0101010101 type" << endl;
        cout << "   3 - Mix between 01010101 and 00001111 type" << endl;
        cout << "   4 - Regular schema with 010101 type between " << endl;
        cout << "   5 - Regular schema with random 0 and 1 between" << endl;
        cout << "   6 - Schema with random 0 and 1 between" << endl;
        cin >> sequence_choice;

        cout << "What is your sequence length ?" << endl;
        cin >> sequence_length;

        fichier << std::to_string(sequence_length) + " ";

        while(sequence_choice!=1 and sequence_choice!=2 and sequence_choice!=3 and sequence_choice!=4 and sequence_choice!=5 and sequence_choice!=6 and sequence_choice!=7 and sequence_choice!=8 and sequence_choice!=9){
            cout << "Error !!! You must type a number between 1 and 9 " << endl;
            cin >> sequence_choice;
        }


        if(sequence_choice==1)
            {
                cout << "when do you want the 0 and 1 to switch ? " << endl;
                cin >> temporaire ;

                for(int i=0;i<temporaire;i++){
                    bit = 0;
                    fichier << std::to_string(bit) + " ";

                }

                for(int j=temporaire;j<sequence_length;j++){
                        bit = 1;
                        fichier << std::to_string(bit) + " ";
                }
            }

        if(sequence_choice==2)
            {
                for(int i=0;i<sequence_length;i++){
                    if(i%2==0){
                        bit = 0;
                        fichier << std::to_string(bit) + " ";
                    }
                    else{
                        bit = 1;
                        fichier << std::to_string(bit) + " ";
                    }
                }
            }

        if(sequence_choice==3)
            {
                temporaire = rand()%sequence_length+1;


                for(int i=0;i<temporaire;i++){
                    if(i%2==0){
                        bit = 0;
                        fichier << std::to_string(bit) + " ";
                    }
                    else{
                        bit = 1;
                        fichier << std::to_string(bit) + " ";
                    }
                }

                aleatoire = rand()%(sequence_length-temporaire)+1;
                counter = temporaire + aleatoire;

                do{
                    if(bit==1){
                        for(int i=temporaire;i<counter;i++){
			    bit = 0;
                            fichier << std::to_string(bit) + " ";
                        }
                    }
                    else{
                        for(int i=temporaire;i<counter;i++){
                            bit =1;
                            fichier << std::to_string(bit) + " ";
                        }
                    }

                    temporaire = counter;
                    aleatoire = rand()%(sequence_length-temporaire)+1;
                    counter = counter + aleatoire;
                }
                while(sequence_length-counter>8); //Random value

                if(bit==1){
                        for(int i=counter-aleatoire;i<sequence_length;i++){
                            bit = 0;
			    fichier << std::to_string(bit) + " ";
                        }
                }
                else{
                    for(int i=counter-aleatoire;i<sequence_length;i++){
                        bit = 1;
			fichier << std::to_string(bit) + " ";
                    }
                }
            }

       if(sequence_choice==4) //seulement si la taille est supŽrieur  6*3
            {
		cout << "What is the pattern you want to recognize ?" << endl;
                cin >> pattern_integer;

		cout << "How many time do you want this pattern to appear ?" << endl;
		cin >> appearance;

		test = std::to_string(bit);

		while(appearance*test.size()>sequence_length){
			cout << "What is the pattern you want to recognize ?" << endl;
                	cin >> pattern_integer;

			cout << "How many time do you want this pattern to appear ?" << endl;
			cin >> space;
		}

		pattern_space = std::to_string(pattern_integer);

		for(int i=0;i<pattern_space.size();i++){
			pattern_string=pattern_string + pattern_space[i] + " ";
		}

		appearance = appearance + 1;
		space = sequence_length/appearance;
        counter = 0;
        bit = 0;
		sequence_length_temp=0;
		pattern_length=(std::to_string(pattern_integer)).size();

                while(sequence_length_temp<sequence_length){
                    if (counter == space){
                        fichier << pattern_string;
			counter = 0;
			sequence_length_temp=sequence_length_temp + pattern_length;
                    }
                    else{
                        fichier << std::to_string(bit) + " ";
                        counter ++;
                        if(bit==0){
                            bit=1;
                        }
                        else{
                            bit=0;
                        }
			sequence_length_temp++;
                    }

                }
            }


             if(sequence_choice==5) //seulement si la taille est supŽrieur  6
            {
                cout << "What is the pattern you want to recognize ?" << endl;
                cin >> pattern_integer;

		cout << "How many time do you want this pattern to appear ?" << endl;
		cin >> appearance;

		test = std::to_string(bit);

		while(appearance*test.size()>sequence_length){
			cout << "What is the pattern you want to recognize ?" << endl;
                	cin >> pattern_integer;

			cout << "How many time do you want this pattern to appear ?" << endl;
			cin >> space;
		}

		pattern_space = std::to_string(pattern_integer);

		for(int i=0;i<pattern_space.size();i++){
			pattern_string=pattern_string + pattern_space[i] + " ";
		}

		appearance = appearance+1;
		space = sequence_length/appearance;
                counter = 0;
                bit = 0;
		sequence_length_temp=0;
		pattern_length=(std::to_string(pattern_integer)).size();


                while(sequence_length_temp<sequence_length){
                    bit = rand()%2;
                    if (counter == space){
                            fichier << pattern_string ;
                            counter = 0;
			    sequence_length_temp=sequence_length_temp + pattern_length;

                    }
                    else{
                        fichier << std::to_string(bit) + " ";
                        counter ++;
                   	sequence_length_temp++;
		   }
                }
            }


             if(sequence_choice==6) //seulement si la taille est supŽrieur  6
            {
		cout << "What is the pattern you want to recognize ?" << endl;
                cin >> pattern_integer;

		cout << "How many time do you want this pattern to appear ?" << endl;
		cin >> appearance;

		test = std::to_string(bit);

		while(space*test.size()>sequence_length){
			cout << "What is the pattern you want to recognize ?" << endl;
                	cin >> pattern_integer;

			cout << "How many time do you want this pattern to appear ?" << endl;
			cin >> space;
		}

		pattern_space = std::to_string(pattern_integer);

		for(int i=0;i<pattern_space.size();i++){
			pattern_string=pattern_string + pattern_space[i] + " ";
		}

		appearance = appearance+1;
		space = rand()%(sequence_length/appearance);
                counter = 0;
		sequence_length_temp=0;
		pattern_length=(std::to_string(pattern_integer)).size();


                while(sequence_length_temp<sequence_length){
                    bit = rand()%2;
                    if (counter == space){
                        fichier << pattern_string ;
                        counter = 0;
                        appearance = appearance - 1;
			if (appearance!=0){
                        	space = rand()%((sequence_length-sequence_length_temp)/appearance);
			}
			sequence_length_temp = sequence_length_temp + pattern_length;
                    }
                    else{
                        fichier << std::to_string(bit) + " ";
                        counter ++;
			sequence_length_temp++;
                    }

                }
            }
    }

    else{
        counter = 0;
        cout << "What is your sequence length ?" << endl;
        cin >> sequence_length;
        fichier << std::to_string(sequence_length) + " ";
        do{
            cout << "Type 0 or 1 to add a bit to your sequence and 2 to end it " << endl;
            cin >> bit;
            while(bit!=0 and bit!=1){
                cout << "Error ! Type 0, 1 or 2 " << endl;
                cin >> bit;
            }

            if(bit==0 or bit==1){
                fichier << std::to_string(bit) + " ";
            }
            counter ++;
        }
        while(sequence_length!=counter);


    }

    fichier.close();

    return 0;
}
