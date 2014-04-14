#----------------------------------------------------------------------------#
# A1 project
# Robert Gutierrez 
# Purpose: Display Maximum and minimum Numbers as well as the s^2
# Input:   15 positive numbers
# Output:  To be determined 
#----------------------------------------------------------------------------#
#lw = load immediatley 
#la = load Address 
#sw store word 



#----------------------------------------------------------------------------#
	.data
instr:	.asciiz	"Enter an integer: "
outstr: .asciiz "Array is: "
endl:	.asciiz "\n"
array:	.word	1 2 3 4

#----------------------------------------------------------------------------#

	.text
	.globl main
main:
	li	$v0, 4	# loads integer number 4 into $v0 
	la	$a0, instr # loads the instr: Enter an array in $a0 
	syscall

# get data
	li	$v0, 5			# v0 stores user's input
	syscall
	move	$t3, $v0		# move it to t3
# change third element to user's input