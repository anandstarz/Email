from validate_email import validate_email

result=open('output.tsv','w')

f=open('input.csv','r')

y=[]

result.write('Email_address\tDomain_name\tEmail_validation\n')

for i in f:
	y.append(i.replace('\n',''))

for j in range(len(y)):
	domain=validate_email('%s'%y[j], check_mx=True)
	if domain:
		val=validate_email('%s'%y[j], verify=True)
		result.write('%s\t%s\t%s\n'%(y[j],domain,val))
	else:
		result.write('%s\t-\t-\n'%(y[j]))
