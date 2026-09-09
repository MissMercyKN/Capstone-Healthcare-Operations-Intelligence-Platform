import pandas as pd
from pathlib import Path

def build_features():
    df=pd.read_csv('data/raw/synthetic/patient_flow.csv')
    out=Path('data/processed')
    out.mkdir(parents=True,exist_ok=True)
    x=df.groupby('department').agg(
        daily_patient_count=('visit_id','count'),
        average_wait_time=('waiting_time','mean')
    ).reset_index()
    x['congestion_flag']=(x['average_wait_time']>65).astype(int)
    x.to_csv(out/'analytics_features.csv',index=False)

if __name__=='__main__':
    build_features()
