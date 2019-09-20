from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from faker import Faker
# Create your views here.
import requests
def index(request):

    return render(request, 'jobs/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        jobs = Job.objects.all()
        for job in jobs:
            if job.name == name:
                data = requests.get(f'http://api.giphy.com/v1/gifs/search?api_key=zAckuQru8VqfxKXUnt3EqtHCYD8veI4K&q={job.past_job}').json() # data 는 dict 타입의 객체!
                picture = data['data'][0]['images']['fixed_width']['url']
                context = {
                    'job' : job,
                    'picture' : picture,
                    }
                return render(request, 'jobs/past_job.html', context)
        
        fake = Faker()
        job = Job()
        job.name = name
        job.past_job = fake.job()
        job.save()  
        data = requests.get(f'http://api.giphy.com/v1/gifs/search?api_key=zAckuQru8VqfxKXUnt3EqtHCYD8veI4K&q={job.past_job}').json() # data 는 dict 타입의 객체!
        picture = data['data'][0]['images']['fixed_width']['url']
        context = {
            'job' : job,
            'picture' : picture,
        }
        return render(request, 'jobs/past_job.html', context)
    else:
        return redirect('articles:index')