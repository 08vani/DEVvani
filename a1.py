# Name : Vani Sikka
# Roll No : 2019395
# Group : 07

import datetime
import urllib.request

def getLatestRates():
	""" Returns: a JSON string that is a response to a latest rates query.

	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	url= urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
	data= url.read()
	return str(data)


def changeBase(amount, currency, desiredCurrency, date):
	""" Outputs: a float value f.
	"""
	currency= currency.upper()
	desiredCurrency= desiredCurrency.upper()
	link="https://api.exchangeratesapi.io/"+date
	url= urllib.request.urlopen(link)
	data= str(url.read())
	r1= data.index(currency)
	r2= data.index(desiredCurrency)
	R1= data[r1+5:data.index(',',r1)]
	R2= data[r2+5:data.index(',',r2)]
	R1= R1.strip()
	R2= R2.strip()
	if (desiredCurrency=="EUR" and currency=="EUR"):
		return float(amount)
	elif (currency=='EUR'):
		return (float(R2))*(float(amount))
	elif (desiredCurrency=="EUR"):
		return (float(amount))/(float(R1))
	
	else:
		return (float(R2)/float(R1))*float(amount)


	
#used bubble sort		
def SSort(l1):
	#i=0
	#j=0
	#temp=[0,0]
	l= len(l1)
	for i in range(0,l):
		for j in range(0,l-i-1):
			if (float(l1[j][1])>float(l1[j+1][1])):
				temp= l1[j]
				l1[j]=l1[j+1]
				l1[j+1]=temp
	
	return l1		
	
	

#json=getLatestRates()
def printAscending(json):
	""" Output: the sorted order of the Rates 
		You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""
	sl=[]
	l1=[]
	a= json.index('{')
	start= json.index('{',a+1)
	end= json.rindex('base')
	data= json[start+1:end-3]
	bl= data.split(',')
	for c in bl:
		s=c.split(':')
		sl.append(s)
	l2=SSort(sl)
	for q in range(len(l2)):
		print("1 EURO = "+l2[q][1]+" "+l2[q][0])
                


	


def extremeFridays(startDate, endDate, currency):
	""" Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		
	Parameters: 
	stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
	"""
	currency= currency.upper()
	link="https://api.exchangeratesapi.io/history?start_at="+ startDate +"&end_at="+ endDate
	url= urllib.request.urlopen(link)
	data= str(url.read())
	data= data[12:]
	d1= data.split('},')
	d=[]
	C=0
	for c in range(len(d1)-1):
		y=d1[c][1:5]
		m=d1[c][6:8]
		D=d1[c][9:11]
		if y=="" and m=="" and D=="":
			print("NO FRIDAYS IN THE GIVEN RANGE")
		else:
			date=(datetime.datetime(int(y),int(m),int(D)))
			day= date.weekday()
			if(day==4):
				d.append(['0','0'])
				d[C][0]=str(date)
				d[C][0]=d[C][0][0:-9]
				r1=d1[c].index(currency)
				R1=float(d1[c][r1+5:d1[c].index(',',r1)])
				d[C][1]=(R1)
				C=C+1
	mk=[]
	Mk=[]

	if len(d)==0:
		print("NO FRIDAYS IN THE GIVEN RANGE")
	else:
	          
		D=[]
		for i in range(len(d)):
			D.append(d[i][1])

		MIN= min(D)	
		MAX= max(D)
		Mk=[]
		for i in range(len(d)):
			if d[i][1] == MAX:
				Mk.append(d[i][0])#when you get maximum rate same in two different years
		mk=[]
		for i in range(len(d)):
			if d[i][1] == MIN:
				mk.append(d[i][0])#when you get minimum rate same in two different years	


		
		
	if(len(Mk)==1 and len(mk)==1):
		print(currency+" was strongest on "+ mk[0] +". 1 Euro was equal to "+ str(MIN) + currency)
		print(currency+" was weakest on "+ Mk[0] +". 1 Euro was equal to "+ str(MAX) + currency)
	else:
		for i in range(len(mk)):
			print(currency+" was strongest on "+ mk[i] +". 1 Euro was equal to "+ str(MIN) + currency)
		for i in range(len(Mk)):
			print(currency+" was weakest on "+ Mk[i] +". 1 Euro was equal to "+ str(MAX) + currency)




def findMissingDates(startDate, endDate):
	""" Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	"""
	date=[]
	DATE=[]
	link="https://api.exchangeratesapi.io/history?start_at="+ startDate +"&end_at="+ endDate
	url= urllib.request.urlopen(link)
	data= str(url.read())  
	datestart= datetime.datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
	dateend= datetime.datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
	duration= dateend - datestart
	for d in range(duration.days+1):
		day=str(datestart+ datetime.timedelta(days=d)) 
		date.append(day)
	for c in range(len(date)):
		DATE.append(date[c][:-9])
	print("The following dates were not present:")
	for r in range(len(DATE)):
		if data.find(DATE[r]) == -1:
			print(DATE[r])
