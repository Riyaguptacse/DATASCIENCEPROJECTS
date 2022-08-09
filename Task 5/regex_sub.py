import re
N=int(input())
String=""""""
for i in range(N):
    s=""+input()+""
    String+=s
    if i<N-1:
        String+="\n"
    
String=re.sub("(?<= )(&&)(?= )",'and',String)
String=re.sub("(?<= )(\|\|)(?= )","or",String)
print(String)