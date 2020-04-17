def fun(s):
    l=[]
    y='.'
    z='@'
    if y in s:
        if(s.count(z) !=1):
            l.append(-1)
        else:
            username,remainning=s.split('@')
            websitename,extension=remainning.split('.')
            username=username.replace('_','').replace('-','')
            if(username.isalnum()):
                      l.append(1)
            if(websitename.isalnum()):
                      l.append(1)
            if(len(extension)<=3):
                      l.append(1)
            if(sum(l)==3):
                return True
            
    return False  
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
