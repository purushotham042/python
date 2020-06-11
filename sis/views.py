from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def Home(request):
    students = models.STUDENT.objects.all()
    return render(request, 'home.html', {'students':students})


def Signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        qualification = request.POST['qualification']
        mail_id = request.POST['mail']
        duration = request.POST['du']
        joining_date = request.POST['join']
        paid_amount = request.POST['paid']
        balance = request.POST['balance']

        stu = models.STUDENT(
            name=name,
            age=age,
            qualification=qualification,
            mail_id=mail_id,
            duration=duration,
            joining_date=joining_date,
            paid_amount=paid_amount,
            balance_amount=balance
        )
        stu.save()
    return render(request, 'signup_form.html')


def Delete(request, id):
    print('id = ', id)
    student = models.STUDENT.objects.get(id=id)
    student.delete()
    print(student.name)
    return redirect('home-page')


def Update(request, id):
    if request.method == 'POST':
        student = models.STUDENT.objects.get(id=request.POST['id'])
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.qualification = request.POST['qualification']
        student.mail_id = request.POST['mail']
        student.duration = request.POST['du']
        student.joining_date = request.POST['join']
        student.paid_amount = request.POST['paid']
        student.balance_amount = request.POST['balance']
        student.save()
        return redirect('home-page')
    else:
        student = models.STUDENT.objects.get(id=id)
    return render(request, 'update_form.html', {'student':student})


def AddPhone(request, id):
    if request.method == 'POST':
        id = request.POST['id']
        stu = models.STUDENT.objects.get(id=id)
        phone = models.PHONE(ph_number=request.POST['phone'], ph=stu)
        phone.save()
        phones = stu.phone_set.all()
        return render(request, 'add_phone.html', {'student': stu, 'phones': phones})
    else:
        stu = models.STUDENT.objects.get(id=id)
        phones = stu.phone_set.all()
        return render(request, 'add_phone.html', {'student': stu, 'phones': phones})


def UpdatePhone(request, id):
    if request.method == 'GET':
         phone = models.PHONE.objects.get(id=id)
         return render(request, 'update_number.html', {'phone':phone})
    else:
        phone = models.PHONE.objects.get(id=id)
        phone.ph_number = request.POST['ph']
        phone.save()
        return HttpResponse('phone number updated')


def AddCourse(request):
    if request.method == 'POST':
        course = models.COURSES(courses=request.POST['course'])
        course.save()
        cr = models.COURSES.objects.all()
        return render(request, 'add_coures.html', {'courses':cr})
    else:
        cr = models.COURSES.objects.all()
        return render(request, 'add_coures.html', {'courses': cr})


def UserCourse(request, id):
    if request.method == 'GET':
         user = models.STUDENT.objects.get(id=id)
         stu_courses = user.courses_set.all()
         course = models.COURSES.objects.all()
         return render(request, 'user_course.html', {'student':user, 'courses':course, 'stu_courses':stu_courses})
    else:
        user = models.STUDENT.objects.get(id=id)
        stu_courses = user.courses_set.all()
        print('course = ', request.POST['course'])
        cr = models.COURSES.objects.get(id=request.POST['course'])
        cr.member.add(user)
        cr.save()
        course = models.COURSES.objects.all()
        return render(request, 'user_course.html', {'student': user, 'courses': course, 'stu_courses':stu_courses})


def DisplayCourse(request):
    if request.method == 'GET':
        courses = models.COURSES.objects.all()
        return render(request, 'displaycourse.html', {'courses':courses})
    else:
        courses = models.COURSES.objects.all()
        sc = models.COURSES.objects.get(id=request.POST['course'])
        students = sc.member.all()
        return render(request, 'displaycourse.html', {'courses': courses, 'students':students})


def DeleteCourse(request, userid, courseid):
    print('DeleteCourse ', courseid)
    sc = models.COURSES.objects.get(id=courseid)
    stu = models.STUDENT.objects.get(id=userid)
    stu.courses_set.remove(sc)
    return redirect('usercourse', id=userid)


from rest_framework.views import APIView, View
from .serializers import STUDENTSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404


class DisplayViews(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('pk'):
            pk = kwargs.get('pk')
            stu_saved = get_object_or_404(models.STUDENT.objects.all(), pk=pk)
            serializer = STUDENTSerializer(stu_saved)
            return Response({"students":serializer.data})
        stu = models.STUDENT.objects.all()
        stu = STUDENTSerializer(stu, many=True)
        return Response({'student': stu.data})

    def post(self, request):
        serializer = STUDENTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        stu = get_object_or_404(models.STUDENT.objects.all(), pk=pk)
        serializer = STUDENTSerializer(instance=stu, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            stu_saved = serializer.save()
        return Response({"success": "Article '{}' updated success".format(stu_saved.name)})




