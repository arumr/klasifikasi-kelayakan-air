# Laporan Proyek Machine Learning
### Nama : Arum Rahmah Romadhoni
### Nim : 211351029
### Kelas : Pagi B

## Domain Proyek

Air menjadi bagian penting dan tak terpisahkan dari kehidupan semua makhluk hidup. Air adalah salah satu senyawa yang paling banyak dan penting, yang terdiri dari molekul-molekul seperti oksigen dan nitrogen. Kualitas air adalah parameter kritis yang mempengaruhi kesehatan manusia, lingkungan, dan ekosistem secara keseluruhan.

## Business Understanding

Memahami pentingnya kualitas air sebagai aset vital bagi keberlanjutan dan kesehatan masyarakat, kami membuat sistem ini untuk pengelolaan kualitas air. Dengan menggabungkan teknologi pemantauan canggih dan analisis data yang mendalam, kami memberikan solusi tidak hanya meningkatkan kualitas air, tetapi juga memberikan dampak positif bagi lingkungan, dan mendukung pertumbuhan kepentingan pelanggan.

Bagian laporan ini mencakup:

### Problem Statements

- Klasifikasi kualitas air yang kurang layak dan kurang aman untuk diminum.

### Goals

- Mengembangkan dan mengoptimalkan sistem pemantauan kualitas air yang canggih, termasuk penggunaan teknologi sensor terkini dan integrasi data real-time untuk memastikan deteksi dini terhadap perubahan kualitas air.
- Mengetahui kualitas air yang layak dan aman diminum.

### Solution statements
- Pengembangan Platform pencarian Kualitas air Berbasis Web, solusi pertama adalah mengembangkan platform pencarian Kualitas air Berbasis Web yang mengintegrasikan data dari Kaggle.com untuk memberikan pengguna akses cepat dan mudah ke informasi tentang Kualitas air. Platform ini akan menyediakan antarmuka pengguna yang ramah. 
- Model yang dihasilkan dari dataset itu menggunakan metode Logistic Regression.

## Data Understanding
Dataset yang saya gunakan berasal dari Kaggle yang berisi kualitas air. Dataset ini mengandung 8000 baris dan 21 columns.<br> 

[Water Quality](https://www.kaggle.com/datasets/mssmartypants/water-quality/data).


### Variabel-variabel pada Water Quality adalah sebagai berikut:
- aluminium : Merupakan unsur kimia dalam tabel periodik dengan simbol Al[Tipe data: Float, berbahaya jika lebih besar dari 2.8]
- ammonia : Merupakan senyawa kimia yang didapati berupa gas dengan bau tajam yang khas[Tipe data: Float, berbahaya jika lebih besar dari 32.5]
- arsenic : Merupakan unsur kimia dengan simbol As[Tipe data: Float, berbahaya jika lebih besar dari 0.01]
- barium : Merupakan logam alkali tanah yang lembut dan bersifat reaktif dengan air dan udara. [Tipe data: Float, berbahaya jika lebih besar dari 2]
- cadmium : Merupakan logam transisi berwarna putih keperakan dengan sifat-sifat fisika yang mirip dengan zinc dan mercury[Tipe data: Float, berbahaya jika lebih besar dari 0.005]
- chloramine : Merupakan senyawa kimia yang terbentuk dari kombinasi amonia (NH₃) dengan klor (Cl₂) atau senyawa klorin (seperti hipoklorit)[Tipe data: Float, berbahaya jika lebih besar dari 4]
- chromium : Merupakan logam transisi yang keras & tahan korosi[Tipe data: Float, berbahaya jika lebih besar dari 0.1 ]
- copper : Merupakan logam transisi yang memiliki konduktivitas listrik dan termal yang sangat baik[Tipe data: Float, berbahaya jika lebih besar darin 1.3 ]
- flouride : Merupakan ion yang terbentuk dari unsur fluorin[Tipe data: Float, berbahaya jika lebih besar dari 1.5]
- bacteria : Merupakan mikroorganisme uniseluler yang merupakan bentuk kehidupan yang sangat kecil dan sederhana[Tipe data: Float, berbahaya jika lebih besar dari 0]
- viruses : Merupakan bentuk mikroorganisme yang sangat kecil, tidak memiliki sel, dan memerlukan inang hidup untuk mereproduksi dan berkembang[Tipe data: Float, berbahaya jika lebih besar dari 0]
- lead : Merupakan logam berat yang berwarna abu-abu kebiruan dan dikenal karena sifatnya yang beracun[Tipe data: Float, berbahaya jika lebih besar dari 0.015]
- nitrates : Merupakan senyawa kimia yang terdiri dari nitrogen (N), oksigen (O), dan atom unsur lain[Tipe data: Float, berbahaya jika lebih besar dari 10]
- nitrites : Merupakan senyawa kimia yang mengandung ion nitrit (NO₂⁻)[Tipe data: Float, berbahaya jika lebih besar dari 1]
- mercury : Merupakan unsur kimia yang terletak di grup 12 (IIB) dalam tabel periodik   [Tipe data: Float, berbahaya jika lebih besar dari 0.002]
- perchlorate : Merupakan ion yang terdiri dari satu atom klor (Cl) dan empat atom oksigen (O)[Tipe data: Float, berbahaya jika lebih besar dari 56]
- radium : Merupakan logam alkali tanah yang bersifat radioaktif[Tipe data: Float, berbahaya jika lebih besar dari 5]
- selenium : Merupakan unsur kimia yang terletak di grup 16 (VIA) dalam tabel periodik[Tipe data: Float, berbahaya jika lebih besar dari 0.5]
- silver : Merupakan unsur kimia yang terletak di grup 11 (IB) dalam tabel periodik[Tipe data: Float, berbahaya jika lebih besar dari 0.1]
- uranium : Merupakan logam berat yang terdapat secara alamiah dan bersifat radioaktif[Tipe data: Float, berbahaya jika lebih besar dari 0.3]
- is_safe : class attribute {0 - not safe, 1 - safe}

## Data Preparation
### Data Collection
Dalam data collection ini, saya mendapatkan dataset yang nantinya digunakan dari website kaggle dengan nama dataset Water Quality. Dataset bisa di download pada link diatas.

### Data Discovery And Profiling
Untuk bagian ini, saya akan menggunakan teknik EDA. <br>
Pertama kita mengimport semua library yang dibutuhkan, 
``` bash
import pandas as pd
import numpy as np
import matplotlib.pypot as plt
import seaborn as sns
```

Karena kita menggunakan google colab untuk mengerjakannya maka kita akan import files juga,
``` bash
from google.colab import files
```

Lalu mengupload token kaggle agar nanti bisa mendownload sebuah datasets dari kaggle melalui google colab
``` bash
file.upload()
```
Setelah mengupload filenya, maka akan lanjut dengan membuat sebuah folder untuk menyimpan file kaggle.json yang sudah diupload tadi, 
``` bash
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle
```
Lalu mari kita download datasets nya, 
``` bash
!kaggle datasets download -d mssmartypants/water-quality
```
Selanjutnya kita harus extract file yang tadi telah didownload
``` bash
!mkdir water-quality
!unzip water-quality.zip -d water-quality
!ls water-quality
```
Lanjut dengan memasukkan file csv yang telah diextract pada sebuah variable,
``` bash
df = pd.read_csv('water-quality/waterQuality1.csv')
df = df.dropna()
df.sample()
```
Untuk melihat mengenai type data dari masing masing kolom kita bisa menggunakan property info,
``` bash
df.info()
```
untuk memisahkan numeric dengan kategori
``` bash
numerical = []
objcols = []

for col in df.columns:
    if df[col].dtype=="float64":
        numerical.append(col)
    else:
        objcols.append(col)
for col in df.columns:
    if col in numerical:
        df[col].fillna(df[col].median(),inplace=True)
    else:
        df[col].fillna(df[col].mode()[0],inplace=True)
```
untuk melakukan transformasi data
``` bash
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for col in objcols:
    df[col] = le.fit_transform(df[col])

df['is_safe'] = le.fit_transform(df['is_safe']
```
Selanjutnya data exploration 
``` bash
plt.figure(figsize=(10,5))
sns.heatmap(confusion_matrix(logreg.predict(x_test),y_test), annot = True,fmt='.1f')
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.title("Confusion Matrix")
plt.tight_layout()
```
![image](https://github.com/arumr/klasifikasi-kelayakan-air/assets/137166475/019c38ef-afb6-49a0-bfa6-cb3bc669c2e1)


## Modeling
sebelumnya mari kita import library yang nanti akan digunakan,
``` bash
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
```
selanjutnya membagi data training dan testing
``` bash
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=1)
```

## Evaluation
Disini saya menggunakan xgboost sebagai metrik evaluasi.
- xgboost adalah implementasi pohon keputusan yang ditingkatkan gradien yang dirancang untuk kecepatan dan kinerja yang mendominasi pembelajaran mesin kompetitif.

``` bash 
from xgboost import XGBClassifier
import xgboost as xgb

xgb = XGBClassifier(missing = 190 , max_depth  = 5 ,  n_estimators  = 6 , learning_rate = 0.4)

xgb.fit(x_train , y_train)

acc = (xgb.score(x_train , y_train)*100)
print(f'The accuracy of the Train Model is {acc:.2f}')

acc =(xgb.score(x_test , y_test)*100)
print(f'The accuracy of the Test Model is {acc:.2f}')
```
Hasil di dapatkan adalah 90%

## Deployment

[Klasifikasi Kelayakan Air Minum](https://klasifikasi-kelayakan-air.streamlit.app/). 
