import pandas as pd
import matplotlib.pyplot as plt


file_path = ''


def load_data(file_path):
    return pd.read_csv(file_path)


def get_failed_students(df):
    failed_students = df[(df['Math'] < 50) |
                         (df['Physics'] < 50) |
                         (df['Chemistry'] < 50) |
                         (df['Biology'] < 50) |
                         (df['English'] < 50)]['Student'].unique()
    return failed_students


def calculate_average_per_semester(df):
    average_per_semester = df.groupby('Semester').mean(numeric_only=True)
    return average_per_semester


def get_highest_avg_student(df):
    df['Average Score'] = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
    highest_avg_student = df.groupby('Student')['Average Score'].mean().idxmax()
    return highest_avg_student


def get_lowest_avg_subject(df):
    lowest_avg_subject = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean().idxmin()
    return lowest_avg_subject


def save_average_scores_to_excel(df, output_path):
    average_subject_semester_df = df.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
    average_subject_semester_df.to_excel(output_path)
    return output_path


def plot_subject_avg_bar_chart(df):
    average_scores_all_semesters = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
    plt.figure(figsize=(10, 6))
    average_scores_all_semesters.plot(kind='bar', color=['#ADD7F6', '#87BFFF', '#3F8EFC', '#2667FF', '#3B28CC'])
    plt.title('average score for each subject across all semesters')
    plt.ylabel('average score')
    plt.xlabel('subjects')
    plt.show()


def plot_avg_score_per_semester(df):
    average_overall_per_semester = df.groupby('Semester')['Average Score'].mean()
    plt.figure(figsize=(10, 6))
    average_overall_per_semester.plot(kind='line', marker='o', linestyle='-', color='b')
    plt.title('overall average score by semester')
    plt.ylabel('average score')
    plt.xlabel('semester')
    plt.grid(True)
    plt.show()


df = load_data(file_path)

failed_students = get_failed_students(df)
print("students who failed in any subject:")
print(failed_students)

average_per_semester = calculate_average_per_semester(df)
print("\naverage score for each subject per semester:")
print(average_per_semester)

highest_avg_student = get_highest_avg_student(df)
print(f"\nstudent with the highest average score: {highest_avg_student}")

lowest_avg_subject = get_lowest_avg_subject(df)
print(f"\nsubject with the lowest average score: {lowest_avg_subject}")

excel_output_path = ''
save_path = save_average_scores_to_excel(df, excel_output_path)
print(f"\naverage scores by semester saved to: {save_path}")

plot_subject_avg_bar_chart(df)
plot_avg_score_per_semester(df)


main(file_path)
