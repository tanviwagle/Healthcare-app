from typing import ContextManager
from django.shortcuts import render
import pandas as pd
import numpy as np

def index(request):
    return render(request, 'index.html')

def heart_dict():
    df_train = pd.read_csv(r'..\Datasets\heart.csv')

    # Gender having disease
    gender_having_Disease = df_train[df_train['target'] == 1].groupby('sex').count()['target']
    gender_having_Disease = pd.DataFrame({'Sex': gender_having_Disease.index, 'Values': gender_having_Disease.values})
    gender_having_Disease['Sex'].loc[0] = 'Female'
    gender_having_Disease['Sex'].loc[1] = 'Male'
    total = gender_having_Disease['Values'].sum()
    gender_having_Disease['Values'] = gender_having_Disease['Values'].div(total).mul(100)
    gender_having_Disease['Values'] = gender_having_Disease['Values'].round(2)
    gender_list = gender_having_Disease['Sex'].values.tolist()
    gender_list_count = gender_having_Disease['Values'].values.tolist()

    # Chest pain type with disease
    cp_type_with_disease = df_train[df_train['target'] == 1].groupby('cp').count()['target']
    cp_type_with_disease = pd.DataFrame({'Type': cp_type_with_disease.index, 'Values': cp_type_with_disease.values})
    cp_type_with_disease['Type'].loc[0] = 'typical angina'
    cp_type_with_disease['Type'].loc[1] = 'atypical angina'
    cp_type_with_disease['Type'].loc[2] = 'non- anginal pain'
    cp_type_with_disease['Type'].loc[3] = 'asymptomatic'
    total = cp_type_with_disease['Values'].sum()
    cp_with_disease_list = cp_type_with_disease['Type'].values.tolist()
    cp_type_with_disease['Values'] = cp_type_with_disease['Values'].div(total).mul(100)
    cp_type_with_disease['Values'] = cp_type_with_disease['Values'].round(2)
    cp_with_disease_count = cp_type_with_disease['Values'].values.tolist()

    # Max heart rate achieved
    df_train["max_rate_group"]=pd.qcut(df_train.thalach, 5, labels = ['70-100', '101-130', '131-160', '161-190', '191-210'])
    max_rate_with_disease = df_train[df_train['target'] == 1].groupby('max_rate_group').count()['target']
    max_rate_without_disease = df_train[df_train['target'] == 0].groupby('max_rate_group').count()['target']
    max_rate_with_disease = pd.DataFrame({'Rate_Group': max_rate_with_disease.index, 'Values': max_rate_with_disease.values})
    max_rate_without_disease = pd.DataFrame({'Rate_Group': max_rate_without_disease.index, 'Values': max_rate_without_disease.values})
    max_rate_with_disease_names = max_rate_with_disease['Rate_Group'].values.tolist()
    max_rate_with_disease_count = max_rate_with_disease['Values'].values.tolist()
    max_rate_without_disease_names = max_rate_without_disease['Rate_Group'].values.tolist()
    max_rate_without_disease_count = max_rate_without_disease['Values'].values.tolist()

    context = {'gender_list': gender_list, 'gender_list_count': gender_list_count, 'cp_with_disease_list': cp_with_disease_list, 'cp_with_disease_count': cp_with_disease_count, 'max_rate_with_disease_names':max_rate_with_disease_names, 'max_rate_with_disease_count': max_rate_with_disease_count, 'max_rate_without_disease_names': max_rate_without_disease_names, 'max_rate_without_disease_count': max_rate_without_disease_count}
    return context


def liver_dict():
    df_train = pd.read_csv(r'..\Datasets\indian_liver_patient.csv')

    # Age
    df_train["agegrp"]=pd.qcut(df_train.Age, 5, labels = ['0-20', '21-40', '41-60', '61-80', '81-95'])
    age_with_disease = df_train[df_train['Dataset'] == 1].groupby('agegrp').count()['Dataset']
    age_without_disease = df_train[df_train['Dataset'] == 2].groupby('agegrp').count()['Dataset']
    age_with_disease = pd.DataFrame({'Age_Group': age_with_disease.index, 'Values': age_with_disease.values})
    age_without_disease = pd.DataFrame({'Age_Group': age_without_disease.index, 'Values': age_without_disease.values})
    age_with_disease_names = age_with_disease['Age_Group'].values.tolist()
    age_with_disease_count = age_with_disease['Values'].values.tolist()
    age_without_disease_names = age_without_disease['Age_Group'].values.tolist()
    age_without_disease_count = age_without_disease['Values'].values.tolist()

    # Gender
    gender_Disease = df_train[df_train['Dataset'] == 1]['Gender'].value_counts()
    gender_with_disease = gender_Disease.values.tolist()
    gender = df_train[df_train['Dataset'] == 2]['Gender'].value_counts()
    gender_without_disease = gender.values.tolist()
    gender_names = ['Male', 'Female']

    context = {'age_with_disease_names': age_with_disease_names, 'age_with_disease_count': age_with_disease_count,'age_without_disease_names': age_without_disease_names, 'age_without_disease_count': age_without_disease_count, 'gender_with_disease': gender_with_disease, 'gender_without_disease': gender_without_disease, 'gender_names': gender_names}
    return context

def stroke_dict():
    df_train = pd.read_csv(r'..\Datasets\healthcare-dataset-stroke-data.csv')
    
    # Gender
    gender_Disease = df_train[df_train['stroke'] == 1]['gender'].value_counts()
    gender_with_disease = gender_Disease.values.tolist()
    gender = df_train[df_train['stroke'] == 0]['gender'].value_counts()
    gender_without_disease = gender.values.tolist()
    gender_names = ['Male', 'Female']

    # Ever Married, work_type
    had_stroke = df_train[df_train['stroke'] == 1][['ever_married','work_type']]
    married = had_stroke[had_stroke['ever_married'] == 'Yes'].groupby('work_type').count()
    married_with_disease = pd.DataFrame({'Work_Type': married.index, 'Values': married['ever_married'].values})
    not_married = had_stroke[had_stroke['ever_married'] == 'No'].groupby('work_type').count()
    not_married_with_disease = pd.DataFrame({'Work_Type': not_married.index, 'Values': not_married['ever_married'].values})
    not_married_work_type_names = not_married_with_disease['Work_Type'].tolist()
    not_married_with_disease_count = not_married_with_disease['Values'].to_list()
    married_work_type_names = married_with_disease['Work_Type'].tolist()
    married_with_disease_count = married_with_disease['Values'].to_list()


    # Residence type + disease/ no disease
    res_had_stroke = df_train[df_train['stroke'] == 1]['Residence_type'] .value_counts().values.tolist()
    stroke_res_names = ['Urban', 'Rural']
    res_never_had_stroke = df_train[df_train['stroke'] == 0]['Residence_type'] .value_counts().values.tolist()


    # smoking status + disease/ no disease
    had_stroke_smStatus = df_train[df_train['stroke'] == 1].groupby('smoking_status').count()['stroke']
    no_stroke_smStatus = df_train[df_train['stroke'] == 0].groupby('smoking_status').count()['stroke']
    smoke_status_names = had_stroke_smStatus.index.tolist()
    smoke_had_stroke = had_stroke_smStatus.values.tolist()
    smoke_no_stroke = no_stroke_smStatus.values.tolist()


    context = {'gender_with_disease':gender_with_disease, 'gender_without_disease': gender_without_disease, 'gender_names': gender_names, 'not_married_work_type_names':not_married_work_type_names, 'not_married_with_disease_count': not_married_with_disease_count, 'married_work_type_names': married_work_type_names, 'married_with_disease_count': married_with_disease_count, 'res_had_stroke': res_had_stroke, 'stroke_res_names': stroke_res_names, 'res_never_had_stroke': res_never_had_stroke, 'smoke_status_names': smoke_status_names, 'smoke_had_stroke': smoke_had_stroke, 'smoke_no_stroke': smoke_no_stroke}
    return context


def heart_pred(request):
    context = heart_dict()
    return render(request, 'heart_pred.html', context)

def liver_pred(request):
    context = liver_dict()
    return render(request, 'liver_pred.html', context)

def stroke_pred(request):
    context = stroke_dict()
    return render(request, 'stroke_pred.html', context)

## Heart Disease
def get_heart_disease_predictions(age, sex, chest_pain, rest_bp, chol, fast_bp, rest_ecg, max_hr, exercise_induced_angina, st_dep, slope, num_major_vessel, thal):
    import pickle
    model, score = pickle.load(open("C:\\Users\\Wagle\\Desktop\\MCA\\SEM 6\\Internal Project\\Health_App\\Health_App\\Heart_Disease.sav", "rb"))

    # Sex
    if sex == 'Male':
        sex_0 = 0
        sex_1 = 1
    else:
        sex_0 = 1
        sex_1 = 0
    
    # Chest Pain Type
    if chest_pain == "Typical Angina":
        chest_pain_type_0 = 1
        chest_pain_type_1 = 0
        chest_pain_type_2 = 0
        chest_pain_type_3 = 0
    elif chest_pain == "Atypical Angina":
        chest_pain_type_0 = 0
        chest_pain_type_1 = 1
        chest_pain_type_2 = 0
        chest_pain_type_3 = 0
    elif chest_pain == "Non-Anginal Pain":
        chest_pain_type_0 = 0
        chest_pain_type_1 = 0
        chest_pain_type_2 = 1
        chest_pain_type_3 = 0
    else:
        chest_pain_type_0 = 0
        chest_pain_type_1 = 0
        chest_pain_type_2 = 0
        chest_pain_type_3 = 1
    
    #Fasting Bloood Pressure
    if fast_bp == 'True':
        fasting_blood_pressure_0 = 0
        fasting_blood_pressure_1 = 1
    else:
        fasting_blood_pressure_0 = 1
        fasting_blood_pressure_1 = 0
    
    # Rest ECG
    if rest_ecg == "Normal":
        rest_ecg_0 = 1
        rest_ecg_1 = 0
        rest_ecg_2 = 0
    elif rest_ecg == "ST-T wave abnormality":
        rest_ecg_0 = 0
        rest_ecg_1 = 1
        rest_ecg_2 = 0
    else:
        rest_ecg_0 = 0
        rest_ecg_1 = 0
        rest_ecg_2 = 1
    
    #Exercise Induced Angina
    if exercise_induced_angina == 'Yes':
        exercise_induced_angina_0 = 0
        exercise_induced_angina_1 = 1
    else:
        exercise_induced_angina_0 = 1
        exercise_induced_angina_1 = 0
    
    # Slope
    if slope == 'Upsloping':
        slope_0 = 1
        slope_1 = 0
        slope_2 = 0
    elif slope == 'Flatsloping':
        slope_0 = 0
        slope_1 = 1
        slope_2 = 0
    else:
        slope_0 = 0
        slope_1 = 0
        slope_2 = 1

    # Number of Major Vessels
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

    # Thalium Stress Result
    if thal == 'Normal':
        thal_0 = 0
        thal_1 = 1
        thal_2 = 0
        thal_3 = 0
    elif thal == 'Fixed defect':
        thal_0 = 0
        thal_1 = 0
        thal_2 = 1
        thal_3 = 0
    elif thal == 'Reversable defect':
        thal_0 = 0
        thal_1 = 0
        thal_2 = 0
        thal_3 = 1
    else:
        thal_0 = 1
        thal_1 = 0
        thal_2 = 0
        thal_3 = 0

    X_test = [[age, rest_bp, chol, max_hr, st_dep, sex_0, sex_1, chest_pain_type_0, chest_pain_type_1, chest_pain_type_2, chest_pain_type_3, fasting_blood_pressure_0, fasting_blood_pressure_1, rest_ecg_0, rest_ecg_1, rest_ecg_2, exercise_induced_angina_0, exercise_induced_angina_1, slope_0, slope_1, slope_2, num_major_vessels_0, num_major_vessels_1, num_major_vessels_2, num_major_vessels_3, num_major_vessels_4, thal_0, thal_1, thal_2, thal_3]]
    prediction = model.predict(X_test)

    if prediction == 0:
        return ("You don't have heart disease", score)
    elif prediction == 1:
        return ("Sorry! You may have heart disease. Please consult a doctor.", score)
    else:
        return "error"


def heart_disease_result(request):
    age = int(request.GET['age'])
    sex = str(request.GET['sex'])
    chest_pain = str(request.GET['chest_pain'])
    rest_bp = int(request.GET['rest_bp'])
    chol = int(request.GET['chol'])
    fast_bp= str(request.GET['fast_bp'])
    rest_ecg= str(request.GET['rest_ecg'])
    max_hr= int(request.GET['max_hr'])
    exercise_induced_angina= str(request.GET['ex_in_ang'])
    st_dep= float(request.GET['st_dep'])
    slope=str(request.GET['slope'])
    num_major_vessel=int(request.GET['n_majorVessel'])
    thal=str(request.GET['thal'])

    result, score = get_heart_disease_predictions(age, sex, chest_pain, rest_bp, chol, fast_bp, rest_ecg, max_hr, exercise_induced_angina, st_dep, slope, num_major_vessel, thal)
    context = heart_dict()
    return render(request, 'heart_pred.html', {'result': result, 'score': score} | context)

## Brain Stroke

def get_brain_stroke_predictions(gender, age, hypertension, heart_dis, married, work_type, res_type, avg_glucose_level, bmi, smoking_status):
    import pickle
    model, score = pickle.load(open("C:\\Users\\Wagle\\Desktop\\MCA\\SEM 6\\Internal Project\\Health_App\\Health_App\\Stroke_Prediction.sav", "rb"))
    score = np.round(score, decimals=2)

    # Gender
    if gender == 'Male':
        gender_Male = 1
        gender_Female = 0
    else:
        gender_Male = 0
        gender_Female = 1
    
    # Hypertension
    if hypertension == 'Yes':
        hypertension = 1
    else:
        hypertension = 0
    
    # Heart Disease
    if heart_dis == 'Yes':
        heart_dis = 1
    else:
        heart_dis = 0

    
    # Marriage Status
    if married == 'Yes':
        ever_married_Yes = 1
        ever_married_No = 0
    else:
        ever_married_Yes = 0
        ever_married_No = 1

    # Work Type
    if work_type == 'Private':
        work_type_Govt_job = 0
        work_type_Never_worked = 0
        work_type_Private = 1
        work_type_Self_employed = 0
        work_type_children = 0
    elif work_type == 'Self-employed':
        work_type_Govt_job = 0
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 1
        work_type_children = 0
    elif work_type == 'Govt_job':
        work_type_Govt_job = 1
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children = 0
    elif work_type == 'children':
        work_type_Govt_job = 0
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children = 1
    else:
        work_type_Govt_job = 0
        work_type_Never_worked = 1
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children = 0

    # Residence Type
    if res_type == 'Urban':
        Residence_type_Urban = 1
        Residence_type_Rural = 0
    else:
        Residence_type_Urban = 0
        Residence_type_Rural = 1

    # Smoking Status
    if smoking_status == 'Formerly Smoked':
        smoking_status_Unknown = 0
        smoking_status_formerly_smoked = 1
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0
    elif smoking_status == 'Never Smoked':
        smoking_status_Unknown = 0
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 1
        smoking_status_smokes = 0
    elif smoking_status == 'Smokes':
        smoking_status_Unknown = 0
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 1
    else:
        smoking_status_Unknown = 1
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0

    X_test = [[age, hypertension, heart_dis, avg_glucose_level, bmi, gender_Female, gender_Male, ever_married_No, ever_married_Yes, work_type_Govt_job, work_type_Never_worked, work_type_Private, work_type_Self_employed, work_type_children, Residence_type_Rural, Residence_type_Urban, smoking_status_Unknown, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]]
    prediction = model.predict(X_test)

    if prediction == 0:
        return ("You don't have chances of getting brain stroke", score)
    elif prediction == 1:
        return ("Sorry! You may have chances of getting brain stroke. Please consult a doctor.", score)
    else:
        return "error"

def brain_stroke_result(request):
    gender = str(request.GET['gender'])
    age = int(request.GET['age'])
    hypertension = str(request.GET['hypertension'])
    heart_dis = str(request.GET['heart_dis'])
    married = str(request.GET['married'])
    work_type = str(request.GET['work_type'])
    res_type = str(request.GET['res_type'])
    avg_glucose_level = float(request.GET['glucose_level'])
    bmi = float(request.GET['age'])
    smoking_status = str(request.GET['smoke_st'])

    result, score = get_brain_stroke_predictions(gender, age, hypertension, heart_dis, married, work_type, res_type, avg_glucose_level, bmi, smoking_status)
    context = stroke_dict()
    return render(request, 'stroke_pred.html', {'result': result,'score': score}| context)


## Liver Disease
def get_liver_disease_predictions(age, gender, total_bil, direct_bil, alkaline_phos, alamine_amino, aspartate_amino, total_pro, albumin, albumin_ratio):
    
    import pickle
    model, score = pickle.load(open("C:\\Users\\Wagle\\Desktop\\MCA\\SEM 6\\Internal Project\\Health_App\\Health_App\\Liver_Disease.sav", "rb"))

    ## Gender
    if gender == 'Male':
        Gender_Male = 1
        Gender_Female = 0
    else:
        Gender_Male = 0
        Gender_Female = 1

    X_test = [[age, total_bil, direct_bil, alkaline_phos, alamine_amino, aspartate_amino, total_pro, albumin, albumin_ratio, Gender_Female, Gender_Male]]
    prediction = model.predict(X_test)

    if prediction == 2:
        return ("You don't have liver disease", score)
    elif prediction == 1:
        return ("Sorry! You may have liver disease. Please consult a doctor.", score)
    else:
        return "error"

def liver_disease_result(request):
    age = int(request.GET['age'])
    gender = str(request.GET['gender'])
    total_bil = float(request.GET['total_bil'])
    direct_bil = float(request.GET['direct_bil'])
    alkaline_phos = int(request.GET['alkaline_phos'])
    alamine_amino = int(request.GET['alamine_amino'])
    aspartate_amino = int(request.GET['aspartate_amino'])
    total_pro = float(request.GET['total_pro'])
    albumin = float(request.GET['albumin'])
    albumin_ratio = float(request.GET['albumin_ratio'])

    result, score = get_liver_disease_predictions(age, gender, total_bil, direct_bil, alkaline_phos, alamine_amino, aspartate_amino, total_pro, albumin, albumin_ratio)
    context = liver_dict()
    return render(request, 'liver_pred.html', {'result': result, 'score': score} |context)


def heart_remedies(request):
    return render(request, 'heart_rems.html')

def liver_remedies(request):
    return render(request, 'liver_rems.html')

def brain_remedies(request):
    return render(request, 'brain_rems.html')