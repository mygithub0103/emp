from django.shortcuts import render
from win.models import Employee

def search_employees(request):
    search_term = request.GET.get('search', '')  # الحصول على نص البحث من استعلام GET
    results = []
    
    if search_term:
        results = Employee().similar_names(search_term)  # استخدام الدالة للبحث عن الأسماء
    
    return render(request, 'search_results.html', {'results': results, 'search_term': search_term})
