from django.shortcuts import render
from django.http import HttpResponse
from ftplib import FTP
import json

def index(request):
	ftp = FTP('ftp.ensembl.org')
	ftp.login()
	ftp.cwd('pub/release-95')
	path = "."+str(request.GET['path'])
	ftp.cwd(path)
	data = []
	ftp.dir(data.append)

	output = []
	for x in data:
		connector = '/'
		if request.GET['path'] == '/':
			connector = ''
		vdict = {}
		if x[0] == '-':
			vdict['url'] = 'ftp://ftp.ensembl.org/pub/release-95'+str(request.GET['path'])+connector+str(x[56:])
			vdict['type'] = 'file'
		elif x[0] == 'd':
			vdict['url'] = 'https://ensembl.vishalpandey.xyz/?path='+str(request.GET['path'])+connector+str(x[56:])
			vdict['type'] = 'dir'
	  
		vdict['size'] = int(x[28:42])
		vdict['date_modified'] = x[42:56]
		vdict['name'] = x[56:]
		output.append(vdict)

	return HttpResponse(json.dumps(output))
