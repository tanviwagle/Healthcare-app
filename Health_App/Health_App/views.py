from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def heart_pred(request):
    return render(request, 'heart_pred.html')

def liver_pred(request):
    return render(request, 'liver_pred.html')

def stroke_pred(request):
    return render(request, 'stroke_pred.html')


def get_predictions(age, sex, chest_pain, rest_bp, chol, fast_bp, rest_ecg, max_hr, exercise_induced_angina, st_dep, slope, num_major_vessel, thal):
    import pickle
    model = pickle.load(open('Heart_Disease.pkl', 'rb'))
    prediction = model.predict([[age, sex, chest_pain, rest_bp, chol, fast_bp, rest_ecg, max_hr, exercise_induced_angina, st_dep, slope, num_major_vessel, thal]])

    if prediction == 0:
        return "You don't have heart disease"
    elif prediction == 1:
        return "Sorry! You have heart disease. Please consult a doctor."
    else:
        return "error"


def result(request):
    age = int(request.GET['age'])
    sex = int(request.GET['sex'])
    chest_pain = int(request.GET['chest_pain'])
    rest_bp = int(request.GET['rest_bp'])
    chol = int(request.GET['chol'])
    fast_bp= int(request.GET['fast_bp'])
    rest_ecg= int(request.GET['rest_ecg'])
    max_hr= int(request.GET['max_hr'])
    exercise_induced_angina= int(request.GET['ex_in_ang'])
    st_dep= int(request.GET['st_dep'])
    slope=int(request.GET['slope'])
    num_major_vessel=int(request.GET['n_majorVessel'])
    thal=int(request.GET['thal'])

    result = get_predictions(age, sex, chest_pain, rest_bp, chol, fast_bp, rest_ecg, max_hr, exercise_induced_angina, st_dep, slope, num_major_vessel, thal)

    return render(request, 'result.html', {'result': result})