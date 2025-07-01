from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notice, Location
from .forms import NoticeForm

@login_required
def upload_notice(request):
    location = request.user.profile.location

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.location = location
            notice.save()
            return redirect('upload_notice')
    else:
        form = NoticeForm()
    return render(request, 'notice/upload_notice.html', {'form': form})

def view_notices(request):
    location_id = request.GET.get('location')
    notices = Notice.objects.filter(location_id=location_id) if location_id else None
    locations = Location.objects.all()
    return render(request, 'notice/view_notices.html', {'notices': notices, 'locations': locations})
