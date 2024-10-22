sir="Încălzirea globală este fenomenul de creștere continuă a temperaturilor medii înregistrate ale atmosferei în imediata apropiere a solului, precum și a apei oceanelor, constatată în ultimele două secole, dar mai ales în ultimele decenii."
mijloc=len(sir)//2
partea1=sir[:mijloc]
partea2=sir[mijloc:]
partea1.strip()
partea2=partea2[::-1]
partea2=partea2.replace(',',' ')
partea2=partea2.replace('.',' ')
print(partea1.upper()+partea2.capitalize())