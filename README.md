<h1 align="center">  Pejantara: AI-Classification Waste Management System </h1>

<p align="center"> 🌍 Transforming Batam's Waste Management with AI 🌍 </p> 

<div align="center">
    <!-- Your badges here -->
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
    <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">
    <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white">
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white">
    <img src="https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white">
    <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white">
</div>

## Teams

- Lalu Kevin Alejandro (Design Researcher)
- Estu Bekti Cahyana (Data Engineer)
- Ekky Dimas Krismanto (Machine Learning Engineer)
- Ahmad Khusna Faizuddin (Machine Learning Engineer)
- Arief Indra Kusuma (Machine Learning Ops)

## Idea Background

### 1. Theme
Sustainable Development: Waste Management in Urban Areas
Proyek ini bertujuan untuk menciptakan sistem manajemen sampah berbasis AI yang dapat mengidentifikasi, mengklasifikasi, dan menganalisis pola pengelolaan sampah di kota Batam.

### 2. Problem
Batam menghadapi tantangan besar dalam pengelolaan sampah, mulai dari kurangnya prediksi kebutuhan pengangkutan sampah hingga kesalahan dalam pengklasifikasian sampah yang mengurangi potensi daur ulang.

### 3. Solution
Solusi yang ditawarkan:
Mengembangkan sistem berbasis Machine Learning yang dapat:

1. Mengklasifikasikan jenis sampah berdasarkan gambar.
2. Memberikan rekomendasi optimal untuk pengelolaan dan daur ulang.

## Dataset and Algorithm

### 1. Dataset
- Data Collection <br />
Kami menggunakan dataset yang bersumber dari Kaggle dan Github.
- Data Splitting <br />
Kami membagi data menjadi 3 bagian, yaitu : train, validation, test. Dengan perbandingan (70%:15%:15%)
dengan klasifikasi saat ini dibagi menjadi 4 bagian, yaitu : Organik, Anorganik, B3, Elektronik
- Data Cleaning <br />
Kami memastikan bahwa semua gambar sesuai dengan klasifikasinya

### 2. Algorithm [Convolutional Neural Network (CNN)]
- Framework <br />
Kami menggunakan TensorFlow, Keras, Pandas, Numpy.

- Pembangunan Model <br />
Masukkan kode training dan juga spesifikasi model, seperti epoch, learning rate, batch size, dan lain sebagainya.

- Model Evaluation <br />
Masukkan metrik evaluasi model seperti accuracy, precision, recall, F1-score, dan lain - lain.

## Prototype
Mobile App untuk Klasifikasi Sampah:

- Aplikasi ini memanfaatkan model CNN untuk mengklasifikasikan jenis sampah secara real-time melalui kamera ponsel.
Memberikan rekomendasi langkah daur ulang kepada pengguna.

Coming Soon: Chatbot:

- Chatbot berbasis AI untuk integrasi di platform web.
Memberikan informasi tentang klasifikasi sampah dan rekomendasi daur ulang secara otomatis (konsep sementara ini)

## Integration
Sistem ini terintegrasi dengan:
Backend: Flask REST API untuk menyimpan data klasifikasi dan mengelola pengolahan sampah.

## Deployment
- Platform: Docker digunakan untuk containerisasi sistem agar lebih portabel.
- Cloud Hosting: Backend dan model CNN di-deploy di IBM Cloud


## Result
Disesuaikan dengan kebutuhan atau bisa ditiru dari laporan dokumentasi massive.

## Conclusion
Proyek Pejantara sukses menciptakan sistem AI yang inovatif untuk manajemen sampah. Dengan klasifikasi berbasis CNN melalui aplikasi mobile dan rencana pengembangan chatbot berbasis web, kami yakin solusi ini akan menjadi langkah besar dalam mendukung pengelolaan sampah yang lebih efisien dan berkelanjutan.
