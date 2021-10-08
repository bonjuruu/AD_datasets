import pandas as pd
import csv
import os

# find filepath
to_be_converted = os.path.join(os.getcwd(), 'to_be_converted')
converted = os.path.join(os.getcwd(),"datasets")

#convert the QSAR datasets
df = pd.read_csv(to_be_converted + "\\biodeg.csv", sep=";", header=None, names=["SpMax_L", "J_Dz(e)", "nHM", "F01[N-N]", "F04[C-N]", "NssssC", "nCb-", "C%", "nCp", "nO ", "F03[C-N]", "SdssC ", "HyWi_B(m)", "LOC", "SM6_L", "F03[C-O]", "Me ", "Mi ", "nN-N", "nArNO2", "nCRX3", "SpPosA_B(p)", "nCIR", "B01[C-Br]", "B03[C-Cl]", "N-073", "SpMax_A", "Psi_i_1d", "B04[C-Br]", "SdO ", "TI2_L", "nCrt", "C-026--", "F02[C-N]", "nHDon", "SpMax_B(m", "Psi_i_A", "nN ", "SM6_B(m)", "nArCOOR", "nX ", "RB"])

df.to_csv(converted + "\\QSAR_dataset.csv")


#convert the BBB datasets
dataContent = [i.strip().split() for i in open(to_be_converted + "\\BBBdatabase.txt").readlines()]

names = dataContent[0]

inactive = dataContent[2:147]
active = dataContent[152:332]

with open(converted + "\\BBBinactive.csv", "w", newline="") as dataset:
    csv_writer = csv.writer(dataset)
    csv_writer.writerow(names)
    for line in inactive:
        csv_writer.writerow(line)
        
with open(converted + "\\BBBactive.csv", "w", newline="") as dataset:
    csv_writer = csv.writer(dataset)
    csv_writer.writerow(names)
    for line in active:
        csv_writer.writerow(line)
        
with open(converted + "\\BBB_all.csv", "w", newline="") as dataset:
    csv_writer = csv.writer(dataset)
    csv_writer.writerow(names)
    for line in inactive:
        csv_writer.writerow(line)
    for line in active:
        csv_writer.writerow(line)


#convert the musk2 dataset
dataContent = [i.strip().split() for i in open(to_be_converted + "\\musk2.dat").readlines()]

names = dataContent[169][1:] + dataContent[170][1:]

rows = dataContent[172:]


with open(converted + "\\musk2_dataset.csv", "w", newline="") as dataset:
    csv_writer = csv.writer(dataset)
    csv_writer.writerow(names)
    for line in rows:
        csv_writer.writerow(line)


#convert the musk2CV datasets
musk2_dir = os.path.join(to_be_converted, "musk2")
filenames = os.listdir(musk2_dir)

musk2CV_converted = converted + "\\musk2CV"
os.mkdir(musk2CV_converted)

for filename in filenames:
    filepath = f"{musk2_dir}\\{filename}"
    
    firstname = filename.split(".")[0]
    csvName = f"{musk2CV_converted}\\{firstname}.csv"
    
    dataContent = [i.strip().split() for i in open(filepath).readlines()]
    
    names = dataContent[169][1:] + dataContent[170][1:]

    rows = dataContent[172:]
    
    with open(csvName, "w", newline="") as dataset:
        csv_writer = csv.writer(dataset)
        csv_writer.writerow(names)
        for line in rows:
            csv_writer.writerow(line)