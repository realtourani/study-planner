import streamlit as st
from datetime import datetime, timedelta
from dateutil.parser import parse
import pandas as pd

# Define course times in minutes
course_times = {
    'Machine Learning 101': 249,  # 4 hours 9 minutes
    'Statistics': 262,            # 4 hours 22 minutes
    'Data processing': 1053,      # 17 hours 33 minutes
    'Data Visualization': 187,    # 3 hours 7 minutes
    'Machine Learning': 396       # 6 hours 36 minutes
}

# Order in which to study courses
study_order = [
    'Machine Learning 101',
    'Statistics',
    'Data processing',
    'Data Visualization',
    'Machine Learning'
]

# Image URLs for courses (replace with your actual images or image paths)
course_images = {
    'Machine Learning 101': 'https://api.pytopia.ai/media/course/course_logos/Project_Based_Python_Github_3_1.png',
    'Statistics': 'https://api.pytopia.ai/media/course/course_logos/Untitled_design_6.png',
    'Data processing': 'https://api.pytopia.ai/media/course/course_logos/pandas.webp',
    'Data Visualization': 'https://api.pytopia.ai/media/course/course_logos/seaborn.webp',
    'Machine Learning': 'https://api.pytopia.ai/media/course/course_logos/Untitled_design_4.png'
}

def minutes_to_hours_and_minutes(minutes):
    """Convert minutes to hours and minutes."""
    return minutes // 60, minutes % 60

def format_time(hours, minutes):
    """Format time in hours and minutes."""
    return f"{hours} hour(s) & {minutes} minute(s)"

def generate_study_plan(start_date, daily_study_hours, selected_courses, parallel_courses):
    start_date = parse(start_date).date()  # Parse the start date
    daily_study_minutes = daily_study_hours * 60  # Convert study hours to minutes
    time_per_course_per_day = daily_study_minutes / parallel_courses  # Allocate time per course

    # Initialize the schedule
    schedule = []
    remaining_times = {course: course_times[course] for course in selected_courses}

    # Sort the courses based on study order
    ordered_courses = [course for course in study_order if course in selected_courses]
    current_date = start_date

    while any(remaining_times.values()):
        daily_allocations = []
        total_allocated_today = 0

        for course in ordered_courses:
            if remaining_times[course] > 0:
                allocated_today = min(time_per_course_per_day, remaining_times[course], daily_study_minutes - total_allocated_today)
                remaining_times[course] -= allocated_today

                allocated_hours, allocated_minutes = minutes_to_hours_and_minutes(allocated_today)
                remaining_hours, remaining_minutes = minutes_to_hours_and_minutes(remaining_times[course])

                daily_allocations.append({
                    'Date': current_date.strftime('%Y-%m-%d'),
                    'Course': course,
                    'Time': format_time(allocated_hours, allocated_minutes),
                    'Remaining Time': format_time(remaining_hours, remaining_minutes)
                })

                total_allocated_today += allocated_today
                if total_allocated_today >= daily_study_minutes:
                    break

        if daily_allocations:
            schedule.extend(daily_allocations)
        
        current_date += timedelta(days=1)  # Move to the next day

    # Convert the schedule into a DataFrame for better presentation
    df_schedule = pd.DataFrame(schedule)

    return df_schedule

# Streamlit GUI
st.title("Study Plan Generator")

# Course selection with images
st.subheader("Select your courses")
selected_courses = []

# Define the grid layout for displaying images
grid_size = 2  # Number of images per row
for i, (course, img) in enumerate(course_images.items()):
    if i % grid_size == 0:
        st.write("---")  # Separate each row with a horizontal line
        cols = st.columns(grid_size)  # Create columns for each image in the row
    
    with cols[i % grid_size]:
        st.image(img, width=200, caption=course, use_column_width='always')
        st.markdown("<br>", unsafe_allow_html=True)  # Add space between images
        if st.checkbox(course):
            selected_courses.append(course)

st.write("---")  # Separate each row with a horizontal line

# Input for start date
start_date = st.date_input("Select start date", value=datetime.today())

# Input for daily study hours
daily_study_hours = st.slider("Daily study hours", min_value=1, max_value=24, value=5)

# Input for parallel courses
parallel_courses = st.slider("Number of parallel courses", min_value=1, max_value=5, value=1)

# Generate the study plan
if st.button("Generate Study Plan"):
    if not selected_courses:
        st.warning("Please select at least one course.")
    else:
        study_plan_df = generate_study_plan(str(start_date), daily_study_hours, selected_courses, parallel_courses)
        st.subheader("Your Study Plan")
        st.dataframe(study_plan_df)
