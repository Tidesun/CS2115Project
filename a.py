from pyeda.inter import *
#  Knight and knave question
#  Z and M stands for Zoey and Mel
#  Z=1 if Zoey is a knight and Z=0 if he is a knave and similarly for M
Z, M = map(exprvar, 'ZM')
#  First statement is
A=~M;
#  Second statement is
B=Z&M
#  Notice that there is a hidden statement that
C=OneHot(Z,M)
#  Only one of these statements is true
S=OneHot(A,B)&C
#  Solve the question
print("The answer to knight and knave is")
for x in S.satisfy_all():
	print(x)

#  Box question
#  A,B,C stands for three boxes and r,w,b stands for three color chips
#  Ar=1 if A contains red chips
Ar,Br,Cr=map(exprvar,('Ar', 'Br', 'Cr'))
Aw,Bw,Cw=map(exprvar,('Aw', 'Bw', 'Cw'))
Ab,Bb,Cb=map(exprvar,('Ab', 'Bb', 'Cb'))
#  a colored chip is unique
R = OneHot(Ar,Br,Cr)
W = OneHot(Aw,Bw,Cw)
B = OneHot(Ab,Bb,Cb)
#  a box contains ONE chip
A=OneHot(Ar, Ab, Aw)
B=OneHot(Br, Bb, Bw)
C=OneHot(Cr, Cb, Cw)
#  Statement stands for the three statements
Statement = OneHot(Ar, ~Br, ~Cb)
#  Solve the question
S= R&W&B&A&B&C&Statement
print("The answer to Box question is")
for x in S.satisfy_all():
       print(x)

#  Lewis Carroll Game of Logic
experience,blunder,competent=map(exprvar,('experience','blunder','competent'))
A= Implies(experience,competent)
B= blunder
C= Implies(competent,~blunder)
S=A&B&C
print("The answer to Lewis Carroll's Game of Logic is")
for x in S.satisfy_all():
	print(x)

# Tao’s Game of Logic
logical,despised,baby,crocodilemanager=map(exprvar,('logical','despised','baby','crocodilemanager'))
A=Implies(~logical,despised)
B=Implies(baby,~logical)
C=Implies(crocodilemanager,~despised)
S=A&B&C
print("The answer to Tao’s Game of Logic is")
with baby:
	print(S.satisfy_one())
