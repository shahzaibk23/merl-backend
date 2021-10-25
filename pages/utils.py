from project.models import category as projectCategory
from trainings.models import category as trainingCategory

def nav_data():
    p_objs = projectCategory.objects.all()
    t_objs = trainingCategory.objects.all()
    projs = [proj.project_set.all() for proj in p_objs]
    trains = [train.training_set.all() for train in t_objs]
    p_lst, t_lst = [],[]
    for i in range(len(p_objs)):
        p_lst.append((p_objs[i], projs[i]))
    for i in range(len(t_objs)):
        t_lst.append((t_objs[i], trains[i]))
    return (p_lst[::-1], t_lst[::-1])