import random
from tkinter.tix import COLUMN
from icecream import ic
import pandas as pd 
import string
from pyparsing import col
import numpy as np 

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
        random_1 = [random.randint(10, 99) for p in range(0, 3)]
        random_2 = [random.randint(10, 99) for p in range(0, 3)]
        df = pd.DataFrame.from_dict(
            {'1' : random_1,'2' : random_2},
            orient='index',
            columns=['0', '1', '2'])
        ic(df)
    
    def id(self):
        return ["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
    
    def score(self):
        return np.random.randint(0, 100, (10, 4))
        
    def quiz_04(self):
        df = pd.DataFrame(self.score(),index= self.id(),columns=['국어','영어','수학','사회'])
        ic(df)
        return df
    
     # 리스트로 DataFrame 생성하는 방법 (디폴트)
    # df = pd.DataFrame([[],[],[],[]], index=[], columns=[])
    
    # 사전으로 DataFrame 생성하는 방법 (from_dict()사용) 
    # df = pd.DataFrame.from_dict({}, orient='index', columns=[])



    # Q5 원하는 과목 점수만 출력하시오. (만약 국어라고 입력하면 아래와 같이 출력됨)
    #     hVoGW    93
    #     QkpKK    25
    #     oDmky    82
    #     qdTeX    51
    #     XGzWk    34
    #     PAwgj    85
    #     vnTmB    28
    #     wuxIm    58
    #     AOQFG    32
    #     jHChe    59
    #     Name: 국어, dtype: int64
    
    def quiz_05(self, subject):
        scores = self.quiz_04()
        df5 = scores.loc[:,subject]
        ic(df5)
        
    def quiz_06(self):
        print(f'{id}의 성적출력')
        scores = self.quiz_04()
        df6 = scores.iloc[[0],:]
        ic(df6)
           
#     Q7 각 학생들의 점수의 총합과 마지막 행은 과목총점 추가해서 출력
#         ic| df5:  국어   영어   수학   사회   과학    총점
#                  hVoGW   93   44   14   94   86   331
#                  QkpKK   25   54   29   10    8   126
#                  oDmky   82   65   31   31    2   211
#                  qdTeX   51   56   56    3   13   179
#                  XGzWk   34   32   67   48   23   204
#                  PAwgj   85   24   16    8   22   155
#                  vnTmB   28   80   52   43   48   251
#                  wuxIm   58   94   93   54   83   382
#                  AOQFG   32   50   95    1   52   230
#                  jHChe   59   37   80   27   39   242
#                  과목총점   547  536  533  319  376  2311

    def quiz_07(self):
        self.science = np.random.randint(0,101,(10,1))
        df7 = self.quiz_04()
        df7['과학'] = self.science
        df7['총점'] = df7['국어'] + df7['영어'] + df7['수학'] + df7['사회'] + df7['과학']
        df7.loc['과목총점']= df7.sum(axis=0)
        ic(df7)
       
       
    