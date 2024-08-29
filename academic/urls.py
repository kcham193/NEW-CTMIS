from django.urls import path
from .views import LectureNotesView, AssignmentView, ReferenceMaterialView, \
    MaterialCreateView, MaterialUpdateView, MaterialDeleteView, MaterialDetailView

urlpatterns = [
    path('lecture_notes/', LectureNotesView.as_view(), name='lecture_notes'),
    path('assignment/', AssignmentView.as_view(), name='assignment'),
    path('reference_materials/', ReferenceMaterialView.as_view(), name='reference_materials'),
    path('material/create', MaterialCreateView.as_view(), name='create_material'),
    path('material/update/<str:pk>', MaterialUpdateView.as_view(), name='update_material'),
    path('material/delete/<str:pk>', MaterialDeleteView.as_view(), name='delete_material'),
    path('material/detail/<str:pk>', MaterialDetailView.as_view(), name='view_material')
]
 