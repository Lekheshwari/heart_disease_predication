import config
import numpy as np
import json, pickle

class HeartDisease():
    def __init__(self,user_data):
        self.user_data = user_data
        self.model_path = config.MODEL_PATH
        self.project_data_path = config.PROJECT_DATA_PATH 
        
    def load_data(self):
        with open(self.model_path,'rb') as f:
            self.model = pickle.load(f)
            
        with open(self.project_data_path,'r') as f:
            self.project_data = json.load(f)
            
    def predication_heart(self):
        self.load_data()
        
        BMI = float(self.user_data['BMI'])
        Smoking =self.user_data['Smoking']
        AlcoholDrinking =self.user_data['AlcoholDrinking']
        Stroke = self.user_data['Stroke']
        PhysicalHealth =float(self.user_data['PhysicalHealth'])
        MentalHealth = float(self.user_data['MentalHealth'])
        DiffWalking = self.user_data['DiffWalking']
        Sex =self.user_data['Sex']
        AgeCategory =int(self.user_data['AgeCategory'])
        Race = self.user_data['Race']
        Diabetic =self.user_data['Diabetic']
        PhysicalActivity =self.user_data['PhysicalActivity']
        GenHealth  =self.user_data['GenHealth']
        SleepTime =int(self.user_data['SleepTime'])
        Asthma =self.user_data['Asthma']
        KidneyDisease =self.user_data['KidneyDisease']
        SkinCancer = self.user_data['SkinCancer']


        features = np.zeros( len(self.project_data['data']))
        x1 = "Race_"+Race
        index1 = self.project_data['data'].index(x1)
        x2 = "Diabetic_"+ Diabetic
        index2 = self.project_data['data'].index(x2)


        features[0]=BMI
        features[1]=self.project_data['Smoking'][Smoking]  
        features[2]=self.project_data['AlcoholDrinking'][AlcoholDrinking] 
        features[3]=self.project_data['Stroke'][Stroke] 
        features[4]=PhysicalHealth 
        features[5]= MentalHealth
        features[6]= self.project_data['DiffWalking'][DiffWalking] 
        features[7]= self.project_data['Sex'][Sex]
        features[8]= AgeCategory 
        features[9]= self.project_data['PhysicalActivity'][PhysicalActivity] 
        features[10]= self.project_data['GenHealth'][GenHealth] 
        features[11]= SleepTime 
        features[12]= self.project_data['Asthma'][Asthma]
        features[13]= self.project_data['KidneyDisease'][KidneyDisease]
        features[14]= self.project_data['SkinCancer'][SkinCancer]
        features[index1]= 1 
        features[index2]= 1
        # print([features])

        pred=np.around(self.model.predict([features])[0],3)
        if pred == 1:
            return "Chance of Heart dieases"
        else:
            return "Safe"

if __name__ =='__main__':
    obj=HeartDisease()
    obj