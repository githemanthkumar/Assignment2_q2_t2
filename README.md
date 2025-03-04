# Assignment2_q2_t2
Input Image:

A random 4x4 matrix is generated using numpy to simulate an input image. The shape of the input matrix is (1, 4, 4, 1), where 1 is the batch size, 4x4 is the size of the image, and 1 is the number of channels (grayscale).
Max Pooling:

A MaxPooling2D layer from TensorFlow/Keras is created with a pool size of 2x2 and a stride of 2. It selects the maximum value from each 2x2 block.
Average Pooling:

Similarly, an AveragePooling2D layer is defined to compute the average of values within each 2x2 block.
Results:

The original matrix, max-pooled matrix, and average-pooled matrix are printed.
