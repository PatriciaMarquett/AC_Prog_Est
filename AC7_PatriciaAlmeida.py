"""
AC7 - Aluna: Patricia Almeida Marquett
Matrícula: 202302989527
"""

# 1048 - Salary Increase
a = float(input())
if(a>=0 and a<=400):
	b= a*0.15
	c=a+b
	d=15
elif(a>=400.01 and a<=800.00):
	b=a*0.12
	c=a+b
	d=12
elif(a>=800.01 and a<=1200.00):
    b=a*0.1
    c=a+b
    d=10
elif(a>=1200.01 and a<=2000.00):
	b=a*0.07
	c=a+b
	d=7
elif(a>2000):
	b=a*0.04
	c=a+b
	d=4
print(f"Novo salario: {c:.2f}")
print(f"Reajuste ganho: {b:.2f}")
print(f"Em percentual: {d} %")

# 1065 - Even Between five Numbers
for i in range(5):
    n = float(input())
    if(n%2==0):
        count=count+1
print(f"{count} valores pares")

# 1132 - 	Multiples of 13
n1 = int(input())
n2 = int(input())
t = n1
s = 0
if(n1 > n2):
    n1 = n2
    n2 = t
while(n1 <= n2):
    if(n1%13 != 0):
        s += n1
    n1 += 1
print(s)

# 1173 - Array fill I
n= int(input())
print("N[%d] = %d" %(0,n))
for i in range(1,10):
    n *= 2
    print("N[%d] = %d" %(i,n))

# 1180 - Lowest Number And Position
n = int(input())
lista = list(map(int, input().split()))
p = 0
m = lista[0]
count = 0
for i in lista:
    if (i < m):
        m = i
        p = count
    count += 1
print("Menor valor: %d" % m)
print("Posicao: %d" % p)

"""# 1182 - Column in Array
#include <stdio.h>
int main()
{
    int a,i,j;
    char b;
    float x[12][12],sum=0,avr=0;
    scanf("%d",&a);
    scanf(" %c",&b);
    for(i=0;i<12;i++){
        for(j=0;j<12;j++){
            scanf("%f",&x[i][j]);
        }
    }

    for(i=0;i<12;i++){
        sum=sum+x[i][a];
    }
    if(b=='S'){
        printf("%.1f\n",sum);
    }
    else if(b=='M'){
        avr=(sum/12);
        printf("%.1f\n",avr);
    }

    return 0;
}"""

# 1244 - Sort by Length
n = int(input())
while n > 0:
    n -= 1
    c = input().split()
    c.sort(key=len, reverse=True)
    for i in range(len(c)):
        print(c[i], end = '')
        if i != len(c)-1:
            print(' ', end = '')
    print()
