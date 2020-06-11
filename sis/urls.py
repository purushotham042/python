from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.Home, name="home-page"),
    url(r'^signup/', views.Signup, name="signup"),
    url(r'^delete/(?P<id>\d+)', views.Delete, name="delete"),
    url(r'^update/(?P<id>\d+)', views.Update, name="update"),
    url(r'^addphone/(?P<id>\d+)', views.AddPhone, name="addphone"),
    url(r'^updatephone/(?P<id>\d+)', views.UpdatePhone, name="updatephone"),
    url(r'^addcourse/', views.AddCourse, name="addcourse"),
    url(r'^usercourse/(?P<id>\d+)', views.UserCourse, name="usercourse"),
    url(r'^displaycourse/', views.DisplayCourse, name="displaycourse"),
    url(r'^deletecourse/(?P<userid>\d+)/(?P<courseid>\d+)', views.DeleteCourse, name="deletecourse"),
    url(r'^displayapi/', views.DisplayViews.as_view(), name="displayapi"),
    url(r'^displayapi/(?P<pk>\d+)', views.DisplayViews.as_view(), name="update"),
    #url('course-list/', CourseListView.as_view(), name='course_list'),


]