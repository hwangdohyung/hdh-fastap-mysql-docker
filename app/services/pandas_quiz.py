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
        
        
    '''
    Q1. 다음 결과 출력
       a  b  c 
    1  1  3  5
    2  2  4  6
    ic| df1:       a  b  c
                1  1  3  5
                2  2  4  6
    '''
