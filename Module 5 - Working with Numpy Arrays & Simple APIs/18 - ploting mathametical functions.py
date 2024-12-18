import numpy as np
import matplotlib.pyplot as mp

# Generate sample space
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)  # sine wave

# Print sample space
print('Sample Space : ', x)

# Plot the data
mp.plot(x, y, marker='o', label='Sine Wave')
mp.title('Sine Wave Plot')
mp.xlabel('X-axis')
mp.ylabel('Y-axis')
mp.legend()
mp.grid(True)

# Show the plot
mp.show()
