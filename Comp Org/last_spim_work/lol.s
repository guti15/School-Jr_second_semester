#-------------------------------------------------------------------------
# SPIM assignment 3
#
# Angel Mejia
# Purpose: Use a recursive definition to calculate the fibonacci sequence
# and calculate the sum also through the use of recursion in MIPS.
#
# Input: The program will take an input of an integer between 0 and 44, no negatives.
#
# Output: The program will output the fibonacci sequence in reverse starting with 
# the nth number from the input. The program will also take the sum of all those
# numbers and output it.
#--------------------------------------------------------------------------
	.data
prompt: .asciiz "Please enter a number: "
endl: .asciiz "\n"
Sumis: .asciiz "Your sum is: "

#-------------------------------------------------------------------------
	.text
	.globl main

main:
	#Registers $s0 and $s1 will hold 0 and 1 respectively as the starting
	#Fibonacci numbers. 
	#Register $s5 will be used later in the program to calculate the sum
	#after the numbers have been calculated.
	#$s7 will hold the user input.

	#will be used to catch sum
	li $s5, 0


	li	$v0, 4
	la	$a0, prompt
	syscall

	#save the integer
	li	$v0, 5
	syscall

	move $s7, $v0 #move the input into an argument

	#will hold 0 and 1
	li $s0, 0
	li $s1, 1

	#if input is 0 this will skill straight to sum calculation
	beq $s7, $zero, Sum

	#jump to procedure
	jal Fibo

Sum:

	#Print the sum
	li	$v0, 4
	la	$a0, Sumis
	syscall

	move $a0, $s5
	li $v0, 1
	syscall

done: 
	#program end
	li	$v0, 10
	syscall

#---------------------------------------------------------------------------#
#Fibonacci function below will calculate the fibonacci sequence from the input
#number position all the way to the bottom number and then calculate the sum of
#all those numbers
	.data
	.text

Fibo:
	# Allocate storage for frame
	subu	$sp, $sp, 32		# size as we computed
	# Save return address
	sw	$ra, 20($sp)
	# Save frame pointer
	sw	$fp, 16($sp)
	# Reset frame pointer
	addu	$fp, $sp, 28
	# Save arguments
	sw	$s0, -4($fp)
	sw	$s1, 0($fp)
	
	#temporary storage
	move $t0, $s1

	#f1+f2 
	add $s1, $s1, $s0

	#store f1
	move $s0, $t0

	#calculate n-1
	subu $s7, $s7, 1

	#check if it is zero
	beq $s7, $zero, end

	#recurse
	jal Fibo

	#print out the number
	move $a0, $s0
	li $v0, 1
	syscall

	#add in to catch sum
	add $s5, $s5, $s0

	#newline
	li $v0, 4
	la $a0, endl
	syscall

	#Reload stack in reverse
	lw $s1, 0($fp)
	lw $s0, -4($fp)

	#addu $fp, $sp, 28
	lw $fp, 16($sp)
	lw $ra, 20($sp)
	addu $sp, $sp, 32
	

end: 
	j $ra

#-------------------------------------END------------------------------#

