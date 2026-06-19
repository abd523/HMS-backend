from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Patient
from .serializers import PatientSerializer

# 1. በአንድ ገጽ ላይ የሚታዩ የዳታዎችን ብዛት መወሰኛ (Pagination)
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # በአንድ ገጽ 10 ታካሚዎች ብቻ እንዲታዩ ያደርጋል
    page_size_query_param = 'page_size'

# 2. የታካሚዎችን CRUD፣ ፍለጋ እና ማጣሪያ በአንድ ላይ የያዘው ViewSet
class PatientViewSet(viewsets.ModelViewSet):
    # አዳዲስ ታካሚዎች መጀመሪያ ላይ እንዲመጡ በ'-created_at' ተደርድረዋል
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientSerializer
    pagination_class = StandardResultsSetPagination

    # የፍለጋ (Search) እና ማጣሪያ (Filter) ዘዴዎችን ማገናኘት
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # በጾታ (Gender) ብቻ ለይቶ ለማውጣት (ለምሳሌ፦ ?gender=Male)
    filterset_fields = ['gender'] 
    
    # በስም ወይም በስልክ ቁጥር ለመፈለግ (ለምሳሌ፦ ?search=0911...)
    search_fields = ['first_name', 'last_name', 'phone_number']