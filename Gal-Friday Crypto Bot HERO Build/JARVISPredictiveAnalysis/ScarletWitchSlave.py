
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

class ScarletWitchSlave:
    def __init__(self, input_shape, output_shape):
        """
        Initialize and compile the LSTM with Attention model.
        """
        # Initialize LSTM model with Attention Mechanism
        self.model = tf.keras.Sequential([
            tf.keras.layers.LSTM(50, return_sequences=True, input_shape=input_shape),
            tf.keras.layers.Attention(),
            tf.keras.layers.Dense(output_shape)
        ])
        # Compile the model
        self.model.compile(optimizer='adam', loss='mse')
        self.scaler = MinMaxScaler()
    
    def preprocess_data(self, data):
        """
        Preprocess the data: scaling and reshaping.
        """
        # Scaling the features
        data = self.scaler.fit_transform(data)
        # Reshaping the data to 3D array
        data = np.reshape(data, (data.shape[0], data.shape[1], 1))
        return data

    def train_model(self, X, y, epochs=10, batch_size=32):
        """
        Train the model.
        """
        X = self.preprocess_data(X)
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, X):
        """
        Predict using the LSTM with Attention model.
        """
        X = self.preprocess_data(X)
        return self.model.predict(X)

    def evaluate_model(self, X, y):
        """
        Evaluate the model using Mean Squared Error (MSE).
        """
        X = self.preprocess_data(X)
        return self.model.evaluate(X, y)
