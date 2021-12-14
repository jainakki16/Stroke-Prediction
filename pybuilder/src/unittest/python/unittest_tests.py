import sys
sys.path.append('src/main/python')

from script_test import predict_stroke
import unittest

class SimpleTest(unittest.TestCase):
    def testcase1(self):
        case_1 = {}
        case_1['gender'] = 'Male'
        case_1['age'] = 45
        case_1['hypertension'] = '0'
        case_1['heart_disease'] = '1'
        case_1['marital_status'] = 'No'
        case_1['work_type'] = 'Private'
        case_1['residence_type'] = 'Urban'
        case_1['avg_glucose_level'] = 51
        case_1['bmi'] = 6
        case_1['smoking_status'] = 'smokes'

        self.assertEquals(predict_stroke(case_1), "Congratulations! Based on your inputs you are not likely to get a stroke.")

    
    def testcase2(self):
        case_2 = {}
        case_2['gender'] = 'Female'
        case_2['age'] = 34
        case_2['hypertension'] = '0'
        case_2['heart_disease'] = '0'
        case_2['marital_status'] = 'Yes'
        case_2['work_type'] = 'children'
        case_2['residence_type'] = 'Rural'
        case_2['avg_glucose_level'] = 140
        case_2['bmi'] = 23
        case_2['smoking_status'] = 'never smoked'

        self.assertEquals(predict_stroke(case_2), "Congratulations! Based on your inputs you are not likely to get a stroke.")
