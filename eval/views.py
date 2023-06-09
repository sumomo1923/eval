from django.views.decorators.cache import cache_control
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Student, AudioFile, Score, Eval_item
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request, 'eval/home.html')

def test_info(request):
    return render(request, 'eval/test_info.html')

def student_list(request):
    page = request.GET.get('page', '1')  # 페이지
    item_lists = Eval_item.objects.order_by('my_id')
    paginator = Paginator(item_lists, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'item_list': page_obj}
    return render(request, 'eval/student_list.html', context)

def audio_list(request, item_id):

    page = request.GET.get('page', '1')
    student_num = AudioFile.objects.filter(item=item_id).order_by('student_number')
    item_by_num = Eval_item.objects.filter(id=item_id)
    paginator = Paginator(student_num, 10)
    audio_files = paginator.get_page(page)

    eval_item_type = ''

    eval_completed = False

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
        std.rating_ho = request.POST['rating_ho']
        std.rating_un = request.POST.get('rating_un', 9)
        std.rating_fu = request.POST.get('rating_fu', 9)
        std.rating_ac = request.POST.get('rating_ac', 9)
        std.rating_ph = request.POST.get('rating_ph', 9)
        std.rating_accent = request.POST.get('rating_accent', 9)
        std.rating_rule = request.POST.get('rating_rule', 9)
        std.rating_pause = request.POST.get('rating_pause', 9)
        std.eval_completed = True
        std.save()

    scores = Score.objects.filter(user=request.user, eval_item=item_by_num[0])
    eval_completed_dict = {score.student.name: score.eval_completed for score in scores}

    # Update eval_completed_dict for current user
    user_scores = Score.objects.filter(user=request.user, eval_item=item_by_num[0])
    eval_completed_dict.update({score.student.name: score.eval_completed for score in user_scores})

    for audio_file in student_num:
        if audio_file.student_number in eval_completed_dict:
            audio_file.eval_completed = '완료'
        else:
            audio_file.eval_completed = '미완료'
        audio_file.save()

    context = {'item': item_by_num[0],
               'item_by_num': item_by_num,
               'student_num': student_num,
               'eval_item_name': eval_item_name,
               'eval_item_type': eval_item_type,
               'eval_completed': eval_completed,
               'eval_completed_dict': eval_completed_dict,
               'audio_files': audio_files,
               }

    return render(request, 'eval/audio_list.html', context)
def vote(request):
    return render(request, 'eval/vote.html')
