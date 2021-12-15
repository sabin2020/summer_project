from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, Watchlist
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def viewall(request):
    obj = Project.objects.all()
    context = {
            'objects': obj,
            }
    return render(request,"teacher/home.html", context)
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors','Student'])
def error(request):
    return HttpResponse('Not uploded yet')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def selection(request,pk):
    student = Project.objects.get(id=pk)
    context = {
            'student':student
            }
    return render(request,"teacher/selection.html",context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def selection_update(request,pk):
    proposal_reason= request.POST['proposal_reason']
    selected_proposal_condition= request.POST['selected_proposal_condition']
    Project.objects.filter(pk=pk).update(proposal_reason=proposal_reason,selected_proposal_condition=selected_proposal_condition)
    return render(request,"teacher/selection.html")

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def report_selection_update(request,pk):
    report_reason= request.POST['report_reason']
    selected_report_condition= request.POST['selected_report_condition']
    Project.objects.filter(pk=pk).update(report_reason=report_reason,selected_report_condition=selected_report_condition)
    return render(request,"teacher/selection.html")

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def search(request):
    query = request.GET['query']
    student = Project.objects.get(unique_name=query)
    print (student)
    context = {
            'student': student
            }
    return render(request,"teacher/search.html", context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student','Mentors'])
def home(request):
    if request.user.groups.all()[0].name=='Student':
        try:
            student = Project.objects.get(unique_name = request.user.username)
            return render(request,"student/home.html",{'student':student})
        except ObjectDoesNotExist:
            return render(request,"student/home.html")
    else:
        return redirect("/teacher/viewall")


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def watchlist(request):
    watch = Watchlist.objects.filter(teacher = request.user.id)
    return render(request,"teacher/watchlist.html", {'watch': watch})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def addwatchlist(request):
    name = request.POST['unique_name']
    project = Project.objects.get(unique_name = name)
    addwatchlist = Watchlist(teacher = request.user, project=project )
    addwatchlist.save()
    return redirect("/watchlist")

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Mentors'])
def deletewatchlist(request,pk):
    Watchlist.objects.get(id=pk).delete()
    return redirect("/watchlist")

# student_part<++>
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student'])
def new_project_submission(request):
    name = request.POST['name']
    git_url = request.POST["git_url"]
    reference = request.POST["reference"]
    tools = request.POST["tools"]
    if bool(request.FILES.get('proposal_file', False)) == True and bool(request.FILES.get('report_file', False)) == False:
        myfile = request.FILES["proposal_file"]
        # myfile_report = request.FILES["report_file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        # filename = fs.save(myfile_report.name,myfile_report)
        # addproject = Project(user=request.user,unique_name=request.user,name=name,git_url=git_url,references=reference,tools=tools,proposal_file=myfile,report_file=myfile_report)
        addproject = Project(user=request.user,unique_name=request.user,name=name,git_url=git_url,references=reference,tools=tools,proposal_file=myfile)
        addproject.save()
    if bool(request.FILES.get('proposal_file', False)) == True and bool(request.FILES.get('report_file', False)) == True:
        myfile = request.FILES["proposal_file"]
        myfile_report = request.FILES["report_file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        filename = fs.save(myfile_report.name,myfile_report)
        addproject = Project(user=request.user,unique_name=request.user,name=name,git_url=git_url,references=reference,tools=tools,proposal_file=myfile,report_file=myfile_report)
        addproject.save()

    if bool(request.FILES.get('proposal_file', False)) == False and bool(request.FILES.get('report_file', False)) == True:
        myfile_report = request.FILES["report_file"]
        fs = FileSystemStorage()
        select = selected
        print(select)
        filename = fs.save(myfile_report.name,myfile_report)
        addproject = Project(user=request.user,unique_name=request.user,name=name,git_url=git_url,references=reference,tools=tools,report_file=myfile_report)
        addproject.save()

    if bool(request.FILES.get('proposal_file', False)) == False and bool(request.FILES.get('report_file', False)) == False:
        return HttpResponse("Must upload proposal and Name")
    return redirect('/')






@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student'])
def new_project(request):
    return render(request, "student/form.html")






@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student'])
def project_update_submission(request,pk):
    name = request.POST["name"]
    git_url = request.POST["git_url"]
    reference = request.POST["reference"]
    tools = request.POST["tools"]
    # myfile = request.FILES["proposal_file"]
    # myfile_report = request.FILES["report_file"]
    fs = FileSystemStorage()
    if bool(request.FILES.get('proposal_file', False)) == True and bool(request.FILES.get('report_file', False)) == False:
        myfile = request.FILES["proposal_file"]
        filename = fs.save(myfile.name,myfile)
        Project.objects.filter(pk=pk).update(name=name,git_url=git_url,references=reference,tools=tools,selected_proposal_condition="not_verified",proposal_file=myfile)
    if bool(request.FILES.get('proposal_file', False)) == False and bool(request.FILES.get('report_file', False)) == True:
        myfile_report = request.FILES["report_file"]
        filename = fs.save(myfile_report.name,myfile_report)
        Project.objects.filter(pk=pk).update(name=name,git_url=git_url,references=reference,selected_report_condition="not_verified",tools=tools,report_file=myfile_report)
    # filename = fs.save(myfile_report.name,myfile_report)
    if bool(request.FILES.get('proposal_file', False)) == True and bool(request.FILES.get('report_file', False)) == True:
        myfile = request.FILES["proposal_file"]
        filename = fs.save(myfile.name,myfile)
        myfile_report = request.FILES["report_file"]
        filename = fs.save(myfile_report.name,myfile_report)
        Project.objects.filter(pk=pk).update(name=name,git_url=git_url,references=reference,tools=tools,selected_report_condition="not_verified",proposal_file=myfile,report_file=myfile_report)
    if bool(request.FILES.get('proposal_file', False)) == False and bool(request.FILES.get('report_file', False)) == False:
        Project.objects.filter(pk=pk).update(name=name,git_url=git_url,references=reference,tools=tools)

    return redirect('/')







@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student'])
def project_update(request,pk):
    student = Project.objects.get(id=pk)
    context = {
            'student':student
            }
    return render(request, "student/updateform.html",context)






@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student'])
def project_delete(request,pk):
    Project.objects.filter(id=pk).delete()
    return redirect('/')






@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['Student'])
def student(request,pk):
    student = Project.objects.get(id=pk)
    context = {
            'student':student
            }
    return render(request, "student.html", context)
