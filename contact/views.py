from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


# Create your views here.
def contact_view(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"votre message a été envoyé:")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request,'contact/index.html', {'form':form})