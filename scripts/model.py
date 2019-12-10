#%%
from keras import models
from keras import layers
import numpy as np
from keras.backend import clear_session
from keras import losses, metrics
clear_session()
X = np.load("res_train.npy")
y = np.load("res_target.npy")

#%%
# Define two input layers
input_d = int(X.shape[1])
output_d = int(y.shape[1])
model = models.Sequential()
model.add(layers.Dense(128, activation='relu', input_shape=(input_d,)))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(output_d, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss= losses.kullback_leibler_divergence,
              metrics = [metrics.categorical_accuracy])

history = model.fit(X,y,
                    epochs=20,
                    batch_size=512,
                    validation_split=0.2)

model.save("modelv5.h5")

# %%
