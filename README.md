# BBS3004_Radiomics_Project
This is an open teaching resource for a short project in University Maastricht Bach Biomedical Science

## Step 1 : Introduction to Radiomics
At the end of this first step, you would be able to do all of the following :
1. Describe quantitatively what is the information that is contained within one of the following three-dimensional clinical imaging modalities - Computed Tomography (CT), Magnetic Resonance (MR), Positron Emission Tomography PET).
2. Describe a few of the tasks that a radiation oncologist or radiologist would need to do to prepare an image for quantitative analysis.
3. Explain to another colleague in the BBS course, what is radiomics and what are the principle steps to be done in a radiomics analysis.
4. Access a public open source of images for radiomics analysis.
#### Recommended reading
1.  Radiomics: Images Are More than Pictures, They Are Data https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4734157/
2.  Radiomics and radiogenomics in lung cancer: A review for the clinician https://www.ncbi.nlm.nih.gov/pubmed/29290259
3.  Decoding tumour phenotype by noninvasive imaging using a quantitative radiomics approach https://www.nature.com/articles/ncomms5006
4.  Repeatability and Reproducibility of Radiomic Features https://www.ncbi.nlm.nih.gov/pubmed/30170872

## Step 2 : Getting and understanding the data
At the end of this second step, you would be able to do all of the following :
1. Know how to look up well-know imaging repositories and then obtain some public clinical images of CT, MR or PET
2. Be able to open, view and understand how medical imaging files are organized in the DICOM standard

### Some resources you may need
1.  https://www.dicompyler.com/
2.  https://pydicom.github.io/
3.  https://www.cancerimagingarchive.net/
4.  https://xnat.bmia.nl/
5.  Python resources in this project needs a python installation such as Anaconda3 https://www.anaconda.com/
6.  There is a script in this github repository itself that you can modify and use to download collections from xnat.bmia.nl

#### General instructions
1. Install Anaconda following the instructions on their webpage.
2. Install Dicompyler
3. Discuss with your project team which image collection you would download
4. Download the appropriate collection
5. View some of these with an appropriate DICOM viewer to get an idea of how DICOM images are organized

## Step 3 : Radiomics features
At the end of this third step, you would be able to do all of the following :
1. Know how to extract radiomic features from medical images using an open source software package
2. Be able to discuss what kind of computational setting may have an effect on the radiomics features that are computed
#### Recommended reading
1.
2.
3.
4.

## Step 4 : Feature selection
At the end of this fourth step, you would be able to do all of the following :
1. Explain why it is almost always advisable to reduce the number of radiomics features available for a given prediction problem
2. Describe at least 2 methods by which feature dimensionality could be significantly reduced
3. Propose and execute one of these methods on the dataset(s) that you have downloaded
#### Recommended reading
1.
2.
3.
4.

## Step 5 : Fitting a prediction model
At the end of this fifth step, you would be able to do all of the following :
1. Explain why is it strongly recommended to separate available data in a study into training, test and validation sets
2. Justify what woud be a suitable choice of predictive performance for the model you have chosen
3. Be able to develop a simple prediction model and know how to solve for the coefficients of your selected model
#### Recommended reading
1.
2.
3.
4.

## Step 6 : Validating an existing prediction model
At the end of this sixth and final step, you would be able to do all of the following :
1. Know how to design a validation of a prediction model that you or a colleague (or as a group) have developed
2. Discuss some reason why a validation of a prediction model might be good or bad or indifferent
#### Recommended reading
1.
2.
3.
4.


