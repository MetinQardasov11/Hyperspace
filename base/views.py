from django.shortcuts import render
from services.models import Service
from django.contrib import messages
from blog.models import Blog
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    
    static_content = """
        
        <div class="inner">
            <h1>HyperSpace</h1>
            <p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
            and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
            <ul class="actions">
                <li><a href="#one" class="button scrolly">Learn more</a></li>
            </ul>
        </div>
    
    """
    
    featured_services = Service.objects.filter(is_featured=True)
    latest_blogs = Blog.objects.all()[:3]
    
    context = {
        'static_content' : static_content,
        'services' : featured_services,
        'latest_blogs' : latest_blogs
    }
    return render(request, 'base/index.html', context)


def contact(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"Hyperspace Contact From"
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        recipient_list = [settings.EMAIL_HOST_USER]
        
        try:
            send_mail(subject, message_body, email, recipient_list)
        except Exception:
            messages.error(request, 'An error occurred while sending the email. Please try again later.')
        else:
            messages.success(request, 'Your message has been sent successfully!')
    
    return HttpResponseRedirect(reverse('base:index') + '#three')