# Robert Gutierrez 

#Manipulate floasts and chalecter and write a couple of functions.

#----------------------------------------------------------------------------#
	.data
instr:	.asciiz	"Chose method of Pay.  S = Smaht pay & C = Credit Purchase(Q to quit): "
outstr: .asciiz "Your recipt" 
endl:	.asciiz "\n"
strl1:	 .space 1
#----------------------------------------------------------------------------#
	.text
	.globl main
main:
	li	$v0, 4		# op code for print string 
	la	$a0, instr
	syscall

# get data
	li	$v0, 8		# v0 stores user's input   8 Read string 
	syscall
	move	$t3, $a0	# User input in t3
	la 	$t3, strl1

# print out user input  -----Do not need vvvvv
	li 	$a0, strl1
	li	$v0,4	
	syscall		#  Debugger to see if I can read user input 
# ---------------------------Do not need ^^^^


#create a a function that compares the input 
