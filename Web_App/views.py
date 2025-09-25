from django.shortcuts import render, redirect
from django.http import HttpResponse, request
import os
import pickle


from .models import *



from .BlockChain import BlockChain


if os.path.exists('bc_voting.pkl'):
    with open('bc_voting.pkl', 'rb') as f:
        bc = pickle.load(f)
else:
    bc=BlockChain()

    



def home(request):
    return render(request, 'index.html')


def userhomedef(request):
    if "uid" in request.session:
        uid = request.session["uid"]
        d = users.objects.filter(email__exact=uid)
        return render(request, 'user_home.html', {'data': d[0]})

    else:
        return render(request, 'user.html')


def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')


def userlogoutdef(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, 'user.html')


def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')


def adminlogindef(request):
    return render(request, 'admin.html')


def userlogindef(request):
    return render(request, 'user.html')


def signupdef(request):
    return render(request, 'signup.html')


def usignupactiondef(request):
    uid = request.POST['uid']
    email = request.POST['mail']
    pwd = request.POST['pwd']
    ph = request.POST['ph']
    addr = request.POST['addr']
    name = request.POST['name']

    d = users.objects.filter(email__exact=uid).count()
    if d > 0:
        return render(request, 'signup.html', {'msg': "Account already registered"})
    else:
        d = users(name=name, email=email, pwd=pwd, uid=uid, contact=ph,address=addr)
        d.save()
        return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})

    return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})

def userloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['mail']
        pwd = request.POST['pwd']
        d = users.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()

        if d > 0:
            d = users.objects.filter(email__exact=uid)
            import random as r

            otp=str(r.randint(99999,999999))

            print(otp)
            sub='Login OTP'
            body='Hello..\n\nLogin OTP:\n\n'+str(otp)
            from .EmailBot import sendEmail
            sendEmail(uid, sub,body)
            

            return render(request, 'otp.html', {'otp': otp, 'uid':uid})

        else:
            return render(request, 'user.html', {'msg': "Login Fail"})

    else:
        return render(request, 'user.html')



def otpverify(request):
    if True:
        otp_o=request.POST['otp_o']
        otp=request.POST['otp']
        uid=request.POST['uid']
        if otp_o==otp:
            d=users.objects.filter(email__exact=uid)
            request.session['uid']=uid
            request.session['name']=d[0].name


            return render(request, 'user_home.html',{'data': d})
        else:
            return render(request, 'user.html',{'msg':"OTP Verification is failed !! "})


    else:
        return redirect('userlogout')




def adminloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')


def viewelections(request):
    
    d=election.objects.filter(stz='Active')

    return render(request, 'viewelections.html',{'data': d})



def addelection(request):
    if request.method == 'POST':
        name = request.POST['name']
        addr = request.POST['addr']
        d = election(name=name, location=addr, stz="Active")
        d.save()

        return render(request, 'addelection.html', {'msg': "Operation done !! "})

    else:
        return render(request, 'addelection.html')


def addcandidate(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        name = request.POST['name']
        party = request.POST['party']
        born = request.POST['born']
        edu = request.POST['edu']
        des = request.POST['des']
        photo = request.POST['photo']
        sym = request.POST['sym']
        
        d = candidates(eid=eid, cname=name, party=party, born=born, education=edu, description=des, photo=photo, symbol=sym, stz="Active")
        d.save()


        d=election.objects.all()


        return render(request, 'addcandidate.html', {'msg': "Operation done !! ", 'data':d})

    else:
        d=election.objects.all()
        return render(request, 'addcandidate.html',{'data':d})



def addannouncement(request):
    if request.method == 'POST':
        from .Dates import get
        dat_e=get()
        cont = request.POST['cont']
        d = announcement(dat_e=dat_e, announcement=cont, stz="Active")
        d.save()

        d=announcement.objects.all()

        return render(request, 'addannouncement.html', {'msg': "Operation done !! ", 'data':d})

    else:
        d=announcement.objects.all()
        return render(request, 'addannouncement.html', { 'data':d})





def addfeedback(request):
    if request.method == 'POST':
        feed = request.POST['feed']
        uid = request.session["uid"]
        name = request.session["name"]
        d = feedback(feedback=feed, name=name, uid=uid)
        d.save()
        return render(request, 'addfeedback.html', {'msg': 'Feedback  Posted Successfully !!'})
        
        
    else:
        return render(request, 'addfeedback.html',)
        


def viewfeedback(request):
    if "adminid" in request.session:
        d = feedback.objects.all()

        return render(request, 'viewfeedback.html', { 'data': d})
    else:
        return redirect('userlogout')



def viewannouncement(request):
    if "uid" in request.session:
        
        d = announcement.objects.all()

        return render(request, 'viewannouncement.html', { 'data': d})
    else:
        return redirect('userlogout')



def uviewelections(request):
    
    d=election.objects.filter(stz='Active')

    return render(request, 'uviewelections.html',{'data': d})


def uannouncement(request):
    d=announcement.objects.all()
    return render(request, 'uannouncement.html', { 'data':d})




def aviewcandidates(request):
    if request.method == 'GET':
        eid = request.GET['eid']
        
        d = candidates.objects.filter(eid=eid).all()
        for d1 in d:
            print(d1.cname)


        return render(request, 'aviewcandidates.html',{'data':d})

    else:
        pass


def vote(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        uid = request.session["uid"]
        vote = request.POST["vote"]
        d = records.objects.filter(eid=eid).filter(user=uid).count()
        if d>0:
            return render(request, 'user_home.html', {'msg': 'You already participated in this voting !! '})
        else:
            
            bc.add_block([{'citizen':uid,'eid':eid,'vote': vote}])
            with open('bc_voting.pkl', 'wb') as f:
                pickle.dump(bc, f)
            d = records(eid=eid,user=uid)
            d.save()
            return render(request, 'user_home.html', {'msg': 'Thank you for your voting !! '})
    else:
        eid = request.GET['eid']
        d = candidates.objects.filter(eid=eid)
        return render(request, 'vote.html',{'data':d})


def viewresults(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        from .LoabBloackChain2 import load

        r=load(eid)
        print(r)

        from .Freq import CountFrequency
        d1=CountFrequency(r)

        print(d1)

        d=[]
        for d11 in d1:
            data=candidates.objects.filter(id=int(d11))
            d2={'name':data[0].cname, 'party':data[0].party, 'votes':d1[d11]}
            d.append(d2)

        
        return render(request, 'viewresults2.html',{'data':d})
        
    else:
        eid = request.GET['eid']
        from .LoabBloackChain import load
        r=load()
        return render(request, 'viewresults.html', {'data': r, 'eid':eid})
        

        

        
