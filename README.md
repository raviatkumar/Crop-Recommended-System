# Project Title : Crop Recommendation

Problem Statement : Precision agriculture is in trend nowadays. It helps the farmers to get informed decision about the farming strategy. Here, I present you a dataset which would allow the users to build a predictive model to recommend the most suitable crops to grow in a particular farm based on various parameters.

https://github.com/raviatkumar/Crop-Recommended-System/assets/125804537/6d7d9880-03b9-46f4-aa45-5985e45a30bc

### Data fields :

N - ratio of Nitrogen content in soil

P - ratio of Phosphorous content in soil

K - ratio of Potassium content in soil

temperature - temperature in degree Celsius

humidity - relative humidity in %

ph - ph value of the soil

rainfall - rainfall in mm
label

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
python app.py
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) from your browser to access Swagger. You can upload an image through the predict endpoint and receive a JSON response. Use the `--reload` argument to see immediate effects when changing code.


### Output 
![Alt text](https://github.com/raviatkumar/Crop-Recommended-System/blob/main/Output/crop.PNG?raw=true)
