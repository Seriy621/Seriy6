x='/'
pole = [["#","#","#"],
           ["#","#","#"],
           ["#","#","#"]]

for stroka in pole:
	for kletka in stroka:
		print(kletka,end="")
	print()
while x!=("i"):
    print()
    a = int(input())
    b = int(input())
    pole[a][b]='*'

    for stroka in pole:
                for kletka in stroka:
                    print(kletka,end="")
                print()
	
    x = int(input())
    y = int(input())
    pole[x][y]='O'

    for stroka in pole:
                for kletka in stroka:
                    print(kletka,end="")
                print()
	
