from django.contrib import admin
# Import Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline for Lesson
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Inline for Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# Inline for Question
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Course admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Question admin (to manage choices inside question)
class QuestionAdmin(admin.ModelAdmin):
    inline =[ChoiceInline]
    list_display = ['question_text', 'course', 'grade']

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register all models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
