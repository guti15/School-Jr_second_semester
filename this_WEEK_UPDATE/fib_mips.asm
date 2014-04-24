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
	la 	$a0, usrInput 		# load adrss with Usr Input prompt
	li 	$v0, 4 			# print out mssg
	syscall  

	li	$v0, 5			# stores in number user input
	syscall

	move 	$t0, $v0		# save the user input into $t0  (need		
	li      $t1,0 		# hold the number 0 in t1 
	li  	$t2,1 		# hold the number 1 in t2
	li 	$t3,1 		# hold a constant of 1 to subtract counter
	
	jal fibb			#call the Fuction fib (recursive)
	

	li 	 $v0 , 10 		# End program FIN 
	syscall
	
# ---------------------------------------------------------------------
fibb:	# this will be our function t0 holds our value 

	beq $t0,$zero,Done
#	j $ra		# will jump when done recursive # Not gonna work
	
	# ---------------------------------------------------------
	#   Register $t5 = f    reg $t1 = a      reg $t2 = b
	#   Register $t3 = 1 (constant)        reg $t0 = usr input counter
	
	add 	$t5,$t1,$t2
	move 	$t1, $t2
	move 	$t2, $t5
	sub 	$t0, $t0, $t3
	move 	$a0, $t2
	li	$v0,1 	#this should be printing what MG whats backw
	syscall
	li 	$v0,4
	la	$a0,endl
	syscall
	#instead of print out, send them to a stack, then -> print for reverse order. 
	
	jal fibb  

	
# ---------------------------------------------------------------------



Done:

	move 	$a0,$t5	
	li 	$v0, 1
	syscall
	
	li 	 $v0 , 10 		# End program FIN 
	syscall
	






	
# get to  my fuction -- new issue branch on equal --> to make this recurs.

	
# got the numeber now I have to call the function
	# if statement will be branch on equal return # that register with the same number:
	# else branch not equal and return (create two registers that hold ( fib -1 & fib -2 ) then each of those numbers calls the function again:   ---> and that repeats and

