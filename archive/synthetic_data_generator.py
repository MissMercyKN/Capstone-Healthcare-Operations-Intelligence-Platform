from pathlib import Path
import pandas as pd
import numpy as np

def generate_all():
    out=Path('data/raw/synthetic')
    out.mkdir(parents=True,exist_ok=True)
    n=5000
    rng=np.random.default_rng(42)
    df=pd.DataFrame({
        'visit_id':range(n),
        'department':rng.choice(['Emergency','ICU','Radiology','Surgery'],n),
        'waiting_time':rng.integers(5,120,n),
        'treatment_time':rng.integers(10,180,n)
    })
    df.to_csv(out/'patient_flow.csv',index=False)

if __name__=='__main__':
    generate_all()
