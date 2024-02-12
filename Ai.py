from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

class StudentExamPerformance:
    def __init__(self) :
        dataframe = pd.read_csv("student_exam_data.csv")
        x = np.array(dataframe.drop(columns=["Pass/Fail"]))
        y = np.array(dataframe["Pass/Fail"])

        self.classification = DecisionTreeClassifier()

        self.classification.fit(x, y)
        
    def predict(self, study_hour, previous_exam_score):
        result = self.classification.predict([[study_hour, previous_exam_score]])[0]
        if result == 0:
            return "Fail"
        else:
            return "Pass"