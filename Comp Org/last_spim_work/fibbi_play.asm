#------------------------------------------------------------------------#
	# Robert Gutierrez
	# Purpose: Fib Numbers in spim beacuse it is FUN 
	# Input:   basic postive numbers
	# Output:  simple input number 
#------------------------------------------------------------------------#
	.data
usrInput:	.asciiz "Enter A positive Whole number: "
endl:		.asciiz "\n"
myNUM:		.space 8 

#------------------------------------------------------------------------#
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
	li 	$t6,1
	
	jal fibb			#call the Fuction fib (recursive)
	
	li 	 $v0 , 10 		# End program FIN 
	syscall
	
# ---------------------------------------------------------------------
	.data
inpro:	.asciiz "In procedure\n"
	.text

	
fibb:	# this will be our function t0 holds our value

	#  all of this vvv should be building a STACK

	#subu    $sp, $sp, 32 	# Allocate a 32-byte stack frame
#	sw  	$ra, 20($sp)  	# Save Return Address
#	sw  	$fp, 16($sp)  	# Save old frame pointer
#	addiu   $fp, $sp, 28  	# Setup new frame pointer
#	sw  	$a0,  0($fp)  	# Save argument (n) to stack
	
	
	# ---------------------------------------------------------
	#   Register $t5 = f    reg $t1 = a      reg $t2 = b
	#   Register $t3 = 1 (constant)        reg $t0 = usr input counter
	# ---------------------------------------------------------
	
	add 	$t5,$t1,$t2
	move 	$t1, $t2
	move 	$t2, $t5
	sub 	$t0, $t0, $t3
	move 	$a0, $t2
#	li	$v0,1 	#this SHOULD,(but not) be printing what MG whats back

	syscall
	li 	$v0,4
	la	$a0,endl
	syscall
	# ---------------------------------------------------------
	# ---------------------------------------------------------
	
	#instead of print out, send them to a stack, then -> print for reverse order. 
	jal fibb  	
# ---------------------------------------------------------------------
stack:

	lw $ra,0($sp)       #read registers from stack
	lw $t1,4($sp)

	addi $sp,$sp,12       #bring back stack pointer
	jr $ra

return1:
	 li $v0,1
	 j stack
	
return0 :
	li $v0,0
	 j stack	
	
	


