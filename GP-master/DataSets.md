https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia    

https://wiki.cancerimagingarchive.net/display/Public/SPIE-AAPM+Lung+CT+Challenge



    This data set consists of 22,489 images of 70 patients and of type .DCM ''. Each patient's images are repeated so , we can use one image or two for every 
    patient.
     
     The Dataset have two excel sheet files 
     
     1 - CalibrationSet_NoduleData : which has 4 columns 
     
	      1 – Scan Number : The Number given for the patient scan 'ID'
	      
 	      2 – Nodule Center : The x , y position of the nodule.
	      
	      3 – Nodule Center Image : The specific image that the nodule appears in.
	      
	      4 – Diagnosis : Which says if the tumor is malignant or benign.
	      
     2 - TestSet_NoduleData_PublicRelease_wTruth : 
     
	      1 – Scan Number : The Number given for the patient scan 'ID'
	      
	      2 – Nodule Number : The number of nodules for analysis in the scan (either 1 or 2).
	      
              3 – Nodule Center : The x , y position of the nodule.
	
	      4 – Nodule Center Image : The specific image that the nodule appears in.
	      
	      5 – Final Diagnosis : Which says if the tumor 'benign' or 'primary lung cancer'.
	      


https://wiki.cancerimagingarchive.net/display/Public/LungCT-Diagnosis

	This is a small data set of 61 diagnostic contrast enhanced CT scans with known tumors. 4,682 Images for 61 patients.

	This data set hosts collections of de-identified medical images, primarily in DICOM format. Collections are organized according to disease (such as lung cancer), image 	modality (such as MRI or CT), or research focus.

	This dataset has two excel files : 

	1 - LungCT-Diagnosis_MetaData : 

		Which has some metdata about this dataset like ' Collection,Patient Id,Study Date,Study Description '.
		
	2 - Representative-Tumor-Slices :
		Which has 4 columns :
			1 - TCIA Patient ID : The ID of the patient for the TCIA.
			
			2 - TCIA SOP Instance UID : SOP instance UIDs (individual DICOM image IDs) for an image series
			
			3 - Instance Number : The number of picture which  the tumor was clear the most.      
			
			4 - Image Position Patient (X\\Y\\Z) : The position of the center of the tumor.
			
	Note : This dataset doesn't inform us with any data except the tumor place it didn't tell us whether this tumor was benign of malignant.


https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70224216
##### A Large-Scale CT and PET/CT Dataset for Lung Cancer Diagnosis (Lung-PET-CT-Dx).
1. This dataset consists of **CT** and **PET-CT** DICOM images of lung cancer subjects with XML Annotation files that indicate tumor location with **bounding boxes**.

2. It contains 260,826 images, with number of Participants 363.

3. Subjects were grouped according to a tissue histopathological diagnosis. Patients with Names/IDs containing the letter:
   * A' were diagnosed with Adenocarcinoma.
   * B' with Small Cell Carcinoma.
   * C' with Large Cell Carcinoma.
   * G' with Squamous Cell Carcinoma.
4. The images were analyzed on the mediastinum (window width, 350 HU; level, 40 HU) and lung (window width, 1,400 HU; level, –700 HU) settings.

5. The reconstructions were made in 2mm-slice-thick and lung settings. The CT slice interval varies from 0.625 mm to 5 mm. Scanning mode includes plain, contrast and 3D   reconstruction. 

6. The CT resolution was **512 × 512** pixels at 1mm × 1mm, the PET resolution was **200 × 200** pixels at 4.07mm × 4.07mm, with a slice thickness and an interslice distance of 1mm. 

7. The PET images were reconstructed via the **TrueX TOF** method with a slice thickness of 1mm.

8. The location of each tumor was annotated by **five** academic thoracic radiologists with expertise in lung cancer to make this dataset a useful tool and resource for developing algorithms for medical diagnosis, After one of the radiologists labeled each subject the other four radiologists performed a verification, resulting in all five radiologists reviewing each annotation file in the dataset. 

9. Annotations were captured using **Labellmg**. ``` labellmg exist in definations file ```

10. Two deep learning researchers used the images and the corresponding annotation files to train several well-known detection models which resulted in a maximum a posteriori probability (MAP) of around 0.87 on the validation set.

https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI


https://www.kaggle.com/ymirsky/medical-deepfakes-lung-cancer

https://data.mendeley.com/datasets/p2r42nm2ty/3#folder-4e652ff8-4fe0-4786-9c50-448f7efb9bf1

Description of this data
Images were collected from the hospital situated in Iran. Part of these CT-scan images of lungs was belonged to lung cancer patients and classified as cancerous images. The rest belonged to other lung diseases, for instance, patients who caught COVID-19, and classified as non-cancerous images.
The total number of CT-scan images used in this paper is equal to 364 that 238 of them belong to cancerous images, and 126 of the rest belong to non-cancerous images. All of these images were collected by the help of a pulmonologist to skip any probable error in classifying images.

https://data.mendeley.com/datasets/gv5j2gk467/11#folder-bc5fe565-0abc-4f9f-a0a2-6251f9c8976c

Description of this data
Here are all the raw data about the study of "Decoding and Systematization of Medical Imaging Features of Multiple Human Malignancies". Including the proposed correlation atlas to clarify the relationship between medical imaging features and human malignancies, and the CT image dataset of 1000 lung cancer patients for discovering the pattern of distribution of values of the texture features and explaining the visual difference of different image feature values, and all of the source code of this study.


https://plos.figshare.com/articles/_sup_68_sup_Ga-DOTATATE_PET_CT_imaging_of_indeterminate_pulmonary_nodules_and_lung_cancer/4637812


Purpose 18F-FDG PET/CT is widely used to evaluate indeterminate pulmonary nodules (IPNs). False positive results occur, especially from active granulomatous nodules. A PET-based imaging agent with superior specificity to 18F-FDG for IPNs, is badly needed, especially in areas of endemic granulomatous nodules. Somatostatin receptors (SSTR) are expressed in many malignant cells including small cell and non-small cell lung cancers (NSCLCs). 68Ga-DOTATATE, a positron emitter labeled somatostatin analog, combined with PET/CT imaging, may improve the diagnosis of IPNs over 18F-FDG by reducing false positives. Our study purpose was to test this hypothesis in our region with high endemic granulomatous IPNs. Methods We prospectively performed 68Ga-DOTATATE PET/CT and 18F-FDG PET/CT scans in the same 30 patients with newly diagnosed, treatment-naïve lung cancer (N = 14) or IPNs (N = 15) and one metastatic nodule. 68Ga-DOTATATE SUVmax levels at or above 1.5 were considered likely malignant. We analyzed the scan results, correlating with ultimate diagnosis via biopsy or 2-year chest CT follow-up. We also correlated 68Ga-DOTATATE uptake with immunohistochemical (IHC) staining for SSTR subtype 2A (SSTR2A) in pathological specimens. Results We analyzed 31 lesions in 30 individuals, with 14 (45%) being non-neuroendocrine lung cancers and 1 (3%) being metastatic disease. McNemar’s result comparing the two radiopharmaceuticals (p = 0.65) indicates that their accuracy of diagnosis in this indication are equivalent. 68Ga-DOTATATE was more specific (94% compared to 81%) and less sensitive 73% compared to 93%) than 18F-FDG. 68Ga-DOTATATE uptake correlated with SSTR2A expression in tumor stroma determined by immunohistochemical (IHC) staining in 5 of 9 (55%) NSCLCs. Conclusion 68Ga-DOTATATE and 18F-FDG PET/CT had equivalent accuracy in the diagnosis of non-neuroendocrine lung cancer and 68Ga-DOTATATE was more specific than 18F-FDG for the diagnosis of IPNs. IHC staining for SSTR2A receptor expression correlated with tumor stroma but not tumor cells.




https://veet.via.cornell.edu/cgi-bin/datac/home.cgi

The database currently consists of an image set of 50 low-dose documented whole-lung CT scans for detection. The CT scans were obtained 

in a single breath hold with a 1.25 mm slice thickness. The locations of nodules detected by the radiologist are also provided.
