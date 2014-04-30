#------------------------------------------------------------------------#
	# Robert Gutierrez
	# Purpose: Fib Numbers in spim beacuse it is FUN 
	# Input:   basic postive numbers
	# Output:  simple input number 
#------------------------------------------------------------------------#
	.data
usrInput:	.asciiz "Enter A positive Whole number: \n"
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
	
	jal fibb			#call the Fuction fib (recursive)
	

	li 	 $v0 , 10 		# End program FIN 
	syscall
	
# ---------------------------------------------------------------------
	.data
inpro:	.asciiz "In procedure\n"
	.text

	
fibb:	# this will be our function t0 holds our value

	#  all of this vvv should be building a STACK

	
	# Allocate storage for frame
	subu	$sp, $sp, 32		# size as we computed
	# Save return address
	sw	$ra, 20($sp)
	# Save frame pointer
	sw	$fp, 16($sp)
	# Reset frame pointer
	addu	$fp, $sp, 28
	# Save arguments
	sw	$t1, -4($fp)	# save argument (5) ; same as  24($sp)
	sw	$t2, 0($fp)	# save argument (10) ; same as 28($sp)
	
#	beq $t0,$zero,Done	--- (THIS IS THE PLAY PART)
	
	# ---------------------------------------------------------
	#   Register $t5 = f    reg $t1 = a      reg $t2 = b
	#   Register $t3 = 1 (constant)        reg $t0 = usr input counter
	# ---------------------------------------------------------
	
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
	# ---------------------------------------------------------
	# ---------------------------------------------------------
	
	#instead of print out, send them to a stack, then -> print for reverse order. 
	jal fibb  	
# ---------------------------------------------------------------------
stack:
	# jam in all the information of the stack.
	#ima call this stack here and then im goint to pop and print
	# numbers from fib get sent here and held 



print:	
	


Done:

	move 	$a0,$t5		# move the number in $t5 which is total Fib
	li 	$v0, 1		# print instruction	
	syscall
	
	li 	 $v0 , 10 		# End program FIN 
	syscall

	# got the fuction right now just need to build a stack to, print out numberes recursively.


