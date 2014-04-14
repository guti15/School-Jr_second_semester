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

	li	$v0, 5			# stores in number user input
	la 	$a0, myNUM		#hopefully sotre the usr input 8
	syscall


	li 	$a1, 8 			# the byte space for the usr input
	move 	$t0, $a0		# save the user input into $t0
	syscall
	
	la 	 $a0 , myNUM 		# print out our NUMBER
	li 	 $v0,  1 		# print out the Number we have
	syscall
	
	li 	 $v0 , 10 		# End program FIN 
	syscall
	
