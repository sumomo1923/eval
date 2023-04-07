from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Student, AudioFile, Score, Eval_item
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def student_list(request):
    page = request.GET.get('page', '1')  # 페이지
    item_list = Eval_item.objects.order_by('my_id')
    paginator = Paginator(item_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'item_list': page_obj}
    return render(request, 'eval/student_list.html', context)

def audio_list(request, item_id):

    item_by_num = Eval_item.objects.filter(id=item_id)
    student_num = AudioFile.objects.filter(item=item_id).order_by('student_number')

    eval_item_type = ''

    for audio_file in student_num:
        eval_item_type = audio_file.item_type

    eval_item_name = ''

    for audio_file in item_by_num:
        eval_item_name = audio_file.item_text

    if request.method == 'POST':
        student_name = request.POST['student_name']
        student = Student.objects.get(name=student_name)
        eval_item_name = Eval_item.objects.get(item_text=eval_item_name)

        std = Score()
        std.user = request.user
        std.student = student
        std.eval_item = eval_item_name
        std.rating_un = request.POST['rating_un']
        std.rating_fu = request.POST['rating_fu']
        std.rating_ac = request.POST['rating_ac']
        std.rating_ph = request.POST.get('rating_ph', 9)
        std.rating_accent = request.POST.get('rating_accent', 9)
        std.rating_rule = request.POST.get('rating_rule', 9)
        std.rating_speed = request.POST.get('rating_speed', 9)
        std.rating_pause = request.POST.get('rating_pause', 9)
        std.save()

    context = {'item_by_num': item_by_num,
               'student_num': student_num,
               'eval_item_name': eval_item_name,
               'eval_item_type': eval_item_type}
    return render(request, 'eval/audio_list.html', context)
