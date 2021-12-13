import sys
sys.path.append('src/main/python')

from script_test import predict_stroke
import unittest

class SimpleTest(unittest.TestCase):
    def testadd1(self):
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

        self.assertEquals(predict_stroke(
            case_1), "Congratulations! Based on your inputs you are not likely to get a stroke.")
