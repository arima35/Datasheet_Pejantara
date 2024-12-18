---

# <h2 align="center">♻️ Waste Management AI with team Web & Mobile Project ♻️</h2>

<p align="center">
🚀 Kolaborasi tim AI dengan tim Web dan Mobile untuk solusi inovatif terkait pengelolaan sampah 🚀
</p>


<div align="center">
    <!-- Teknologi AI -->
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">
    <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white">
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
    <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
    <img src="https://img.shields.io/badge/IBM%20Cloud-%231C1E26.svg?style=for-the-badge&logo=ibm&logoColor=white">
</div>
<div align="center">
    <!-- Teknologi Mobile -->
    <img src="https://img.shields.io/badge/Android%20Studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white">
    <img src="https://img.shields.io/badge/kotlin-%230095D5.svg?style=for-the-badge&logo=kotlin&logoColor=white">
    <img src="https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black">
</div>
<div align="center">
    <!-- Teknologi Web -->
    <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB">
    <img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
    <img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white">
    <img src="https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB">
    <img src="https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white">
</div>

---

## 🧑‍💻 **Teams**

| **Nama**                     | **Peran**                        |
|-----------------------------|----------------------------------|
| Lalu Kevin Alejandro        | Design Researcher               |
| Estu Bekti Cahyana          | Data Engineer                   |
| Ekky Dimas Krismanto        | Machine Learning Engineer       |
| Achmad Khusna Faizuddin     | Machine Learning Engineer       |
| Arief Indra Kusuma          | Machine Learning Ops            |

---

## 🌱 **Idea Background**

### 🌍 **Tema: Waste Management & Environment**

### ❗ **Permasalahan**  
Prediksi pengelolaan sampah saat ini belum optimal. Banyaknya data sampah yang tidak terstruktur dan kurangnya edukasi masyarakat menyebabkan perencanaan pengelolaan sampah tidak efektif.

### 💡 **Solusi**  
Kami mengembangkan sistem berbasis AI dan Web/Mobile:  
1. **Klasifikasi Sampah** menggunakan **Machine Learning (R-CNN)** untuk mengenali jenis sampah dari gambar.  
2. **Chatbot Edukatif** berbasis **Flask** untuk memberikan solusi dan edukasi terkait sampah berdasarkan dataset JSON.  
3. **Integrasi Web dan Mobile** agar pengguna dapat dengan mudah menggunakan sistem ini untuk edukasi, monitoring, dan klasifikasi.

---

## 📊 **Dataset**

Kami menggunakan 2 sumber dataset dari **Kaggle**:  
1. [Garbage Dataset (12 Classes)](https://www.kaggle.com/datasets/carloshcarneiro/garbage-v4-12-classes)  
2. [Real Waste Dataset](https://www.kaggle.com/datasets/joebeachcapital/realwaste)

**Langkah-langkah pengolahan data**:
1. **Data Collection**: Mengumpulkan dataset yang relevan.  
2. **Data Cleaning**: Menghapus duplikasi data, menangani missing values, dan mempersiapkan gambar/data JSON.  
3. **Data Augmentation** *(jika diperlukan)*: Untuk menyeimbangkan kelas sampah.

---

## 🧠 **Model & Algorithm**

### **1. Model Klasifikasi Sampah**  
- **Algoritma**: R-CNN (Region-based Convolutional Neural Network)  
- **Framework**: TensorFlow & Keras  
- **Spesifikasi Model**:  
    - Epochs: 50  
    - Batch Size: 32  
    - Learning Rate: 0.001  
- **Evaluasi Model**: Menggunakan **Accuracy**, **Precision**, dan **Recall**.  

### **2. Chatbot Flask**  
- **Dataset**: JSON berisi intents dan responses edukatif.  
- **Algoritma**: Cosine Similarity menggunakan **TF-IDF** dari `scikit-learn`.  
- **Kode Utama**:  
   Flask-based chatbot server dapat dilihat di file `app.py`.

---

## 🎨 **Prototype**

### Fitur Utama 🚀
- 🌟 Teknologi AI untuk klasifikasi sampah otomatis.
- 🌟 Chatbot interaktif berbasis Flask.  
- 📱 Aplikasi mobile menggunakan **Android Studio & Kotlin**.  
- 💻 Web dashboard dengan **React & Tailwind CSS**.  
- 🤝 Kolaborasi bersama stakeholder **Pejantara**.

---

## 🔄 **Integration**

1. **Tim AI**:  
   - Mengembangkan model klasifikasi menggunakan **TensorFlow/Keras**.  
   - Chatbot edukasi dengan **Flask** API.  

2. **Tim Web**:  
   - Mengintegrasikan Flask chatbot API ke dalam UI/UX berbasis **React**.  

3. **Tim Mobile**:  
   - Menggunakan API klasifikasi sampah untuk upload gambar langsung dari aplikasi mobile.  

---

## 🚀 **Deployment**

1. **Containerization**:  
- Sistem di-deploy menggunakan **Docker** untuk memastikan aplikasi dapat berjalan konsisten di berbagai lingkungan (development, testing, production).
- Docker memungkinkan pengemasan aplikasi beserta dependensinya dalam satu kontainer, memudahkan tim dalam manajemen versi dan skalabilitas.
2. **Cloud Deployment**:  
- **IBM Cloud Code Engine** digunakan untuk hosting aplikasi dan API. Code Engine memfasilitasi deployment aplikasi berbasis kontainer tanpa perlu mengelola infrastruktur server secara langsung. 
- Layanan ini memungkinkan sistem untuk menskalakan aplikasi secara otomatis sesuai dengan kebutuhan trafik dan memastikan kinerja yang optimal tanpa overprovisioning.
---

## 📈 **Result**

**Hasil sementara**:  
- Model klasifikasi mencapai akurasi hingga **85%** pada validasi dataset.  
- Chatbot berhasil memberikan respon edukatif dengan relevansi tinggi berdasarkan threshold cosine similarity.  

(📝 **Catatan**: Hasil ini masih dapat diimprovisasi seiring evaluasi lebih lanjut.)

---

## 🏁 **Conclusion**

Dengan penggabungan teknologi AI dan platform web/mobile, proyek ini bertujuan:  
1. Memberikan **solusi pengelolaan sampah** yang efektif berbasis teknologi.  
2. Mendorong **edukasi masyarakat** untuk lebih peduli terhadap lingkungan.  
3. Menunjukkan potensi kolaborasi antara tim AI dan tim pengembang aplikasi dalam menciptakan solusi **berkelanjutan**.

--- 

### 🛠️ **Getting Started**  

Ikuti langkah-langkah berikut untuk menjalankan project ini di lokal:  

### 🗂 **Folder 1: Klasifikasi (Image Classification)**  

#### **1. Menjalankan Server Flask**  
- Arahkan terminal ke folder `klasifikasi` dulu.  
   ```bash
   cd klasifikasi
   python app.py
   ```
- Server biasanya jalan di **http://localhost:5000**.  

#### **2. Endpoint Klasifikasi Gambar**  
| **Method** | **Endpoint**         | **Deskripsi**                         |
|------------|----------------------|---------------------------------------|
| POST       | `/classify`           | Menerima gambar untuk klasifikasi.    |

#### **3. Pengaturan di Postman**  
1. **Buat Request Baru** → Pilih **POST**.  
2. **URL**:  
   ```
   http://localhost:5000/classify
   ```
3. **Body Request**:  
   - Pilih tab **Body** → Klik **form-data**.  
   - Tambahkan **Key** dengan tipe **File**:  
     ```
     Key: file
     Value: <pilih file gambar sampah>
     ```
4. **Send Request** → Cek respons Flask:  
   ```json
   {
       "confidence": 0.95
       "class": "Plastik",
   }
   ```
5. **Validasi Respons**:  
   - **Confidence** menunjukkan akurasi model.
   - Pastikan **class** sesuai jenis sampah (Plastik, Kertas, dll).  

---

### 🗂 **Folder 2: Chatbot (Text-Based Chatbot)**  

#### **1. Menjalankan Server Flask**  
- Arahkan terminal ke folder `chatbot`:  
   ```bash
   cd chatbot
   python app.py
   ```
- Server Flask jalan di **http://localhost:5000**.  

#### **2. Endpoint Chatbot**  
| **Method** | **Endpoint**         | **Deskripsi**                     |
|------------|----------------------|-----------------------------------|
| POST       | `/chat`              | Menerima input teks dari user.    |

#### **3. Pengaturan di Postman**  
1. **Buat Request Baru** → Pilih **POST**.  
2. **URL**:  
   ```
   http://localhost:5000/chat
   ```
3. **Body Request**:  
   - Pilih tab **Body** → Klik **raw** → Pilih format **JSON**.  
   - Masukkan payload seperti ini:  
     ```json
     {
         "message": "Bagaimana cara membuang sampah plastik?"
     }
     ```
4. **Send Request** → Cek respons Flask:  
   ```json
   {
       "response": "Buanglah sampah plastik di tempat sampah anorganik."
   }
   ```
5. **Validasi Respons**:  
   - Respons teks harus relevan dengan input dari user.  
   - Perhatikan format JSON.

---

## 🤝 **Kolaborasi & Kontribusi**

Kami membuka kolaborasi lebih lanjut untuk improvisasi proyek ini. Jika tertarik, silakan buka **issue** atau **pull request**! 🚀

--- 

✨ **_Bersama kita wujudkan lingkungan yang lebih bersih dan berkelanjutan!_** 🌍

---
