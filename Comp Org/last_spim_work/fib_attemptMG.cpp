#include <iostream> 
using namespace std ;

// fibb numbers   1  1  2  3  5  8  13  21  34  55  89  144
// list order     0  1  2  3  4  5  6   7   8   9   10  11 
// ----------------------------------------------------------
// Done. - Program Works flaw less

int fibbi(int a, int b, int num ) { 
  int f;
  if( num < 1 ){ 
    // n is our counter and the number that the user input placed 
    cout << "this is your answer: "<< b<< endl;
    return b ; 
  }

  else { 
    // I need to to initiate a and b as well as subtract 1 from n.  
    f= a+b;
    a = b ;
    b  = f ;
    num = num-1; 

    //    cout <<"this is f "<<  f<< endl;
    //    cout <<" this is a " << a <<endl;
    
    return fibbi( a, b, num); 
  } 
} 

int main() { 
  int a, b , num; 
  a = 0;
  b = 1;
  cout << "Enter your fib number:\n " ; 
  cin >> num; 
  fibbi(a,b, num) ; 
  
  // cout << fibbi(a,b, num)  << endl;

  return 0 ; 
  

}
 // end of fibbi function 		
