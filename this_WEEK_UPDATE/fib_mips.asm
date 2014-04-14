#--------------------------------------------------------------------------#
	# Robert Gutierrez
	# Purpose: Fib Numbers in spim beacuse it is FUN 
	# Input:   basic postive numbers
	# Output:  simple input number 
#--------------------------------------------------------------------------#
	.data
usrInput:	.asciiz "Enter A positive Whole number: \n"
endl:		.asciiz "\n"
myNUM:		.space 8 

#--------------------------------------------------------------------------#
	.text
	.globl main
main:
	la 	$a0, usrInput 		# load address with Usr Input prompt
	li 	$v0, 4 			# print out mssg
	syscall  

	li	$v0, 5
	syscall				
	
	la	$a0, myNum		#load the usr input into myNum space
	li	$a1,8   		# the byte space 
	move 	$t0, $a0
	syscall 			


	
	la 	$a0, myNUM
	li	$v0,1
	syscall
	
	
	li 	 $v0 , 10 		# End program FIN 
	syscall
	
