# Title: Advanced AI Tuberculosis Detection Analysis

## Domain: Medical Imaging

## Introduction:

### Background

Tuberculosis (TB) is a leading infectious disease in Ethiopia, killing more people than HIV and malaria combined. In 2022, TB killed over 19,000 people in Ethiopia, which is more than two deaths every hour. The World Health Organization (WHO) estimates that about 30% of TB cases in Ethiopia go undetected by the healthcare system, which can lead to unnecessary deaths.

> Source : U.S. Embassy Addis Ababa ,United States Agency for International Development(USAID)

### Goal and Objective

The goal of this research is to build a resilient AI system for tuberculosis detection involves training advanced models on diverse medical images and refining them for precise identification of tuberculosis-related anomalies using techniques like data augmentation to enhance performance across various imaging types.

### Dataset:

We have used Tuberculosis (TB) Chest X-ray Database to train and evaluate our model.

#### [Tuberculosis (TB) Chest X-ray Cleaned Database](https://www.kaggle.com/datasets/scipygaurav/tuberculosis-tb-chest-x-ray-cleaned-database/data)

The Tuberculosis (TB) Chest X-ray Database is a collaborative effort between researchers from Qatar University, Doha, Qatar, and the University of Dhaka, Bangladesh, and their counterparts from Malaysia, in association with medical practitioners from Hamad Medical Corporation and Bangladesh. The database consists of chest X-ray images of both normal individuals (3500) and TB positive cases (700 publicly accessible images and 2800 images that can be obtained from the NIAID TB portal[3] by signing a data-sharing agreement).

Contribution

This dataset contains CXR images of Normal (3500) and patients with TB (700 TB images in publicly accessible and 2800 TB images can be downloaded from NIAID TB portal[3] by signing an agreement). The TB database is collected from the source:
NLM dataset: National Library of Medicine (NLM) in the U.S. [1] has made two lung X-ray datasets publicly available: the Montgomery and Shenzhen datasets.

Belarus dataset: Belarus Set [2] was collected for a drug resistance study initiated by the National Institute of Allergy and Infectious Diseases, Ministry of Health, Republic of Belarus.

NIAID TB dataset: NIAID TB portal program dataset [3], which contains about 3000 TB positive CXR images from about 3087 cases. Weblink: https://tbportals.niaid.nih.gov/download-data

RSNA CXR dataset: RSNA pneumonia detection challenge dataset [4], which is comprised of about 30,000 chest X-ray images, where 10,000 images are normal and others are abnormal and lung opacity images.

Objective

Researchers can use this database to produce useful and impactful scholarly work on TB, which can help in tackling this issue.

### Run Locally

Step 1. Clone the repository

```bash
clone the repository
```

Step 2. Go to the project directory

```bash
cd medical-imaging
```

Step 3. Start Backend Server

```bash
cd backend

# create virtual environment
python -m venv venv # or python3 -m venv venv
# activate virtual environment
source venv/bin/activate  # source venv/Scripts/activate (for windows)

# install dependencies
pip install -r dev-requirements.txt

# install tensorflow
pip install tensorflow

# start server
python app.py

#  or run
uvicorn app:app --reload

```

Step 4. Start Frontend Server

```bash
cd frontend

# install dependencies
npm install

# copy env file
cp .env.example .env.local

# start server
npm run dev

# open browser and go to http://localhost:3000
```