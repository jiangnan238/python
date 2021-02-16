#匿名调查问卷
class Survey():
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)
    
    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_result(self):
        for response in self.responses:
            print(response,end='\n')
'''
question = "what language did you first learn to speak?"
my_survey = Survey(question)
#显示问题
my_survey.show_question()
#存储答案
while True:
    response = input("input language(enter'q' end the question)：")
    if response == 'q':
        break
    my_survey.store_response(response)
#显示结果
my_survey.show_result()
'''

#测试
import unittest
class TestSurvey(unittest.TestCase):
    def test_store_single_response(self):
        test_question = "what language did you first learn to speak?"
        test_survey = Survey(test_question)
        test_survey.store_response('english')
        #是否存储在列表内
        self.assertIn('english',test_survey.responses)
    
#unittest.main()
class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin with 'test'  
            self.assertEqual((1 + 2), 3)  
            self.assertEqual(0 + 1, 1)  
        def testMultiply(self):  
            self.assertEqual((0 * 10), 0)  
            self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()
# unittest.main()的意思就是：
# 当程序自己运行时，则调用当前程序中名字以“test”开头的函数
# 当程序被调用运行时，则不运行程序中名字以“test”开头的函数