from django.shortcuts import render, redirect, HttpResponse
import random
# Create your views here.
def index(request):
    if 'number' not in request.session or 'count' not in request.session or 'almost' not in request.session or 'almost1' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['count'] = 5
        request.session['almost']
        request.session['almost1'] 
    return render(request, 'index.html')


def form(request):
    try:
        request.session['guess'] = int(request.POST['guess'])
        request.session['count'] -= 1
        request.session['almost'] = request.session['number'] + 5
        request.session['almost1'] = request.session['number'] - 5
        print("session is found : )")
    except:
        print("Not session found : (")
    return redirect('/')


def destroy(request):
    if 'number' in request.session and 'count' in request.session:
        del request.session['number']
        
    return redirect('/')


    # request.session['count'] -=1
    #     if request.session['count'] == 0:
    #         del request.session['number']