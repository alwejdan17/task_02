from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msg_1(request):

	context={
	'msg':"Hello World!"
	}
	return render(request,'hello_world.html',context)
