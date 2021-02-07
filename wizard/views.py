from django.shortcuts import render, get_object_or_404, redirect
from training.models import CustomImages
from training.forms import wizard_form
# Create your views here.


def wizard(request):
    form = wizard_form()
    user = request.user
    disc = CustomImages.objects.all().filter(user=user)
    if request.method == "POST":
        log = wizard_form(
            request.POST, request.FILES)
        if log.is_valid():
            newlog = log.save(commit=False)
            newlog.user = user
            newlog.save()

    return render(request, 'wizard.html', {'form': form, 'disc': disc})


def deletedisipline(request, pk):
    item = get_object_or_404(CustomImages, pk=pk)
    item.delete()

    return redirect('wizard')
