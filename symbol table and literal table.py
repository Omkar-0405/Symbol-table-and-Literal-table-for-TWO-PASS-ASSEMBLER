#symbol table and literal table
ip=[
['','START','200',''],
['','MOVR','AREG','DATA'],
['','MOVR','BREG','=4'],
['X','EQU','10',''],
['','LTORG','',''],
['DATA','DC','4',''],
['ST','DS','10',''],
['','MOVR','CREG','=5'],
['','END','','']]

instruction = ["MOVR","DC"]
instruction1 = ["EQU","START","END","LTORG","DS"]
reg=["AREG","BREG","CREG","DREG"]


LC = []
lt=0
sytab = dict()
literal = dict()

for r in range(len(ip)):
    row = ip[r]
    for c in range(len(row)):
        item = row[c]
        if item == "START" :
            lt = int(row[c+1])
            LC.append(lt)
        elif item =="MOVR":
            lt += 1
        elif item not in reg and item not in instruction not in instruction1 and item != '' and item == row[3] and "=" not in item:
            sytab[item] = '_'
            print("sYMBOL1",sytab)
            
        elif "=" in item:
            literal[item] = '_'
            print("LITERAL1",literal)
            
        elif item == "EQU" :
            sytab[row[c-1]] = int(row[c+1])
            print("sYMBOL2",sytab)
        elif item == "LTORG":
            for key in list(literal.keys()):
                literal[key] = lt
                lt+=1
                print("LITERAL2",literal)
        elif item == "DC":
            sytab[row[c-1]] = lt
            print("sYMBOL3",sytab)
        elif item == "DS":
            lt += int(row[c+1])
            sytab[row[c-1]] = lt
            print("sYMBOL4",sytab)
            
        elif item == "END":
            for key in list(literal.keys()):
                if literal[key] == "_":
                    lt+=1
                    literal[key] = lt
            print("LITERAL3",literal)        
        if item == row[1] :
            LC.append(lt)
 

print("...LOACTION COUNTER...\n",LC)
print("...SYMBOL TABLE...")
print(sytab)
print()
print("...LITERAL TABLE...")
print(literal)