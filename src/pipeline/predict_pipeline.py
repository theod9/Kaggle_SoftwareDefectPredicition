import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(str(e),e)



import pandas as pd

class CustomData:
    def __init__(
        self,
        loc: float,
        vg: float,
        evg: float,
        ivg: float,
        n: float,
        v: float,
        l: float,
        d: float,
        i: float,
        e: float,
        b: float,
        t: float,
        lOCode: float,
        lOComment: float,
        lOBlank: float,
        locCodeAndComment: float,
        uniq_Op: float,
        uniq_Opnd: float,
        total_Op: float,
        total_Opnd: float,
        branchCount: float
    ):
        self.loc = loc
        self.vg = vg
        self.evg = evg
        self.ivg = ivg
        self.n = n
        self.v = v
        self.l = l
        self.d = d
        self.i = i
        self.e = e
        self.b = b
        self.t = t
        self.lOCode = lOCode
        self.lOComment = lOComment
        self.lOBlank = lOBlank
        self.locCodeAndComment = locCodeAndComment
        self.uniq_Op = uniq_Op
        self.uniq_Opnd = uniq_Opnd
        self.total_Op = total_Op
        self.total_Opnd = total_Opnd
        self.branchCount = branchCount

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "loc": [self.loc],
                "v(g)": [self.vg],
                "ev(g)": [self.evg],
                "iv(g)": [self.ivg],
                "n": [self.n],
                "v": [self.v],
                "l": [self.l],
                "d": [self.d],
                "i": [self.i],
                "e": [self.e],
                "b": [self.b],
                "t": [self.t],
                "lOCode": [self.lOCode],
                "lOComment": [self.lOComment],
                "lOBlank": [self.lOBlank],
                "locCodeAndComment": [self.locCodeAndComment],
                "uniq_Op": [self.uniq_Op],
                "uniq_Opnd": [self.uniq_Opnd],
                "total_Op": [self.total_Op],
                "total_Opnd": [self.total_Opnd],
                "branchCount": [self.branchCount],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise Exception(f"Error creating DataFrame: {str(e)}")
