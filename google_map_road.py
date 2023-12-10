
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint


def load_and_preprocess_dataset(dataset_path):
    images = []
    labels = []

    class_mapping = {'Animaux': 0, 'Femme': 1, 'NonVisibiliteRue': 2, 'ObstacleVoiture': 3, 'Other': 4}


    for filename in os.listdir(dataset_path):
        img_path = os.path.join(dataset_path, filename)
        class_name = filename.split('.')[0]

        if class_name in class_mapping:
            label = class_mapping[class_name]
        else:
            label = class_mapping['Other'] 

        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, (224, 224))

            images.append(img)
            labels.append(label)

    if not images:
        raise ValueError("Aucune image n'a été chargée. Vérifiez le chemin d'accès de votre ensemble de données.")

    images = np.array(images) / 255.0
    labels = np.array(labels)

    num_classes = len(class_mapping)
    labels_one_hot = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

    X_train, X_temp, y_train, y_temp = train_test_split(images, labels_one_hot, test_size=0.2, random_state=42)

    if not X_train.any():
        raise ValueError("Aucun échantillon n'est disponible pour l'ensemble d'entraînement. Assurez-vous d'avoir suffisamment d'échantillons.")

    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

    return X_train, X_val, X_test, y_train, y_val, y_test



dataset_path = "/home/khaoula/Bureau/dataset/Fog"
X_train, X_val, X_test, y_train, y_val, y_test = load_and_preprocess_dataset(dataset_path)

def create_faster_rcnn_model(num_classes):
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    x = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(base_model.output)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(256, activation='relu')(x)

    class_output = layers.Dense(num_classes, activation='softmax', name='class_output')(x)
    bbox_output = layers.Dense(3, name='bbox_output')(x)


    model = Model(inputs=base_model.input, outputs=[class_output, bbox_output])

    return model

num_classes = 3
faster_rcnn_model = create_faster_rcnn_model(num_classes)

faster_rcnn_model.compile(optimizer=Adam(), loss={'class_output': 'categorical_crossentropy', 'bbox_output': 'mse'})

checkpoint_callback = ModelCheckpoint('faster_rcnn_model.h5', save_best_only=True)
faster_rcnn_model.fit(X_train, {'class_output': y_train, 'bbox_output': np.zeros_like(y_train)},
                       validation_data=(X_val, {'class_output': y_val, 'bbox_output': np.zeros_like(y_val)}),
                       epochs=10, callbacks=[checkpoint_callback])
new_image_path = "/home/khaoula/Bureau/dataset_test/Fog/28971289.png"
new_image = cv2.imread(new_image_path)
new_image = cv2.resize(new_image, (224, 224)) 

new_image = new_image / 255.0

new_image = np.expand_dims(new_image, axis=0)

predictions = faster_rcnn_model.predict(new_image)

class_predictions = predictions[0]
bbox_predictions = predictions[1]

print("Prédictions de classe :", class_predictions)
print("Prédictions de boîte englobante :", bbox_predictions)
  
