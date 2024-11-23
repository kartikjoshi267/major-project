import matplotlib.pyplot as plt

# Data
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mse = [2.6503, 2.6819, 2.7905, 2.9185, 2.9360, 2.9539, 2.9150, 2.9276, 2.9703, 2.9785]
accuracy = [0.9245, 0.9245, 0.9085, 0.8475, 0.8590, 0.8630, 0.8380, 0.8365, 0.8900, 0.8800]
precision = [0.0, 0.0, 0.1667, 0.2722, 0.3009, 0.3164, 0.2895, 0.2934, 0.3883, 0.3760]
recall = [0.0, 0.0, 0.0530, 0.6093, 0.6556, 0.7020, 0.7881, 0.8278, 0.7947, 0.8940]
f1_score = [0.0, 0.0, 0.0804, 0.3763, 0.4125, 0.4362, 0.4235, 0.4333, 0.5217, 0.5294]

# Plotting
plt.figure(figsize=(12, 8))

# Plot MSE
plt.subplot(2, 2, 1)
plt.plot(epochs, mse, marker='o', color='blue', label='MSE')
plt.title('Epoch vs MSE')
plt.xlabel('Epochs')
plt.ylabel('MSE')
plt.grid(True)
plt.legend()

# Plot Accuracy
plt.subplot(2, 2, 2)
plt.plot(epochs, accuracy, marker='o', color='green', label='Accuracy')
plt.title('Epoch vs Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.grid(True)
plt.legend()

# Plot Precision
plt.subplot(2, 2, 3)
plt.plot(epochs, precision, marker='o', color='orange', label='Precision')
plt.title('Epoch vs Precision')
plt.xlabel('Epochs')
plt.ylabel('Precision')
plt.grid(True)
plt.legend()

# Plot Recall
plt.subplot(2, 2, 4)
plt.plot(epochs, recall, marker='o', color='red', label='Recall')
plt.title('Epoch vs Recall')
plt.xlabel('Epochs')
plt.ylabel('Recall')
plt.grid(True)
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()
