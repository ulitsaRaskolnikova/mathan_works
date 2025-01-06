import numpy as np
import matplotlib.pyplot as plt

def function(x, y):
    return (x**2 - x * y + 2 * y**2) * np.exp(x + 2 * y)

def calculate_gradient(x, y):
    grad_x = (2 * x - y) * np.exp(x + 2 * y) + (x**2 - x * y + 2 * y**2) * np.exp(x + 2 * y)
    grad_y = (-x + 4 * y) * np.exp(x + 2 * y) + 2 * (x**2 - x * y + 2 * y**2) * np.exp(x + 2 * y)
    return np.array([grad_x, grad_y])

initial_position = np.array([1.0, 1.0])
learning_rate = 0.0003
gradient_threshold = 1e-5
position_threshold = 1e-5
max_iterations = 100000

position = initial_position
path = [position]

for _ in range(max_iterations):
    gradient = calculate_gradient(*position)
    new_position = position - learning_rate * gradient
    path.append(new_position)

    if np.linalg.norm(gradient) < gradient_threshold:
        break
    if np.linalg.norm(new_position - position) < position_threshold:
        break

    position = new_position

optimum_position = position

expected_position = np.array([0, 0])
actual_function_value = function(*optimum_position)
expected_function_value = function(*expected_position)

print(f"Полученная точка: {optimum_position}")
print(f"Ожидаемая точка: {expected_position}")
print(f"Разница: {np.linalg.norm(optimum_position - expected_position)}")
print(f"Знчение функции в полученной точке: {actual_function_value}")
print(f"Знчение функции в ожидаемой точке: {expected_function_value}")

trajectory = np.array(path)
x_path, y_path = trajectory[:, 0], trajectory[:, 1]
z_path = np.array([function(x, y) for x, y in trajectory])

x_values = np.linspace(-4, 4, 400)
y_values = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x_values, y_values)
Z = function(X, Y)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121)
ax1.contourf(X, Y, np.log1p(Z), cmap='viridis', levels=50)
ax1.plot(x_path, y_path, color='blue', marker='o', label="Process Path")
ax1.scatter(optimum_position[0], optimum_position[1], color='red', s=100, label="Optimum", zorder=5)
ax1.set_title("XY Plane Projection")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, rstride=5, cstride=5)
ax2.plot(x_path, y_path, z_path, color='blue', marker='o', label="Process Path")
ax2.scatter(optimum_position[0], optimum_position[1], function(*optimum_position), color='red', s=100, label="Optimum")
ax2.set_title("Function Surface with Process Path")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("Function Value")
ax2.legend()

plt.tight_layout()
plt.show()