from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from .models import Student, City, Course


# from django.contrib.auth.models import User,auth
#
# from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        u_name = request.POST.get('nmt')
        u_email = request.POST.get('emt')
        u_password = request.POST.get('pmt')
        # password1 = request.POST.get('pmt')
        # if password != password1:
        #     return HttpResponse("your password and confirm password is not same")
        #
        # my_user = User.objects.create_user(uname, email, password)
        # my_user.save()
        # data  = User.objects.all()
        # print(data)
        if User.objects.filter(username=u_name, email=u_email, password=u_password).exists():

            return render(request, 'signup.html', {'data': "user name is alraedy exit"})
        else:

            u1 = User.objects.create_user(username=u_name, email=u_email, password=u_password)
            u1.save()
            print('data saved')
            return render(request, 'login.html')


        # return redirect('login')
        # return HttpResponse("user has beeen crated successfully")

    return render(request, 'signup.html')


def loginaction(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user1 = authenticate(username=username, password=password)
        if user1 is not None:
            login(request, user1)
            return redirect('home')


        else:
            return HttpResponse("invalid credintials")
            # return redirect('login_up')

    else:
        return render(request, 'login.html')


def display(request):
    return render(request, 'display.html')


def add(request):
    return render(request, 'add.html')


from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404

def main(request):
    try:
        s_name = request.POST['dj']
        s_age = int(request.POST['dj2'])
        s_phn = request.POST['dj3']
        s_city_name = request.POST['dj4']
        s_course_name = request.POST['dj5']

        # Get or create a City instance based on the city name
        s_city, created_city = City.objects.get_or_create(City_Name=s_city_name)

        # Get or create a Course instance based on the course name
        s_course, created_course = Course.objects.get_or_create(Course_Name=s_course_name)

        s1 = Student()
        s1.Stud_Name = s_name
        s1.Stud_AGE = s_age
        s1.Stud_Phn = s_phn
        s1.Stud_City = s_city
        s1.Stud_Course = s_course
        s1.save()

        return HttpResponse("Inserted successfully")
    except Exception as e:
        return HttpResponse(f"Error: {e}")


    # return  HttpResponse(f"Name is{obj.}<br> age is {obj.age}<br>roll is {obj.rollno}")


def display_fun(request):
    print("called")
    s1 = Student.objects.all()
    return render(request, 'display.html', {"Data": s1})


def update_fun(request,id):
    s1=Student.objects.get(id=id)     #first id is coumn name and second one is parameter value
    # return HttpResponse(f" id={s1.id}<br> Name:{s1.Name}<br> Age:{s1.Age}<br> city:{s1.city}")
    if request.method =='POST':
        s1.Name =request.POST['dj']
        s1.Age =request.POST['dj2']
        s1.Age =request.POST['dj3']
        s1.city =request.POST['dj4']
        s1.city =request.POST['dj5']
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data':s1})



def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')

def search(request):
    if request.method=="POST":
        data=request.POST['query']
        allpost=Student.objects.filter(Stud_Name__icontains=data)
       

        params={"allpost":allpost}

        return render(request,'search.html',params)

    else:
        return render(request,'home.html',{'data':"PAGE NOT FOUND"})
