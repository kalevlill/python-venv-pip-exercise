import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Example numbers from 0-9
y = [i**2 for i in x] # Square numbers
z = [i**3 for i in x] # Cubic numbers

# Create a line chart
plt.plot(x, y, label='Square numbers')
plt.plot(x, z, label='Cubic numbers')

# Titel and axis labels
plt.title('Square numbers from 0 to 9')
plt.xlabel('Number',  rotation="horizontal")
plt.ylabel('Cubes and Squares', rotation="horizontal")

# Show legend
plt.legend()

# Save as png
plt.savefig('foo.png')

# Show Diagram
plt.show()


