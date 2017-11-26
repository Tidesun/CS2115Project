from pyeda.inter import *

A,B, C, D, E, F, G = map(exprvar, 'ABCDEFG')

A = 0
B = 1
E = 1
H = ~D
S1 = C&H | ~C&~H
I = G
S2 = F&~I | ~F&I
S3 = D&S2 | ~D&~S2
S4 = C&S3 | ~C&~S3
S = ~S4 | S1

for x in S.satisfy_all():
	print(x)