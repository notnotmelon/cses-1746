c={}
def w(x,y,s,m):
	t=(x,y,s)
	if not 0<=x<=m:return 0
	if s==0:return 1 if not y or -2<y-x<2 else 0
	if t in c:return c[t]
	c[t]=w(x-1,y,s-1,m)+w(x,y,s-1,m)+w(x+1,y,s-1,m)
	return c[t]

def solution(array, max):
	result = 1
	zeros = 0
	start = ''
	for i in array:
		if i == 0:
			zeros += 1
		else:
			
			if zeros == 0:
				start = i
			else:
				if start:
					result *= w(start, i, zeros, max)
				else:
					result *= sum(w(j+1, i, zeros - 1, max) for j in range(max))
				zeros = 0
	if zeros != 0: result *= w(start, '', zeros, 3)
	return result%1000000007


n1, n2 = (int(s) for s in input().split())
print(solution([int(s) for s in input().split()], n2))