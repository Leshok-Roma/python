from faker import Faker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

fake = Faker('ru_RU')
Faker.seed(42)

years = [2021, 2022, 2023, 2024, 2025]
forms = ["очная", "заочная"]
specialties = ["Прикладная Информатика", "Кибербезопасность", "Радиофизика"]

students = []

for _ in range(300):
    math_score = fake.pyfloat(min_value=55, max_value=95, right_digits=1)
    physics_score = fake.pyfloat(min_value=50, max_value=90, right_digits=1)
    language_score = fake.pyfloat(min_value=65, max_value=95, right_digits=1)
    att_score = fake.pyfloat(min_value=7.0, max_value=9.5, right_digits=1)
    avg_exam_score = (math_score + physics_score + language_score) / 3
    total_score = math_score + physics_score + language_score + att_score * 10
    students.append({
        "ФИО": fake.name(),
        "Год поступления": fake.random_element(years),
        "Форма обучения": fake.random_element(forms),
        "Специальность": fake.random_element(specialties),
        "Балл_Математика": round(math_score, 1),
        "Балл_Физика": round(physics_score, 1),
        "Балл_Язык": round(language_score, 1),
        "Балл_ЦЭ_ЦТ": round(avg_exam_score, 1),
        "Балл_аттестата": round(att_score, 1),
        "Общий_балл": round(total_score, 1),
        "Адрес": fake.city(),
        "Телефон": fake.phone_number()
    })

df = pd.DataFrame(students)

plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
subject_columns = ['Балл_Математика', 'Балл_Физика', 'Балл_Язык']
subject_means = df.groupby('Год поступления')[subject_columns].mean()
years_list = sorted(df['Год поступления'].unique())
x_pos = np.arange(len(years_list))
width = 0.25
plt.bar(x_pos - width, subject_means['Балл_Математика'], width, label='Математика', alpha=0.8)
plt.bar(x_pos, subject_means['Балл_Физика'], width, label='Физика', alpha=0.8)
plt.bar(x_pos + width, subject_means['Балл_Язык'], width, label='Язык', alpha=0.8)
plt.xlabel('Год поступления')
plt.ylabel('Средний балл')
plt.title('Динамика среднего балла по предметам', fontweight='bold')
plt.xticks(x_pos, years_list)
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
att_dynamic = df.groupby('Год поступления')['Балл_аттестата'].mean()
plt.plot(att_dynamic.index, att_dynamic.values, marker='o', linewidth=2, markersize=8, color='green')
plt.xlabel('Год поступления')
plt.ylabel('Средний балл аттестата')
plt.title('Динамика среднего балла аттестата', fontweight='bold')
plt.grid(True, alpha=0.3)
plt.ylim(7, 9)

plt.subplot(2, 2, 3)
passing_scores = df.groupby(['Год поступления', 'Специальность'])['Общий_балл'].min().unstack()
passing_scores.plot(kind='line', marker='o', ax=plt.gca())
plt.xlabel('Год поступления')
plt.ylabel('Проходной балл')
plt.title('Динамика проходного балла по специальностям', fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.subplot(2, 2, 4)
year_counts = df['Год поступления'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values, color='skyblue', alpha=0.8)
plt.xlabel('Год поступления')
plt.ylabel('Количество студентов')
plt.title('Количество поступивших по годам', fontweight='bold')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
specialty_counts = df['Специальность'].value_counts()
plt.pie(specialty_counts.values, labels=specialty_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Распределение по специальностям', fontweight='bold')

plt.subplot(1, 2, 2)
form_counts = df['Форма обучения'].value_counts()
plt.pie(form_counts.values, labels=form_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Статистика по формам обучения', fontweight='bold')

plt.tight_layout()
plt.show()  

plt.figure(figsize=(10, 6))
subject_corr = df[['Балл_Математика', 'Балл_Физика', 'Балл_Язык', 'Балл_аттестата', 'Общий_балл']].corr()
sns.heatmap(subject_corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Корреляция между баллами по предметам', fontweight='bold')
plt.tight_layout()
plt.show()

print("\nСредние баллы по годам:")
yearly_stats = df.groupby('Год поступления')[['Балл_Математика', 'Балл_Физика', 'Балл_Язык', 'Балл_аттестата', 'Общий_балл']].mean().round(2)
print(yearly_stats)
print("\nПример записей:")
print(df.head(), '\n')
print("\nПроходные баллы по специальностям:")
passing_by_specialty = df.groupby('Специальность')['Общий_балл'].min().sort_values(ascending=False)
print(passing_by_specialty.round(1).to_string())
print("\nКоличество студентов по специальностям:")
print(df['Специальность'].value_counts().to_string())
print("\nКоличество студентов по формам обучения:")
print(df['Форма обучения'].value_counts().to_string())
print("\nКорреляция между предметами:")
subject_corr = df[['Балл_Математика', 'Балл_Физика', 'Балл_Язык', 'Балл_аттестата', 'Общий_балл']].corr()
print(subject_corr.round(3))