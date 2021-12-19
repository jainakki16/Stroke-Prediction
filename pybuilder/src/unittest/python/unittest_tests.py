import sys
sys.path.append('src/main/python')

from script_test import predict_stroke
import unittest

class SimpleTest(unittest.TestCase):
    def testcase1(self):
        case_1 = {}
        case_1['gender'] = 'Male'
        case_1['age'] = 25
        case_1['hypertension'] = '1'
        case_1['heart_disease'] = '1'
        case_1['marital_status'] = 'No'
        case_1['work_type'] = 'Never_worked'
        case_1['residence_type'] = 'Rural'
        case_1['avg_glucose_level'] = 175
        case_1['bmi'] = 18
        case_1['smoking_status'] = 'never smoked'

        self.assertEquals(predict_stroke(case_1), "Congratulations! Based on your inputs you are not likely to get a stroke.")

    
    def testcase2(self):
        case_2 = {}
        case_2['gender'] = 'Female'
        case_2['age'] = 30
        case_2['hypertension'] = '1'
        case_2['heart_disease'] = '1'
        case_2['marital_status'] = 'No'
        case_2['work_type'] = 'Never_worked'
        case_2['residence_type'] = 'Rural'
        case_2['avg_glucose_level'] = 120
        case_2['bmi'] = 25
        case_2['smoking_status'] = 'never smoked'

        self.assertEquals(predict_stroke(case_2), "Congratulations! Based on your inputs you are not likely to get a stroke.")


    def testcase3(self):
        case_3 = {}
        case_3['gender'] = 'Female'
        case_3['age'] = 40
        case_3['hypertension'] = '1'
        case_3['heart_disease'] = '0'
        case_3['marital_status'] = 'Yes'
        case_3['work_type'] = 'children'
        case_3['residence_type'] = 'Rural'
        case_3['avg_glucose_level'] = 190
        case_3['bmi'] = 10
        case_3['smoking_status'] = 'formerly smoked'

        self.assertEquals(predict_stroke(case_3), "Please consult a doctor. Based on your inputs you are likely to get stroke.")
