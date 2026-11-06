


import pandas as pd
import plotly.express as px

# 1. قراءة البيانات من ملف CSV محلي
# تأكد أن الملف weather_data.csv موجود في نفس مجلد الكود
try:
    df = pd.read_csv('weather_data.csv')
    df['Date'] = pd.to_datetime(df['Date']) # تحويل التاريخ لنوع صحيح
    
    print("تم تحميل بيانات الطقس بنجاح!")
    print(df.head()) # عرض عينة من البيانات في الـ Terminal

    # 2. رسم بياني خطي لتغير درجات الحرارة عبر الزمن لكل مدينة
    fig_temp = px.line(
        df, 
        x='Date', 
        y='Temperature', 
        color='City',
        title='تغير درجات الحرارة اليومية حسب المدينة',
        markers=True, # إضافة نقاط على الخط
        labels={'Temperature': 'درجة الحرارة (°C)', 'Date': 'التاريخ'}
    )

    # 3. رسم بياني أعمدة لمقارنة متوسط الرطوبة بين المدن
    avg_humidity = df.groupby('City')['Humidity'].mean().reset_index()
    fig_hum = px.bar(
        avg_humidity, 
        x='City', 
        y='Humidity',
        title='متوسط نسبة الرطوبة في كل مدينة',
        color='City',
        labels={'Humidity': 'نسبة الرطوبة %'}
    )

    # 4. رسم بياني دائري (Pie Chart) لتوزيع حالات الطقس
    fig_pie = px.pie(
        df, 
        names='Condition', 
        title='توزيع حالات الطقس العامة (مشمس، ممطر، إلخ)',
        hole=0.3 # جعلها بشكل "Donut" لتبدو أجمل
    )

    # 5. عرض الرسوم البيانية
    fig_temp.show()
    fig_hum.show()
    fig_pie.show()

except FileNotFoundError:
    print("خطأ: لم يتم العثور على ملف 'weather_data.csv'. تأكد من وجوده في نفس المجلد.")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")


