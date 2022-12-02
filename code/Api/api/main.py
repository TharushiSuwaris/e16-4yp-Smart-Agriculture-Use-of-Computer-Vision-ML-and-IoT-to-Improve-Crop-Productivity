from fastapi import FastAPI , File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PORT = 8000

# using the https://colab.research.google.com/drive/1uw9d4F_zLY3w9BpEWQ526z_LUvGECie3#scrollTo=f_UkvjZGv47y saved cnn model (this will be our model)
MODEL = tf.keras.models.load_model("../saved_models/1")   
#MODELRCNN = tf.keras.models.load_model("../rcnn/saved_models/2")    we can use all of our models, with api versioning 

CLASS_NAMES = ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']


@app.get("/ping")
async def ping():
    return f"Leaf disease prediction server is running on port {PORT}"

@app.post("/modelcnn/predict")                       #can use other models too         # todo: postman not working withh files
async def predict(file: UploadFile = File(...)):
    
    image = read_file_as_image(await file.read())   # await to free while reading file (async i/o)
      
    # predict with model
    img_batch = np.expand_dims(image, 0)   # predict function input has to be a image batch
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0]) 
    
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

#helper functin to read image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)