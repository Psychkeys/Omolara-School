from django.shortcuts import render, redirect
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
# Create your views here.



def newsletter(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful!')
            return redirect('newsletter')
    else:
        form = SubscibersForm()
    context = {

        'form':form,   
    }
    return render(request, 'letter/newsletter.html', context)



def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames = ['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently= False,
            )
            messages.success(request, 'Message has been sent to the MailList')
            return redirect('mail_letter')
    else:
        form = MailMessageForm()
    form = MailMessageForm
    context = {
        'form':form,
    }
    return render(request, 'letter/mail_letter.html', context)
