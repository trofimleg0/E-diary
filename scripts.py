from random import choice
from datacenter.models import (
    Schoolkid,
    Teacher,
    Subject,
    Lesson,
    Mark,
    Chastisement,
    Commendation,
)


def fix_marks(student_fullname):
    Mark.objects.filter(
        schoolkid__full_name__contains=student_fullname, points__in=[2, 3]
    ).update(points=5)


def remove_chastisements(student_fullname):
    chastisements = Chastisement.objects.filter(
        schoolkid__full_name__contains=student_fullname
    )
    chastisements.delete()


def create_commendation(student_fullname, lesson):
    try:
        commendations = [
            "Молодец!",
            "Отлично!",
            "Хорошо!",
            "Гораздо лучше, чем я ожидал",
            "Ты меня приятно удивил!",
            "Великолепно!",
            "Прекрасно!",
            "Ты меня очень обрадовал!",
            "Именно этого я давно ждал от тебя!",
            "Сказано здорово – просто и ясно!",
            "Ты, как всегда, точен!",
            "Очень хороший ответ!",
            "Талантливо!",
            "Ты сегодня прыгнул выше головы!",
            "Я поражен!",
        ]

        student_fullname = Schoolkid.objects.get(full_name=student_fullname)
        selected_lesson = Lesson.objects.filter(
            year_of_study=student_fullname.year_of_study,
            group_letter=student_fullname.group_letter,
            subject__title=lesson,
        ).first()
        Commendation.objects.create(
            created=selected_lesson.date,
            teacher=selected_lesson.teacher,
            subject=selected_lesson.subject,
            schoolkid=student_fullname,
            text=choice(commendations),
        )
    except:
        print("Try again")
