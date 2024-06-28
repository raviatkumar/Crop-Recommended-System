# Project Title: Crop Recommendation System

#### Problem Statement:

Precision agriculture is revolutionizing the way farming is conducted by leveraging data-driven techniques to enhance decision-making and optimize agricultural practices. In the modern era, where food security and sustainable farming practices are paramount, it is crucial to utilize advanced technologies to guide farmers in their cultivation choices. Precision agriculture enables farmers to make informed decisions about various farming strategies, from the selection of crops to the management of soil nutrients and irrigation schedules.

However, the challenge lies in the effective utilization of data to recommend the most suitable crops for specific farm conditions. Each farm is unique, with varying soil compositions, climatic conditions, and environmental factors. Traditional farming methods often rely on experience and generalized practices, which may not be optimal for maximizing crop yield and ensuring soil health. This project aims to address this challenge by developing a predictive model that recommends the most suitable crops to grow in a particular farm based on a comprehensive analysis of various parameters.

The dataset provided contains crucial information that influences crop suitability and growth. The following data fields are included:

- **N (Nitrogen content in soil)**: Nitrogen is a critical nutrient for plant growth, influencing various physiological processes. An appropriate balance of nitrogen is essential for healthy plant development and optimal yield.
  
- **P (Phosphorous content in soil)**: Phosphorous plays a significant role in energy transfer and photosynthesis in plants. Adequate phosphorous levels are necessary for root development and flowering.
  
- **K (Potassium content in soil)**: Potassium regulates water uptake and enzyme activation in plants. It is vital for overall plant health and resistance to diseases.
  
- **Temperature**: The temperature in degree Celsius affects the metabolic rates of plants. Different crops have specific temperature ranges for optimal growth.
  
- **Humidity**: Relative humidity in percentage impacts transpiration and water uptake in plants. Maintaining appropriate humidity levels is crucial for preventing diseases and ensuring healthy plant growth.
  
- **pH value of the soil**: Soil pH affects nutrient availability and microbial activity. Different crops thrive in specific pH ranges, making it essential to match crop selection with soil pH.
  
- **Rainfall**: Rainfall in millimeters influences water availability for crops. Sufficient rainfall is necessary for crop growth, while excessive or insufficient rainfall can adversely affect yields.

The objective of this project is to develop a machine learning model that leverages these parameters to predict the most suitable crop for a given set of conditions. By analyzing the data, the model will learn the relationships between the various factors and the optimal crop choices. This recommendation system will empower farmers with actionable insights, enabling them to make data-driven decisions that enhance crop yield, soil health, and overall farm productivity.

Dataset Link : https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

### Random Forest Gives Best Result

### Installation

To install the required packages for this project, use the following command after creating a virtual environment:

```bash
pip install -r requirements.txt
```

*Note: The model was trained on Google Colab with GPU support.*

### How to Run the App

After installing the necessary packages, run the following command from the project root directory to start the app:

```bash
pip install Flask
```

```bash
uvicorn app:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) from your browser to access Swagger. You can upload an image through the predict endpoint and receive a JSON response. Use the `--reload` argument to see immediate effects when changing code.


### Output 
![Alt text](https://github.com/raviatkumar/Crop-Recommended-System/blob/main/Output/crop.PNG?raw=true)
