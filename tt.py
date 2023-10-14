import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, UpSampling1D

# Create the CNN model
def create_cnn_model(input_shape):
    model = Sequential()
    model.add(Conv1D(16, 3, activation='relu', padding='same', input_shape=input_shape))
    model.add(MaxPooling1D(2, padding='same'))
    model.add(Conv1D(8, 3, activation='relu', padding='same'))
    model.add(MaxPooling1D(2, padding='same'))
    model.add(Conv1D(8, 3, activation='relu', padding='same'))
    model.add(UpSampling1D(2))
    model.add(Conv1D(16, 3, activation='relu', padding='same'))
    model.add(UpSampling1D(2))
    model.add(Conv1D(1, 3, activation='sigmoid', padding='same'))
    return model

# Train the CNN model to denoise the list
def train_cnn_model(X_train, Y_train, epochs=20):
    input_shape = X_train.shape[1:]
    model = create_cnn_model(input_shape)
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.summary()
    model.fit(X_train, Y_train, epochs=epochs, batch_size=32, verbose=1)
    return model

# Denoise the given list using the trained CNN model
def denoise_list(input_list, window_size=10, epochs=20):
    X_train = []
    Y_train = []
    for i in range(len(input_list) - window_size):
        X_train.append(input_list[i:i + window_size])
        Y_train.append(input_list[i + window_size])
    X_train = np.array(X_train)
    Y_train = np.array(Y_train)

    # Reshape data for CNN
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    Y_train = np.reshape(Y_train, (Y_train.shape[0], 1))

    model = train_cnn_model(X_train, Y_train, epochs)

    # Denoise the list using the trained model
    denoised_list = []
    for i in range(len(input_list) - window_size):
        input_data = np.array([input_list[i:i + window_size]])
        input_data = np.reshape(input_data, (input_data.shape[0], input_data.shape[1], 1))
        predicted_value = model.predict(input_data)
        denoised_list.append(predicted_value[0][0])

    return denoised_list

# Function to calculate the sine function
def sine_function(t):
    return np.sin(2*np.pi*3*t) + np.sin(2*np.pi*7*t)  # Example sine function with two frequencies

# Main function to denoise the list and fit it to the sine function
def denoise_and_fit_to_sine(input_list):
    t = np.linspace(0, 5, len(input_list))
    denoised_list = denoise_list(input_list)
    fitted_sine = denoised_list + sine_function(t)  # Fit to the sine function by adding the sine function values to the denoised list
    return t, denoised_list, fitted_sine

# Example usage:
input_list = [2.0, 2.5, 3.2, 2.8, 1.9, 2.4, 3.1, 2.6, 1.8, 2.3]
t, denoised_list, fitted_sine = denoise_and_fit_to_sine(input_list)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, input_list, label='Original List', color='b')
plt.plot(t, denoised_list, label='Denoised List', color='r', alpha=0.7)
plt.plot(t, fitted_sine, label='Fitted Sine', color='g', linestyle='dashed')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Denoising List and Fitting to Sine Function')
plt.show()