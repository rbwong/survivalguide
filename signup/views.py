from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from signup.models import Contact


class IndexView(TemplateView):
    template_name = "index.html"


class SignupPage(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'signup.html'
    success_message = "You have successfuly registered for Bloc Shot 2014 :)"

    def get_success_url(self):
        return reverse_lazy('signup_page')

    def get_context_data(self, **kwargs):
        context = super(SignupPage, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.designer = self.request.user
        return super(SignupPage, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))
