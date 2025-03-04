import tensorflow as tf
import numpy as np

# Create a random 4x4 matrix as input (simulate an image)
input_matrix = np.random.randint(0, 10, (1, 4, 4, 1))  # Shape: (batch_size, height, width, channels)

# Define a 2x2 Max Pooling operation
max_pooling = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2)

# Define a 2x2 Average Pooling operation
avg_pooling = tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides=2)

# Apply Max Pooling
max_pooled_matrix = max_pooling(input_matrix)

# Apply Average Pooling
avg_pooled_matrix = avg_pooling(input_matrix)

# Print the results
print("Original Matrix (Input Image):")
print(input_matrix[0, :, :, 0])  # Remove batch and channel dimensions for easier viewing

print("\nMax Pooled Matrix (2x2):")
print(max_pooled_matrix[0, :, :, 0])

print("\nAverage Pooled Matrix (2x2):")
print(avg_pooled_matrix[0, :, :, 0])
