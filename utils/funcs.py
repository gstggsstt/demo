from db.models import *


def in_class(user_id, class_id):
    try:
        cl = Class.objects.get(id=class_id)
        return (Student.objects.get(id__id=user_id) in cl.students.all() or
                Teacher.objects.get(id__id=user_id) in cl.teachers.all() or
                TA.objects.get(id__id=user_id) in cl.tas.all())
    except Exception as e:
        return False


def is_student_of(user_id, class_id):
    try:
        cl = Class.objects.get(id=class_id)
        return Student.objects.get(id__id=user_id) in cl.students.all()
    except Exception as e:
        return False


def is_teacher_of(user_id, class_id):
    try:
        cl = Class.objects.get(id=class_id)
        return Teacher.objects.get(id__id=user_id) in cl.teachers.all()
    except Exception as e:
        return False


def is_ta_of(user_id, class_id):
    try:
        cl = Class.objects.get(id=class_id)
        return TA.objects.get(id__id=user_id) in cl.tas.all()
    except Exception as e:
        return False


def is_leader_of(user_id, group_id):
    try:
        gr = Group.objects.get(id=group_id)
        return gr.leader.id.id == user_id
    except Exception as e:
        return False

def is_teacher(user_id):
    try:
        Teacher.objects.get(id__id=user_id)
        return True
    except Exception as e:
        return False

