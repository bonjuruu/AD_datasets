import csv
import os
import pandas as pd

def create_datasets(files_directory, dataset_list, destination):
    for dataset in dataset_list:
        #find filepath
        directory = os.path.join(files_directory, dataset)
        file = os.path.join(directory, "dataset_smiles.csv")
        
        #get dataframe and make smiles the first column
        csv = pd.read_csv(file)
        columns = list(csv.columns)
        first_col = csv.pop('smiles')
        csv.insert(0, 'smiles', first_col)
        
        #remove id of chemical
        if 'id' in columns:
            csv = csv.drop('id', 1)
        if 'my_id' in columns:
            csv = csv.drop('my_id', 1)
        if 'ID' in columns:
            csv = csv.drop('ID', 1)
        
        #make csv file
        file_name = os.path.join(destination, "{}_smiles.csv".format(dataset))
        csv.to_csv(file_name, index=False)
    
                    
if __name__ == "__main__":                    
    datapath = os.path.join(os.getcwd(),'Comp_datasets')
    smiles_directory = os.listdir(datapath)
    dataset = os.path.join(os.getcwd(), 'datasets')
    
    create_datasets(datapath, smiles_directory, os.path.join(dataset, "finished"))
