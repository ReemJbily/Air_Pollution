import pickle

def load_model():  
    #thfollowing model was downloaded form mlflow after running the experments and compairing different models 
    filename='D://MLOPS//Air pollution//model.pkl'
    model=pickle.load(open(filename, 'rb'))     
    return model
