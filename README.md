# AD_datasets

## Introduction
Datasets to be used for applicability domains

### Datasets

These datasets originate from two papers.
- [Efficiency of different measures for defining the applicability domain of classification models](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0230-2#MOESM3)
- [A comprehensive comparison of molecular feature representations for use in predictive modeling](https://www.sciencedirect.com/science/article/abs/pii/S001048252030528X)

The directories to_be_converted, Comp_datasets, Additional_files, and Additional_files_CV consist of datasets that originates from one of the two papers.

- to_be_converted consists of the datasets Musk2, QSAR, BBB and PGP dataset. These were found in Additional file 4 of [Efficiency of different measures for defining the applicability domain of classification models](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0230-2#MOESM3)
- Additional_files consists of the preprocessed datasets found in Additional files 5 of [Efficiency of different measures for defining the applicability domain of classification models](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0230-2#MOESM3)
- Additional_files consists of the indices for the fivefold CV of the datasets found in Additional files 5 of [Efficiency of different measures for defining the applicability domain of classification models](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0230-2#MOESM3)
- Comp_datasets consists of the smiles csv files that originates from the [A comprehensive comparison of molecular feature representations for use in predictive modeling](https://www.sciencedirect.com/science/article/abs/pii/S001048252030528X). These include the BBBP, HIV, Mutagenicity, MUV, SIDER and Tox21 datasets.


### Notes

The PGP dataset is found in the [Supporting Information Available](https://pubs.acs.org/doi/10.1021/ci034160g) section of an article. The origin filename was is groot_all.csv.

The Mutagenicity dataset in Comp_datasets and Ames dataset in Additional_files consists of the same data however, the Mutagenicity dataset is missing some chemicals as RDKit was used to preprocess the chemicals. RDKit was not able to preprocess all chemicals resulting in it having 81 chemicals missing.
