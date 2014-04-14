// Robert Gutierrez 
// Fibbinacci numbers


#include<iostream>
using namespace std; 


int fib(int num){ 

  if (num == 1 || num ==0)
 { 
    return num ; 
 }
  else{

  return ((fib(num-1)) + (fib(num-2))); 
}
} // Close fib function 

int main()
{
  int num;
  cout << "Enter your fibonacci number: " << endl; 
  cin >>  num ; 

  int answer; 
  cout << fib(num) << endl; 

 return 0; 
}
