# include <iostream> 
using namespace std; 


int factorialRecursive(int factorialMe) {

  // BASE CASES

  if(factorialMe < 0) {

    cout << "NO ! DEFINED FOR " << factorialMe << endl;

    return -1;

  }

  else if(factorialMe == 0) {

    return 1;

  }

  // RECURSIVE CASE

  else {

    return factorialMe * factorialRecursive(factorialMe - 1);
 }} 				//  end function and else statement 




int main (){

  int num ; 
  cout << "Enter your Fib Number: " << endl; 
  cin >>  num ;  
  cout<< factorialRecursive(num) << endl; 
  cout << "Done." << endl;


      return 0 ; 
    }
