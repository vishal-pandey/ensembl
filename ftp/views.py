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

	files = 0
	dirs = 0

	output = []
	for x in data:
		y = x.split()
		connector = '/'
		if request.GET['path'] == '/' or request.GET['path'][-1] == '/':
			connector = ''
		vdict = {}
		if x[0] == '-':
			vdict['url'] = 'ftp://ftp.ensembl.org/pub/release-95'+str(request.GET['path'])+connector+str(y[8])
			vdict['type'] = 'file'
			files = files+1
		elif x[0] == 'd':
			vdict['url'] = 'https://ensembl.vishalpandey.xyz/?path='+str(request.GET['path'])+connector+str(y[8])
			vdict['type'] = 'dir'
			dirs = dirs+1
		vdict['size'] = int(y[4])
		vdict['date_modified'] = y[5]+" "+y[6]+" "+y[7]
		vdict['name'] = str(y[8])
		
		output.append(vdict)

	result = {}
	result['self'] = 'https://ensembl.vishalpandey.xyz/?path='+str(request.GET['path'])
	result['files'] = files
	result['dirs'] = dirs
	result['data'] = output
	return HttpResponse(json.dumps(result))
