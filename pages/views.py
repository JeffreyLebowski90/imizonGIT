from django.shortcuts import render
from .forms import TestForm

# Create your views here.

def home(request):
	my_form = TestForm()
	context = {
		"form": my_form,
	}
	return render(request, 'home.html', context)

def search(request):
	my_form = SearchForm()
	my_result = "checking..."
	my_width = "width: 50%"
	if request.method == "POST":
		my_form = SearchForm(request.POST)
		print(my_form)
		if my_form.is_valid():
			result = my_form.cleaned_data.get("search_bar")
			my_width = "width: " + str(result) + "%"
			if result>3:
				my_result = "bene!"
			else:
				my_result = "male"
	context = {
		"form": my_form,
		"result": my_result,
		"line_width": my_width
	}
	return render(request, "search.html", context)