from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from .models import ContactDetails
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
from pages.models import HomePage, ServicesPage, PortfolioPage, AboutPage, TeamPage

class IndexPageView(TemplateView):

    def get(self, request, **kwargs):
        context = {}
        context['banner'] = HomePage.objects.all()[0]
        print context['banner'], context['banner'].banner_text
        context['services'] = ServicesPage.objects.all()
        context['portfolios'] = PortfolioPage.objects.all()
        context['about'] = AboutPage.objects.all()
        context['team'] = TeamPage.objects.all()
        return render(request, 'index.html', context=context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        number = request.POST.get('phone', False)
        message = request.POST.get('message', False)
        if name and email and number and message:
            ContactDetails.objects.create(contact_name=name, contact_email=email, contact_number=number, contact_message=message)
            subject = 'New contact form submitted.'
            template = get_template('contactform_email_template.html')
            context = Context({
                'contact_name': name,
                'contact_email': email,
                'contact_message': message,
            })
            content = template.render(context)
            try:
                send_mail(subject, content, email, ['admin@example.com'])
            except BadHeaderError:
                pass
            return render(request, 'index.html', {'success': True})
        return render(request, 'index.html', {'error': True})