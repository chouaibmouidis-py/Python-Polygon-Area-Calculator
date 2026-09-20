# Polygon Area Calculator - Python 📐

A Python application that implements geometric calculations for Rectangles and Squares using Object-Oriented Programming (OOP).

## 🚀 Features
- **Geometry Calculations**: Calculate area, perimeter, and diagonal of shapes.
- **Visual Representation**: Generates a text-based visual representation of the shape using asterisks.
- **Containment Logic**: Calculates how many times one shape can fit inside another without rotation.
- **OOP Principles**: Uses inheritance to implement a `Square` class as a specialized version of a `Rectangle`.

## 🛠️ Technical Implementation
- **Inheritance**: The `Square` class inherits from `Rectangle`, overriding specific methods to maintain the square's properties (equal sides).
- **Math Module**: Use of `math.sqrt` for precise diagonal calculations.
- **Input Validation**: Ensures shapes are created with valid dimensions.

## 📖 How to Use
1. Clone the repository.
2. Import the `Rectangle` or `Square` classes into your script.
3. Create an instance: `rect = Rectangle(10, 5)` or `sq = Square(9)`.
4. Call methods like `.get_area()` or `.get_picture()`.

---
*Developed as part of a Python Certification journey.*
