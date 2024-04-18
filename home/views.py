from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from home.models import subrequest
from django.contrib import messages
from .models import ServiceRequest
from .models import Profile

# Create your views here.
def index(request):
    context = {
        'variable':'this is sent'
    }
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def subreq(request):
    if request.method == 'POST':
        # Get form data
        fname = request.POST.get("fname")
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        service_type = request.POST.get('service_type')
        details = request.POST.get('details')
        submit=subrequest(fname=fname,lname=lname,email=email,service_type=service_type,details=details)
        submit.save()
        messages.success(request, "Saved Successfully")
    return render(request, 'subreq.html')

def trackreq(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        request_details = request.POST.get('email')
        # ServiceRequest.objects.create(customer_name=customer_name, request_details=request_details)
        existing_request = ServiceRequest.objects.filter(customer_name=customer_name, status='Pending').first()
        if existing_request:
            # Update existing request instead of creating a new one
            existing_request.request_details = request_details
            existing_request.save()
        else:
            # Create new request
            ServiceRequest.objects.create(customer_name=customer_name, request_details=request_details)
        return redirect('reqlist')
    return render(request, 'trackreq.html')
    return render(request, 'trackreq.html')

def viewacc(request):
    return render(request, 'account_info.html')

def reqlist(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'reqlist.html', {'requests': requests})

def updatestatus(request, request_id):
    service_request = get_object_or_404(ServiceRequest, pk=request_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        service_request.status = new_status
        service_request.save()
        return redirect('reqlist')
    
        return render(request, 'update_status.html', {'trackreq': trackreq})
    
def account_info(request, account_number):
    customer = Profile.objects.get(account_number=account_number)
    return render(request, 'customer_accounts/account_info.html', {'customer': customer})





