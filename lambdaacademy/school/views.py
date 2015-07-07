from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Module, Participant
from .forms import RegisterForm

def home(request):
	all_modules = get_list_or_404(Module)
	context = {'all_modules' : all_modules}
	context['page'] = 'home'
	return render(request, 'school/pages/home.html', context)

def registration(request, module_id):
	module = get_object_or_404(Module, pk = module_id)
	context = {}
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			course_registered = form.cleaned_data['course_registered']
			f_name = form.cleaned_data['f_name']
			l_name = form.cleaned_data['l_name']
			email = form.cleaned_data['email']
			contact_number = form.cleaned_data['contact_number']
			best_suited_time = form.cleaned_data['best_suited_time']
			comment = form.cleaned_data['comment']

			p = Participant(f_name = f_name, l_name = l_name, email = email,
				contact_number = contact_number, best_suited_time = best_suited_time,
				course_registered = course_registered, comment = comment)
			p.save()
			course_registered.current_participants = course_registered.current_participants + 1
			course_registered.save()

			return HttpResponseRedirect('/success/')
	else:
		form = RegisterForm(initial={'course_registered': module})
	context['page'] = 'register'
	context['form'] = form
	return render(request, 'school/pages/registration.html', context)

def success(request):
	return render(request, 'school/pages/success.html', {})

def about(request):
	context = {}
	context['page'] = 'about'
	return render(request, 'school/pages/about.html', context)

def detail(request,module_id):

	module = get_object_or_404(Module, pk = module_id)
	context = {}
	context['module'] = module
	num_of_seats = module.max_participants - module.current_participants
	if num_of_seats > 0:
		context['availability'] = True
	else:
		context['availability'] = False
	context['num_of_seats'] = num_of_seats
	return render(request, 'school/pages/module_detail.html', context)