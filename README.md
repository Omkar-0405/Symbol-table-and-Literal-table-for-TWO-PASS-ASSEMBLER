# Symbol-table-and-Literal-table-for-TWO-PASS-ASSEMBLER

#Assembly language code used in Programme
      START 200
      MOVR AREG DATA
      MOVR BREG =4
 X    EQU  10 
      LTORG
DATA  D   4
ST    DS  10
      MOVR CREG =5
      END

##**Assembly Directives(AD)** i.e** LTORG, EQU, START, END** has not assigned with Incremented location counter 

OutPut:
**...LOACTION COUNTER...**
 [200, 200, 201, 202, 202, 203, 203, 213, 214, 215]
 
**...SYMBOL TABLE...**
{'DATA': 203, 'X': 10, 'ST': 213}

**...LITERAL TABLE...**
{'=4': 202, '=5': 215}

