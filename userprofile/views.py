from django.shortcuts import render_to_response
from userprofile.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from forms import UserProfileForm

@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin')
	else:
		user = request.user
		profile = user.profile

		# instance pre-populates any existing data from the models
		form = UserProfileForm(instance=profile)	

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('profile.html', args)