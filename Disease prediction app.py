import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading model
diabetes_model = pickle.load(open("C:/Users/ommoh/PycharmProjects/disease_prediction/saved model/diabetes_model.sav","rb"))
parkinsons_model = pickle.load(open("C:/Users/ommoh/PycharmProjects/disease_prediction/saved model/parkinsons_model.sav","rb"))
heart_disease_model = pickle.load(open("C:/Users/ommoh/PycharmProjects/disease_prediction/saved model/heart_disease_model.sav","rb"))
Breast_Cancer_model =pickle.load(open("C:/Users/ommoh/PycharmProjects/disease_prediction/saved model/Breast_Cancer_model.sav","rb"))

#sidebar for navigation
with st.sidebar:
    selected = option_menu("Disease_Prediction_System Using Ml",
                           ["Diabeties_Prediction",
                            "Heart_Disease_Prediction",
                            "Parkinsons_Prediction",
                            "Breast_Cancer_Prediction"],
                           icons = ["clipboard pulse","bag heart","align-center","bookmark-star"],

                           default_index=0)
#diabetics prediction page
if (selected == "Diabeties_Prediction"):

    #page title
    st.title("Diabeties_Prediction_Using_ML")
    with st.container():
       st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
       st.text("Pregnancies: Number of times pregnant")
       st.text("Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
       st.text("BloodPressure: Diastolic blood pressure (mm Hg)")
       st.text("Ski""nThickness: Triceps skin fold thickness (mm)")
       st.text("Insulin: 2-Hour serum insulin (mu U/ml)")
       st.text("BMI: Body mass index (weight in kg/(height in m)^2)")
       st.text("DiabetesPedigreeFunction: Diabetes pedigree function")
       st.text("Age: Age (years)")
       st.text("Outcome: Class variable (0 or 1)")
       st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #getting input
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.number_input("Number of Pregnancies")
    with col2:
        Glucose=st.number_input("Glucose level")
    with col3:
        BloodPressure=st.number_input("BloodPressure value")
    with col1:
        SkinThickness=st.number_input("SkinThickness value")
    with col2:
        Insulin=st.number_input("Insulin value")
    with col3:
        BMI=st.number_input("BMI value")
    with col1:
        DiabetesPedigreeFunction=st.number_input("DiabetesPedigreeFunction value")
    with col2:
        Age= st.number_input("Age value")

    #code of prediction
    diab_diagnosis = ""
    #create button for prediction
    if st.button("Diabetics Test Result"):
        diab_predict = diabetes_model.predict([[Pregnancies,Glucose, BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diab_predict[0]==1):
            diab_diagnosis = "The Person is a Diabetic Person,Need To control your Suger"
        else:
            diab_diagnosis = "The Person is not Diabetic Person,Thanks for coming"
    st.success(diab_diagnosis)




#Heart_Disease_prediction page
if (selected == "Heart_Disease_Prediction"):
    #page title
    st.title("Heart_Disease_Prediction_Using_Ml")

    with st.container():
        st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        st.text("age")
        st.text("sex")
        st.text("chest pain type (4 values)")
        st.text("resting blood pressure")
        st.text("serum cholestoral in mg/dl")
        st.text("fasting blood sugar > 120 mg/dl")
        st.text("esting electrocardiographic results (values 0,1,2)")
        st.text("maximum heart rate achieved")
        st.text("exercise induced angina")
        st.text("oldpeak = ST depression induced by exercise relative to rest")
        st.text("the slope of the peak exercise ST segment")
        st.text("number of major vessels (0-3) colored by flourosopy")
        st.text("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #column
    col1,col2 = st.columns(2)
    with col1:
        age = st.number_input("Age")
    with col2:
        sex = st.number_input("sex [1 or 0]")
    with col1:
        cp =st.number_input("chest pain type (1 to 4)")
    with col2:
        trestbps =st.number_input("resting blood pressure")
    with col1:
        chol=st.number_input("serum cholestoral in mg/dl")
    with col2:
        fbs	=st.number_input("blood sugar")
    with col1:
        restecg=st.number_input("restecg (0,1,2)")
    with col2:
        thalach=st.number_input("thalach")
    with col1:
        exang=st.number_input("exercise induced angina")
    with col2:
        oldpeak=st.number_input("oldpeak")
    with col1:
        slope=st.number_input("slope of the peak")
    with col2:
        ca=st.number_input("ca (0-3)")
    with col1:
        thal=st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
    # code of prediction
    heart_diagnosis = ""
    # create button for prediction
    if st.button("Heart Test Result"):
        heart_predict = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if(heart_predict[0] == 1):
             heart_diagnosis = "The Person is a Heart_disease pataient,Need to special Care."
        else:
             heart_diagnosis = "The Person is not Heart Disease Person"
    st.success(heart_diagnosis)

#Parkinsons_Prediction page
if (selected == "Parkinsons_Prediction"):
    #page title
    st.title("Parkinsons_Prediction_Using_Ml")
    with st.container():
         st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
         st.text("MDVP:Fo(Hz) - Average vocal fundamental frequency")
         st.text("MDVP:Fhi(Hz) - Maximum vocal fundamental frequency")
         st.text("MDVP:Flo(Hz) - Minimum vocal fundamental frequency")
         st.text("MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP - Several measures of variation in fundamental frequency")
         st.text("MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude")
         st.text("NHR, HNR - Two measures of the ratio of noise to tonal components in the voice")
         st.text("status - The health status of the subject (one) - Parkinson's, (zero) - healthy")
         st.text("PDE, D2 - Two nonlinear dynamical complexity measures")
         st.text("spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation")
         st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #column
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.number_input('MDVP:RAP')

    with col2:
        PPQ = st.number_input('MDVP:PPQ')

    with col3:
        DDP = st.number_input('Jitter:DDP')

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')

    with col3:
        APQ = st.number_input('MDVP:APQ')

    with col4:
        DDA = st.number_input('Shimmer:DDA')

    with col5:
        NHR = st.number_input('NHR')

    with col1:
        HNR = st.number_input('HNR')

    with col2:
        RPDE = st.number_input('RPDE')

    with col3:
        DFA = st.number_input('DFA')

    with col4:
        spread1 = st.number_input('spread1')

    with col5:
        spread2 = st.number_input('spread2')

    with col1:
        D2 = st.number_input('D2')

    with col2:
        PPE = st.number_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

if (selected == "Breast_Cancer_Prediction"):
    #page title
    st.title("Breast_Cancer_Prediction_Using_Ml")
    with st.container():
        st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        st.text("id:Unique ID")
        st.text("diagnosis:Target: M - Malignant B - Benign")
        st.text("texture_mean:Mean of Surface Texture")
        st.text("perimeter_mean:Outer Perimeter of Lobes")
        st.text("area_mean:Mean Area of Lobes")
        st.text("smoothness_mean:Mean of Smoothness Levels")
        st.text("compactness_mean:Mean of Compactness")
        st.text("concavity_mean:Mean of Concavity")
        st.text("concave points_mean:Mean of Cocave Points")
        st.text(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #column
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
         mean_radius	= st.number_input('mean radius')

    with col2:
        mean_texture = st.number_input('mean texture')

    with col3:
        mean_perimeter  = st.number_input('mean perimeter')

    with col4:
        mean_area = st.number_input('mean area')

    with col5:
        mean_smoothness = st.number_input('mean smoothness')

    with col1:
        mean_compactness = st.number_input('mean compactness')

    with col2:
        mean_concavity = st.number_input('mean concavity')

    with col3:
        mean_concave_points = st.number_input('mean concave points')

    with col4:
        mean_symmetry = st.number_input('mean symmetry')

    with col5:
        mean_fractal_dimension = st.number_input('mean fractal dimension')

    with col1:
        radius_error = st.number_input('radius error')

    with col2:
        texture_error = st.number_input('texture error')

    with col3:
        perimeter_error = st.number_input('perimeter error')

    with col4:
        area_error = st.number_input('area error')

    with col5:
        smoothness_error = st.number_input('smoothness error')

    with col1:
        compactness_error = st.number_input('compactness error')

    with col2:
        concavity_error = st.number_input('concavity error')

    with col3:
        concave_points_error = st.number_input('concave points error')

    with col4:
        symmetry_error = st.number_input('symmetry error')

    with col5:
        fractal_dimension_error = st.number_input('fractal dimension error')
    with col1:
        worst_radius = st.number_input('worst radius')
    with col2:
        worst_texture = st.number_input('worst texture')
    with col3:
        worst_perimeter = st.number_input('worst perimeter')
    with col4:
        worst_area = st.number_input('worst area')
    with col5:
        worst_smoothness = st.number_input('worst smoothness')
    with col1:
        worst_compactness = st.number_input('worst compactness')
    with col2:
        worst_concavity = st.number_input("worst concavity")
    with col3:
        worst_concave_points = st.number_input("worst concave point")
    with col4:
        worst_symmetry = st.number_input('worst symmetry')
    with col5:
        worst_fractal_dimension = st.number_input('worst fractal dimension')

    # code for Prediction
    Breast_Cancer_diagnosis = ''

    # creating a button for Prediction
    if st.button("Breast Cancer Test Result"):
        Breast_prediction = Breast_Cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])

        if (Breast_prediction[0] == 0):
            Breast_Cancer_diagnosis = 'The Breast cancer is Malignant'
        else:
            Breast_Cancer_diagnosis = "The Breast Cancer is Benign"

    st.success(Breast_Cancer_diagnosis)

