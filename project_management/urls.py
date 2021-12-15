"""project_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

from project.views import home, new_project ,new_project_submission ,student, project_delete,project_update,project_update_submission, viewall ,selection,selection_update,report_selection_update,error,search,watchlist,addwatchlist,deletewatchlist
from users.views import registerPage, loginPage, logoutUser

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    #teacher
    path('teacher/viewall/', viewall, name='viewall'),
    path('selection/<str:pk>',selection, name='selection'),
    path('selection_update/<str:pk>',selection_update, name='selection_update'),
    path('report_selection_update/<str:pk>',report_selection_update, name='report_selection_update'),
    path('media/', error, name='error'),
    path('search', search, name='search'),
    path('watchlist', watchlist, name='watchlist'),
    path('addwatchlist', addwatchlist, name='addwatchlist'),
    path('deletewatchlist/<str:pk>', deletewatchlist, name='deletewatchlist'),
    #student
    path('student/home', home, name='home'),
    path('', home, name='home'),
    path('projectadd/', new_project, name='new_project'),
    path('projectadd/project_submission', new_project_submission, name='new_project_submission'),
    path('student/<str:pk>/', student, name='student'),
    path('update/<str:pk>/', project_update, name='project_update'),
    path('delete/<str:pk>/', project_delete, name='project_delete'),
    path('project_update_submission/<str:pk>', project_update_submission, name='project_update_submission'),
    #user
    path('register/',registerPage,name='registerPage'),
    path('login/',loginPage,name='loginPage'),
    path('logout/',logoutUser,name='logout'),
]
if settings.DEBUG:
    urlpatterns+=[url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,})]
