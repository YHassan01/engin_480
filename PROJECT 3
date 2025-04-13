import numpy as np
import matplotlib.pyplot as plt

class WindFarmBoundary:
    def __init__(self, name, coordinates):
        """
        Initializes the WindFarmBoundary object.

        Args:
            name (str): Name of the wind farm.
            coordinates (list of tuples): List of (longitude, latitude) pairs.
        """
        self.name = name
        self.coordinates = coordinates
        self.array = np.array(coordinates)

    def get_array(self):
        return self.array

    def plot(self):
        """
        Plots the boundary using matplotlib.
        """
        x, y = self.array[:, 0], self.array[:, 1]
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, marker='o', linestyle='-', color='blue')
        plt.fill(x, y, color='skyblue', alpha=0.3)
        plt.title(f"Boundary of {self.name}")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.grid(True)
        plt.axis("equal")
        plt.show()

# Example usage
eystrasalt_coords = [
    (17.004, 57.008),
    (17.005, 57.005),
    (17.005, 57.001),
    (17.005, 56.998),
    (17.006, 56.994),
    (17.004, 57.008)  # close the polygon
]

eystrasalt = WindFarmBoundary("Eystrasalt", eystrasalt_coords)
print("Numpy array of boundary:")
print(eystrasalt.get_array())

# Plot
eystrasalt.plot()