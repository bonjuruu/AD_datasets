import csv
import os



def create_datasets(files_directory, dataset_list, destination):
    for dataset in dataset_list:
        dat_file_path = files_directory + "\\" + dataset
        dat_files = [filename for filename in os.listdir(dat_file_path) if ".dat" in filename]
        for dat in dat_files:
            dataContent = [i.strip().split() for i in open(dat_file_path + "\\" + dat).readlines()]
            
            csv_name = "\\" + dat[:-3] + "csv"

            with open(destination + csv_name, "w", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                for line in dataContent:
                    line = [float(data) for data in line]
                    csv_writer.writerow(line)
                    
if __name__ == "__main__":                    
    preprocessed_datapath = os.path.join(os.getcwd(),'Additional_files')
    prepro_dataset_list = os.listdir(preprocessed_datapath)
    
    cv_datapath = os.path.join(os.getcwd(),'Additional_files_CV')
    cv_dataset_list = os.listdir(cv_datapath)
    
    create_datasets(preprocessed_datapath, prepro_dataset_list, os.getcwd() + "\\datasets\\preprocessed")
    create_datasets(cv_datapath, cv_dataset_list, os.getcwd() + "\\datasets\\preprocessedCV")
