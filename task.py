import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

fake = Faker('ru_RU')
random.seed(42)
np.random.seed(42)
years = [2021, 2022, 2023, 2024, 2025]
forms = ["очная", "заочная"]
specialties = ["Прикладная Информатика", "Кибербезопасность", "Радиофизика"]
subjects = ["Математика", "Физика", "Язык"]
students = []
for _ in range(300):  
    fio = fake.name()
    year = random.choice(years)
    form = random.choice(forms)
    speciality = random.choice(specialties)
    math_score = max(0, min(100, np.random.normal(75, 12)))
    physics_score = max(0, min(100, np.random.normal(70, 15)))
    language_score = max(0, min(100, np.random.normal(80, 10)))
    avg_exam_score = (math_score + physics_score + language_score) / 3
    att_score = max(1, min(10, np.random.normal(8.2, 0.8)))
    total_score = math_score + physics_score + language_score + att_score*10 
    address = fake.city()
    phone = fake.phone_number()
    students.append({
        "ФИО": fio,
        "Год поступления": year,
        "Форма обучения": form,
        "Специальность": speciality,
        "Балл_Математика": round(math_score, 1),
        "Балл_Физика": round(physics_score, 1),
        "Балл_Язык": round(language_score, 1),
        "Балл_ЦЭ_ЦТ": round(avg_exam_score, 1),  
        "Балл_аттестата": round(att_score, 1),
        "Общий_балл": round(total_score, 1),
        "Адрес": address,
        "Телефон": phone,
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