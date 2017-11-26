from pyeda.inter import *

catagory = [['Norwegian', 'Ukrainian', 'Englishman', 'Spaniard', 'Japanese'],
			['Fox', 'Horse', 'Snails', 'Dog', 'Zebra'],
			['Water', 'Tea', 'Milk', 'Orange Juice', 'Coffee'],
			['Yellow', 'Blue', 'Red', 'Ivory', 'Green'],
			['Kools', 'Chesterfield', 'Old Gold', 'Lucky Strike', 'Parliament']]

name="Nationality Pets Drinks Color Smokes".split()
X = exprvars('X',(1, 6),(1, 6),(1, 6))
A,B,C,D,E,F,G,H,I,J,K,L=map(exprvar,'ABCDEFGHIJKL')
V = And(*[
        And(*[
            OneHot(*[ X[r, c, v]
                for v in range(1, 6) ])
            for c in range(1, 6) ])
        for r in range(1, 6) ])


W = And(*[
        And(*[
            OneHot(*[ X[r, c, v]
                for c in range(1, 6) ])
            for v in range(1, 6) ])
        for r in range(1, 6) ])



# 2.The Englishman lives in the red house.
A=And(*[Equal(X[1,3,i],X[4,3,i]) for i in range(1, 6) ])
# 3.The Spaniard owns the dog.
B=And(*[Equal(X[1,4,i],X[2,4,i]) for i in range(1, 6) ])
# 4.Coffee is drunk in the green house.
C=And(*[Equal(X[3,5,i],X[4,5,i]) for i in range(1, 6) ])
# 5.The Ukrainian drinks tea.
D=And(*[Equal(X[1,2,i],X[3,2,i]) for i in range(1, 6) ])
# 6.The green house is immediately to the right of the ivory house.
E=And(*[Equal(X[4,5,i+1],X[4,4,i]) for i in range(1, 5) ])
E=E&(~X[4,5,1])
# 7.The Old Gold smoker owns snails.
F=And(*[Equal(X[5,3,i],X[2,3,i]) for i in range(1, 6) ])
# 8.Kools are smoked in the yellow house.
G=And(*[Equal(X[5,1,i],X[4,1,i]) for i in range(1, 6) ])
# 9.Milk is drunk in the middle house.
#=True
# 10.The Norwegian lives in the first house.
#X[1,1,1]=True
# 11.The man who smokes Chesterfields lives in the house next to the man with the fox.
H1=exprvar('H1')
H2=exprvar('H2')
H1=And(*[Equal(X[5,2,i+1],X[2,1,i]) for i in range(1, 5)])
H1=H1&(~X[5,2,1])
H2=And(*[Equal(X[5,2,i-1],X[2,1,i]) for i in range(2, 6)])
H2=H2&(~X[5,2,5])
H=H1|H2
# 12.Kools are smoked in the house next to the house where the horse is kept.
I1=exprvar('I1')
I2=exprvar('I2')
I1=And(*[Equal(X[5,1,i+1],X[2,2,i]) for i in range(1, 5)])
I1=I1&(~X[5,1,1])
I2=And(*[Equal(X[5,1,i-1],X[2,2,i]) for i in range(2, 6)])
I2=I2&(~X[5,1,5])
I=I1|I2
# 13.The Lucky Strike smoker drinks orange juice.
J=And(*[Equal(X[5,4,i],X[3,4,i]) for i in range(1, 6) ])
# 14.The Japanese smokes Parliaments.
K=And(*[Equal(X[1,5,i],X[5,5,i]) for i in range(1, 6) ])
# 15.The Norwegian lives next to the blue house.
L1=exprvar('I1')
L2=exprvar('I2')
L1=And(*[Equal(X[1,1,i+1],X[4,2,i]) for i in range(1, 5)])
L1=L1&(~X[1,1,1])
L2=And(*[Equal(X[1,1,i-1],X[4,2,i]) for i in range(2, 6)])
L2=L2&(~X[1,1,5])
L=L1|L2
S=A&B&C&D&E&F&G&H&I&J&K&L&V&W&(X[3,3,3])&(X[1,1,1])
result=S.satisfy_one()

for i in range(5):

	print("Person who lives in house No.",i+1,":")

	for k in range(5):
		for j in range (5):
			if (result[X[k+1,j+1,i+1]]==1):
				print(name[k],':',catagory[k][j])

	print()





