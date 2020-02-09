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

### Things to do
1.  Feel free to sit in on Intro to Radiomics lecture for the BMS students - Monday 0830h Wynand Wijnenzaal UNS50 K4.403. Lecture PDF here by Tuesday.
2.  We will look at some training materials by Maastro Clinic (for doctors and radiation technologists) on Thursday.
3.  Choose an imaging modality (CT/MRI/PET) as a pair and read up on what information you could learn from the image.
4.  Learn how to navigate and download public-access image repositories like **The Cancer Imaging Archive**  (https://www.cancerimagingarchive.net/) or **TRaIT-xnat** (https://xnat.bmia.nl/).





## Step 2 : Getting and understanding the data
At the end of this second step, you would be able to do all of the following :
1. Know how to look up imaging repositories (see things to do in Step 1) and  obtain  public access clinical images of CT, MR or PET.
2. Be able to open, view and understand how medical imaging files are organized in the DICOM standard

#### Resources you may need
1.  https://www.dicompyler.com/
2.  https://pydicom.github.io/
3.  https://www.cancerimagingarchive.net/
4.  https://xnat.bmia.nl/
5.  Python resources in this project needs a python installation such as Anaconda3 https://www.anaconda.com/
6.  There is a script in this github repository itself that you can modify and use to download collections from xnat.bmia.nl

### Things to do
1.  Install **Dicompyler** (this is one of several free software you can use to view DICOM format medical images).
2.  Alternatively to dicompyler, you could another freeware software package online that can open DICOM images with annotations.
3.  Navigate to TCIA cancer archive and locate the lung radiomics collections. Since there are 6 people in the team, you could decide among yourselves who is going to download which part (we will need all six parts) :
      3.1. NSCLC-Radiomics-Interobserver1
      3.2. RIDER Lung CT
      3.3. NSCLC-Radiomics patients 1-100
      3.4. NSCLC-Radiomics patients 101-200
      3.5. NSCLC-Radiomics patients 201-300
      3.6. NSCLC-Radiomics patients 301-422
4.  Open your own part of the images and have a browse around, try to work out how the dicom files are organized by its contents.
5.  *if you would like to using a more flexible programming script you can do the following :*
      - *Install Anaconda3 Python following the instructions on their webpage (stay with the defaults)*
      - *There is a small python script in this repository for downloading collections from xnat*
      - *You will need a little experience eg installing packages with "pip" for example*
      - *Feel free to modify the script with a text editor to download different collections etc.*





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


