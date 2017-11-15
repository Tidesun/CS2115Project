from pyeda.inter import *

n = input('please enter the number of heaps: ')
n = int(n)
heap=[0 for n in range(100)]
bheap=[0 for n in range(100)]

sizemax=-1
for i in range(n):
    heap[i]=int(input('please enter the number of stones in heap'+str(i)+': '))
    if (sizemax<uint2exprs(heap[i]).size):
    	sizemax=uint2exprs(heap[i]).size
for i in range(n):
    bheap[i]=uint2exprs(heap[i],sizemax)
ans= bheap[0]
for i in range(n-1):
	ans=ans ^ bheap[i+1]
if (ans.uor().simplify()==1):
	print('offensive move lose!')
else:
	print('offensive move win!')
