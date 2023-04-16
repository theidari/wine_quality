import tensorflow as tf

# create and train a keras neural network
classifier = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1]),
    tf.keras.layers.Dense(units=28, activation='relu'),
    tf.keras.layers.Dense(units=1)
])
classifier.compile(optimizer='sgd', loss='mean_squared_error')
classifier.fit(x=[-1, 0, 1], y=[-3, -1, 1], epochs=5)


# Convert the model to a Tensorflow Lite object
converter = tf.lite.TFLiteConverter.from_keras_model(classifier)
tfl_classifier = converter.convert()

# Save the model as a .tflite file
with open('classifier.tflite', 'wb') as f:
  f.write(tfl_classifier)