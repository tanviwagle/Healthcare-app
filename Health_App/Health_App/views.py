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
    model = pickle.load(open("C:\\Users\\Wagle\\Desktop\\MCA\\SEM 6\\Internal Project\\Health_App\\Health_App\\Heart_Disease.sav", "rb"))

    if sex == 0:
        sex_0 = 1
        sex_1 = 0
    else:
        sex_0 = 0
        sex_1 = 1
    
    if chest_pain == 0:
        chest_pain_type_0 = 1
        chest_pain_type_1 = 0
        chest_pain_type_2 = 0
        chest_pain_type_3 = 0
    elif chest_pain == 1:
        chest_pain_type_0 = 0
        chest_pain_type_1 = 1
        chest_pain_type_2 = 0
        chest_pain_type_3 = 0
    elif chest_pain == 2:
        chest_pain_type_0 = 0
        chest_pain_type_1 = 0
        chest_pain_type_2 = 1
        chest_pain_type_3 = 0
    else:
        chest_pain_type_0 = 0
        chest_pain_type_1 = 0
        chest_pain_type_2 = 0
        chest_pain_type_3 = 1
    

    if fast_bp == 0:
        fasting_blood_pressure_0 = 1
        fasting_blood_pressure_1 = 0
    else:
        fasting_blood_pressure_0 = 0
        fasting_blood_pressure_1 = 1
    
    if rest_ecg == 0:
        rest_ecg_0 = 1
        rest_ecg_1 = 0
        rest_ecg_2 = 0
    elif rest_ecg == 1:
        rest_ecg_0 = 0
        rest_ecg_1 = 1
        rest_ecg_2 = 0
    else:
        rest_ecg_0 = 0
        rest_ecg_1 = 0
        rest_ecg_2 = 1
    
    if exercise_induced_angina == 0:
        exercise_induced_angina_0 = 1
        exercise_induced_angina_1 = 0
    else:
        exercise_induced_angina_0 = 0
        exercise_induced_angina_1 = 1
    
    if slope == 0:
        slope_0 = 1
        slope_1 = 0
        slope_2 = 0
    elif slope == 1:
        slope_0 = 0
        slope_1 = 1
        slope_2 = 0
    else:
        slope_0 = 0
        slope_1 = 0
        slope_2 = 1


    if num_major_vessel == 0:
        num_major_vessels_0 = 1
        num_major_vessels_1 = 0
        num_major_vessels_2 = 0
        num_major_vessels_3 = 0
        num_major_vessels_4 = 0
    elif num_major_vessel == 1:
        num_major_vessels_0 = 0
        num_major_vessels_1 = 1
        num_major_vessels_2 = 0
        num_major_vessels_3 = 0
        num_major_vessels_4 = 0
    elif num_major_vessel == 2:
        num_major_vessels_0 = 0
        num_major_vessels_1 = 0
        num_major_vessels_2 = 1
        num_major_vessels_3 = 0
        num_major_vessels_4 = 0
    elif num_major_vessel == 3:
        num_major_vessels_0 = 0
        num_major_vessels_1 = 0
        num_major_vessels_2 = 0
        num_major_vessels_3 = 1
        num_major_vessels_4 = 0
    else:
        num_major_vessels_0 = 0
        num_major_vessels_1 = 0
        num_major_vessels_2 = 0
        num_major_vessels_3 = 0
        num_major_vessels_4 = 1

    if thal == 0:
        thal_0 = 1
        thal_1 = 0
        thal_2 = 0
        thal_3 = 0
    elif thal == 1:
        thal_0 = 0
        thal_1 = 1
        thal_2 = 0
        thal_3 = 0
    elif thal == 2:
        thal_0 = 0
        thal_1 = 0
        thal_2 = 1
        thal_3 = 0
    else:
        thal_0 = 0
        thal_1 = 0
        thal_2 = 0
        thal_3 = 1


    prediction = model.predict([[age, rest_bp, chol, max_hr, st_dep, sex_0, sex_1, chest_pain_type_0, chest_pain_type_1, chest_pain_type_2, chest_pain_type_3, fasting_blood_pressure_0, fasting_blood_pressure_1, rest_ecg_0, rest_ecg_1, rest_ecg_2, exercise_induced_angina_0, exercise_induced_angina_1, slope_0, slope_1, slope_2, num_major_vessels_0, num_major_vessels_1, num_major_vessels_2, num_major_vessels_3, num_major_vessels_4, thal_0, thal_1, thal_2, thal_3]])

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