from random import random
from icecream import ic
import pandas as pd 
class PandasQuiz(object):
    def __init__(self) -> None:
        pass
    
    def quiz_01(self) -> None : 
        df = pd.DataFrame.from_dict(
        {'1' :[1, 3, 5],'2' :[2, 4, 6]},
        orient='index',
        columns=['a','b','c'])
        ic(df)
    
    def quiz_02(self) -> None :
        df = pd.DataFrame.from_dict(
        {'1':[1,2,3],'2':[4,5,6],'3':[7,8,9],'4':[10,11,12],},
        orient='index',
        columns=['A','B','C']) 
        ic(df)
        
    def quiz_03(self) -> None : 
        df = pd.DataFrame.from_dict(
        {'0':[95, 25, 74],'1':[44, 24, 97]},
        orient = 'index',
        columns=['0','1','2'])
        dff = pd.DataFrame.sample(n=(2,3))
        ic(dff)
            
        
        
        
        
        
        #  '''Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        # ic| df3:     0   1   2
        #          0  95  25  74
        #          1  44  24  97
        #          '''
        
        
        
        
        
        
    '''
    Q1. 다음 결과 출력
       a  b  c 
    1  1  3  5
    2  2  4  6
    ic| df1:       a  b  c
                1  1  3  5
                2  2  4  6
    '''

'''         
        Q2. 다음 결과 출력
           A   B   C
        1   1   2   3
        2   4   5   6
        3   7   8   9
        4  10  11  12
        ic| df2:     A   B   C
                 1   1   2   3
                 2   4   5   6
                 3   7   8   9
                 4  10  11  12
        '''
        
        
