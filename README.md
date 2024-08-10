# Study Plan Generator

## Overview

The **Study Plan Generator** is a Streamlit application that helps you create a personalized study schedule for various courses. The application allows you to select courses, choose a start date, set daily study hours, and decide how many courses you want to study in parallel. Based on your selections, the application generates a detailed study plan, outlining how much time you should spend on each course daily.

## Features

- **Course Selection with Images**: Choose courses from a visually appealing grid layout with course images and captions.
- **Customizable Study Hours**: Set daily study hours between 1 and 24 hours.
- **Parallel Course Selection**: Choose to study between 1 and 5 courses in parallel.
- **Automated Schedule Generation**: The application calculates and generates a study plan based on the selected courses and study hours.
- **Detailed Study Plan**: The generated study plan is presented in a well-organized table format.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository/study-plan-generator.git


2. **Navigate to the Project Directory:**:
    ```bash
    cd study-plan-generator

3. **Install Dependencies:**:
Make sure you have Python installed, then install the required packages:
    ```bash
    pip install -r requirements.txt

4. **Run the Application:**:
    ```bash
    streamlit run app.py

## Usage:
1. **Course Selection:**
    - The course selection section displays images for each course in a grid format.

2. **Input Study Parameters:**
    - <b>Start Date</b>: Select the date when you plan to begin your study.
    - <b>Daily Study Hours</b>: Use the slider to choose how many hours per day you want to study.
    - <b>Parallel Courses</b>: Use the slider to select how many courses you want to study at the same time.

3. **Generate Study Plan:**

    - Click the "Generate Study Plan" button to create a custom study schedule based on your inputs.
    - The study plan will be displayed in a table, showing the date, course name, allocated time, and remaining time for each course.


## TO-DO:
- Use a dynamic way for updating the courses time instead of using a static way




