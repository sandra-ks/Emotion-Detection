from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
import base64
from fer import FER
import cv2
def home(request):
	if request.user.is_active :
		return redirect('dashboard')
	return render(request,"home.html")

def userlogin(request):
	if request.user.is_active :
		return redirect('dashboard')
	else:
		if request.method == 'POST':

			username = request.POST.get('username')
			password = request.POST.get('pass')
			
			
			user=authenticate(username=username,password=password)
			
			if user is not None:

				if user.is_active:

					login(request, user)
					return redirect('dashboard')
			else:
				messages.error(request,'Enter Valid Credentials')
				print('Hi')
				return redirect('login')
			
		return render(request,"login.html")

def signup(request):
	if request.user.is_active :
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			email = request.POST.get('email')
			password1 = request.POST.get('pass1')
			password2 = request.POST.get('pass2')
			password=make_password(password1)
			ob=User.objects.create(username=username,email=email,password=password)
			messages.success(request,'Your Account Has Been Created Please Login')
			return redirect('login')
		return render(request,"signup.html")

@login_required
def dashboard(request):
	return render(request,"dashboard.html")

@login_required
def view_kids(request):
	ob = Kids.objects.filter(guardian=request.user)
	if request.method == 'POST':
		name = request.POST.get('kname')
		age = request.POST.get('kage')
		ob= Kids.objects.create(guardian=request.user,name=name,l1acc='100',l2acc='100',l3acc='100',age=age,level='Not Started',status='Not Started',index=len(ob)+1)
		ob.save()
		return redirect('view-kids')
	context={
	'kid': Kids.objects.filter(guardian=request.user)
	}
	return render(request,"view_kids.html",context)


@login_required
def userlogout(request):
    logout(request)
    return redirect('login')

@login_required
def selkid(request):
	context={
	'kid': Kids.objects.filter(guardian=request.user)
	}
	return render(request,"selkid.html",context)


@login_required
def trainkid(request,id):

	ob=Kids.objects.get(id=id)

	if ob.status == 'Not Started' or ob.status == None:
		ob.status= 'Training Started'
		ob.save()

	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=id)
		ob2.status = 'Training Completed'
		ob2.training= True
		ob2.save()
		return redirect('dashboard')

	context={
	'kid': Kids.objects.get(id=id)
	}
	
	return render(request,"trainkid.html",context)


@login_required
def selkid2(request):
	context={
	'kid': Kids.objects.filter(guardian=request.user)
	}
	return render(request,"selkid2.html",context)

@login_required
def test(request):
	return render(request,"test.html")

@login_required
def gamelevel(request,id):
	obc=Counter.objects.get(id=1)
	obc.count=int(obc.count)+1
	obc.save()
	

	context={
	'kid': Kids.objects.get(id=id)
	}
	return render(request,"gamelevel.html",context)

@login_required
def level1(request,id):
	ob=Kids.objects.get(id=id)

	obc=Counter.objects.get(id=1)

	val=int(obc.count)
	print(val)
	if val % 7 == 0:
		l1=Level1.objects.get(index='1')
	elif val % 7 == 1:
		l1=Level1.objects.get(index='2')
	elif val % 7 == 2:
		l1=Level1.objects.get(index='3')
	elif val % 7 == 3:
		l1=Level1.objects.get(index='4')
	elif val % 7 == 4:
		l1=Level1.objects.get(index='1')
	elif val % 7 == 5:
		l1=Level1.objects.get(index='2')
	elif val % 7 == 6:
		l1=Level1.objects.get(index='3')
	else:
		l1=Level1.objects.get(index='4')

	if ob.status == 'Training Started':
		ob.status= 'Level 1 Started'
		ob.save()

	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=id)
		ob2.status = 'Level 1 Completed'
		ob2.l1= True
		ob2.save()
		return redirect('/select-level/'+ str(ob2.id))
	context={
	'kid': Kids.objects.get(id=id),
	'l1':l1
	}
	return render(request,"level1.html",context)

@login_required
def level1acc(request):
	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=kid)
		acc=ob2.l1acc
		ob2.l1acc = int(acc) - 10
		ob2.save()

	return HttpResponse('Success')

@login_required
def status_view(request,id):
	context={
	'kid': Kids.objects.get(id=id)
	}
	return render(request,"status.html",context)


@login_required
def level2(request,id):

	ob=Kids.objects.get(id=id)

	obc=Counter.objects.get(id=1)
	val=int(obc.count)
	print(val)
	if val % 7 == 0:
		l1=Level2.objects.get(index='1')
	elif val % 7 == 1:
		l1=Level2.objects.get(index='1')
	elif val % 7 == 2:
		l1=Level2.objects.get(index='1')
	elif val % 7 == 3:
		l1=Level2.objects.get(index='1')
	elif val % 7 == 4:
		l1=Level2.objects.get(index='1')
	elif val % 7 == 5:
		l1=Level2.objects.get(index='1')
	elif val % 7 == 6:
		l1=Level2.objects.get(index='1')
	else:
		l1=Level2.objects.get(index='1')

	if ob.status == 'Level 1 Completed':
		ob.status= 'Level 2 Started'
		ob.save()

	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=id)
		ob2.status = 'Level 2 Completed'
		ob2.l2= True
		ob2.save()
		return redirect('/select-level/'+ str(ob2.id))
	context={
	'kid': Kids.objects.get(id=id),
	'l1':l1
	}
	return render(request,"level2.html",context)


@login_required
def level2acc(request):
	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=kid)
		acc=ob2.l3acc
		ob2.l3acc = int(acc) - 10
		ob2.save()

	return HttpResponse('Success')


@login_required
def level3(request,id):

	ob=Kids.objects.get(id=id)
	obc=Counter.objects.get(id=1)
	obc.count=int(obc.count)+1
	obc.save()
	val=int(obc.count)
	print(val)
	if val % 7 == 0:
		l1=Level3.objects.get(id='1')
	elif val % 7 == 1:
		l1=Level3.objects.get(id='2')
	elif val % 7 == 2:
		l1=Level3.objects.get(id='3')
	elif val % 7 == 3:
		l1=Level3.objects.get(id='4')
	elif val % 7 == 4:
		l1=Level3.objects.get(id='5')
	elif val % 7 == 5:
		l1=Level3.objects.get(id='6')
	elif val % 7 == 6:
		l1=Level3.objects.get(id='7')
	else:
		l1=Level3.objects.get(id='1')
	

	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=id)
		ob2.status = 'Level 3 Completed'
		ob2.l3= True
		ob2.save()
		return redirect('/select-level/'+ str(ob2.id))
	context={
	'kid': Kids.objects.get(id=id),
	'l1':l1
	}
	return render(request,"level3.html",context)


@login_required
def level3acc(request):
	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=kid)
		acc=ob2.l3acc
		ob2.l3acc = int(acc) - 10
		ob2.save()

	return HttpResponse('Success')

@login_required
def vids_class(request):
	if request.method == 'POST':
		img = request.POST.get('cfile')
		name = request.POST.get('name')
		emot = request.POST.get('emot')
		imglst=img.split(',')
		imgdata = base64.b64decode(imglst[1])
		filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
		with open(filename, 'wb') as f:
		    f.write(imgdata)
		emotion_detector = FER(mtcnn=True)
		test_img = cv2.imread(filename)
		analysis = emotion_detector.detect_emotions(test_img)
		dominant_emotion, emotion_score = emotion_detector.top_emotion(test_img)
		result=analysis[0]["emotions"]
		print(result['surprise'])
		if result[emot] > 0.2:
			ob=Level3.objects.create(name=name,string=result[emot],emot=emot)
			ob.save
			return HttpResponse('Success')
		else:
			return HttpResponse('Fail')


@login_required
def reset(request):
	if request.method == 'POST':
		kid = request.POST.get('kid')
		ob2= Kids.objects.get(id=kid)
		ob2.l1=False
		ob2.l2=False
		ob2.l3=False

		ob2.l1acc = '100'
		ob2.l2acc = '100'
		ob2.l3acc = '100'
		ob2.save()

	return HttpResponse('Success')
