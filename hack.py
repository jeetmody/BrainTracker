import json

webdata = open("file1.txt", "r")
android_data = open("file2.csv", "r")
result = [1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1]
#print len(result)
web=[]
for i in webdata:
	x,y = i.split(",")
	x = int(x)
	y = int(y)
	web.append([x,y])
print web


android = {}
for i in android_data:

	separated = i.strip().split("\t")
	if len(separated) != 6:
		continue

	t = int(separated[1])
	if(t in android):
		continue

	if len(separated[2]) == 0:
		continue

	alpha = map(float,separated[2].strip().split(","))

	alphaAvg = 0.0
	for i in alpha:
		alphaAvg=alphaAvg+(i)
	alphaAvg=alphaAvg/4
	beta = map(float,separated[3].strip().split(","))
	betaAvg = 0.0
	for i in beta:
		betaAvg=betaAvg+(i)
	betaAvg=betaAvg/4
	delta = map(float,separated[4].strip().split(","))
	deltaAvg = 0.0
	for i in delta:
		deltaAvg=deltaAvg+(i)
	deltaAvg=deltaAvg/4
	gamma = map(float,separated[5].strip().split(","))
	gammaAvg = 0.0
	for i in gamma:
		gammaAvg=gammaAvg+(i)
	gammaAvg=gammaAvg/4
	rAvg = 0.0
	for i in xrange(4):
		if(float(beta[i])==0.0):
			beta[i] = 0.0001
		rAvg = rAvg + float(alpha[i])/float(beta[i])
	rAvg /= 4
	android[t] =[alphaAvg,betaAvg,gammaAvg,deltaAvg,rAvg]

print android
k = 0
z = 0
webDict = {}
final = {}
for i in range(web[0][1],web[len(web)-1][1]+1):
	if(web[k+1][1]==i):
		k=k+1
	webDict[i]=k+1
f = open("train.csv","w")

for i in webDict:
	if(i in android):

		final[int(i)] = [(android[i][0]),android[i][1], (android[i][2]), (android[i][3]),(android[i][4]), (result[webDict[i]-1])]

		f.write(str(android[i][0])+","+str(android[i][1])+","+str(android[i][2])+","+str(android[i][3])+","+str(android[i][4])+","+str(result[webDict[i]-1])+"\n")


a = (min(final))
ff = {}
for i in final:
	ff[i-a] = final[i]

print json.dumps(ff, ensure_ascii=False)


''' 


for i in xrange(length(webdata)):
	d = webdata[i+1][1] - webdata[i][1]
	for j in xrange(d):
		newAlphaAvg[k] + = android[z][0]
		newDeltaAvg[k] + = android[z][1]
		newGammaAvg[k] + = android[z][2]
		newDeltaAvg[k] + = android[z][3]
		z = z+1
	newAlphaAvg[k] = newAlphaAvg[k]/d
	newBetaAvg[k] = newBetaAvg[k]/d
	newDeltaAvg[k] = newDeltaAvg[k]/d
	newGammaAvg[k] = newGammaAvg[k]/d
	k = k+1
'''