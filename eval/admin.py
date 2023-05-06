from django.contrib import admin
from .models import Student, AudioFile, Score, Eval_item
import csv
from django.http import HttpResponse
class EvaldataInline(admin.StackedInline):
    model = AudioFile
    extra = 2
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'name']
    list_display = ('id', 'name')

@admin.register(Eval_item)
class Eval_itemAdmin(admin.ModelAdmin):
    inlines = (EvaldataInline,)
    list_display_links = ['id', 'item_text', 'item_component']
    list_display = ('id', 'my_id', 'item_text', 'item_component')

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_number', 'item', 'item_type', 'audio_file', 'eval_completed')
    list_display_links = ['id', 'student_number', 'item', 'item_type', 'audio_file', 'eval_completed']
    list_filter = ('id', 'student_number', 'item', 'item_type', 'audio_file','eval_completed')
    ordering = ['id', 'student_number', 'item', 'item_type', 'audio_file', 'eval_completed']

    def export_to_excel(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="audio_files.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['id', 'student_number', 'item', 'audio_file'])

        for obj in queryset:
            writer.writerow(
                [obj.id, obj.student_number, obj.item, obj.audio_file])

        return response

    export_to_excel.short_description = 'Export selected to Excel'

    actions = [export_to_excel]

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'user', 'student', 'eval_item', 'rating_ho', 'rating_un', 'rating_fu', 'rating_ac',
                          'rating_ph', 'rating_accent', 'rating_rule', 'rating_pause', 'uploaded_at', 'eval_completed']
    list_display = ('id', 'user', 'student', 'eval_item', 'rating_ho', 'rating_un', 'rating_fu', 'rating_ac',
                    'rating_ph', 'rating_accent', 'rating_rule', 'rating_pause', 'uploaded_at', 'eval_completed')
    ordering = ['id', 'user', 'student', 'eval_item', 'rating_ho', 'rating_un', 'rating_fu', 'rating_ac',
                'rating_ph', 'rating_accent', 'rating_rule', 'rating_pause', 'uploaded_at', 'eval_completed']

    def export_to_excel(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="eval_score.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['id', 'user', 'student', 'eval_item',
             'rating_ho', 'rating_un', 'rating_fu', 'rating_ac',
             'rating_ph', 'rating_accent', 'rating_rule', 'rating_pause', 'uploaded_at'])

        for obj in queryset:
            writer.writerow(
                [obj.id, obj.user, obj.student, obj.eval_item, obj.rating_ho,
                 obj.rating_un, obj.rating_fu, obj.rating_ac,
                 obj.rating_ph, obj.rating_accent, obj.rating_rule, obj.rating_pause,
                 obj.uploaded_at])

        return response

    export_to_excel.short_description = 'Export selected to Excel'

    actions = [export_to_excel]