import csv
import os
import pandas as pd



def create_datasets(files_directory, dataset_list, destination):
    for dataset in dataset_list:
        #get each dat filename for a dataset
        dat_file_path = os.path.join(files_directory, dataset)
        dat_files = [filename for filename in os.listdir(dat_file_path) if ".dat" in filename]
        
        #turn dat files into csv form
        for dat in dat_files:
            dataContent = [i.strip().split() for i in open(os.path.join(dat_file_path, dat)).readlines()]
            
            csv_name = os.path.join(destination, dat[:-3] + "csv")

            with open(csv_name, "w", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                for line in dataContent:
                    line = [float(data) for data in line]
                    csv_writer.writerow(line)
                    
def merge_datasets(files_directory, destination):
    x_files = []
    y_files = []
    
    #find csv files that have MACCS values
    for filename in os.listdir(files_directory):
        if "MACCS_raw_X.csv" in filename:
            x_files.append(filename)
            y_files.append(filename.split("_")[0] + "_Y.csv")

    #join the x and y values together
    if len(x_files) == len(y_files):
        for i in range(len(x_files)):
            name = ["x{}".format(num + 1) for num in range(166)]
            
            x = pd.read_csv(os.path.join(files_directory, x_files[i]), sep=",", header=None, names=name)
            y = pd.read_csv(os.path.join(files_directory, y_files[i]), sep=",", header=None, names=["y"])
            
            merged = pd.concat([x, y], axis=1)
            name =  "{}_MACCS.csv".format(x_files[i].split("_")[0])
            merged.to_csv(os.path.join(destination, name), index=False)
    else:
        print("ERROR")
    
                    
if __name__ == "__main__":
    #datapath for preprocessed additional files                    
    preprocessed_datapath = os.path.join(os.getcwd(),'Additional_files')
    prepro_dataset_list = os.listdir(preprocessed_datapath)
    dataset = os.path.join(os.getcwd(), 'datasets')
    #datapath for 5 CV additional files
    cv_datapath = os.path.join(os.getcwd(),'Additional_files_CV')
    cv_dataset_list = os.listdir(cv_datapath)
    
    create_datasets(preprocessed_datapath, prepro_dataset_list, os.path.join(dataset, "preprocessed"))
    create_datasets(cv_datapath, cv_dataset_list, os.path.join(dataset,"preprocessedCV"))
    merge_datasets(os.path.join(dataset, "preprocessed"), os.path.join(dataset, "finished"))
