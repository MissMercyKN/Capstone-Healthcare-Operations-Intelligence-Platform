from Healthcare_Operations_Intelligence_Platform_FINAL.archive.synthetic_data_generator import generate_all
from feature_engineering_v3 import build_features
from database_builder import build_database

if __name__=='__main__':
    generate_all()
    build_features()
    build_database()
    print('Pipeline completed')
