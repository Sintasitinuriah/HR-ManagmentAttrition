# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis
Tingginya attrition rate berdampak langsung pada meningkatnya biaya rekrutmen dan pelatihan, serta hilangnya pengetahuan dan produktivitas. Oleh karena itu, tim HR memiliki beberapa tujuan utama:
- Menurunkan tingkat attrition yang tinggi.
- Memahami penyebab utama karyawan resign, agar dapat dilakukan intervensi yang tepat sasaran.
- Memonitor risiko attrition secara berkala melalui dashboard interaktif.

### Cakupan Proyek
Proyek ini akan berfokus pada analisis sejumlah faktor yang diduga berkontribusi terhadap keputusan karyawan untuk keluar dari perusahaan. Faktor-faktor tersebut mencakup aspek keterlibatan kerja, intensitas perjalanan dinas, jenis jabatan tertentu, status pernikahan, serta kebiasaan lembur. Analisis akan membantu mengidentifikasi kelompok karyawan yang paling berisiko resign dan memberikan pemahaman yang lebih dalam mengenai kondisi-kondisi kerja yang dapat mendorong terjadinya attrition. Diperjelas dengan pembuatan dashboard interaktif.


### Persiapan
| Jenis      | Keterangan                                                                 |
|------------|------------------------------------------------------------------------------|
| Title      | Jaya Jaya Maju                                                   |
| Source     | [github](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/) |
| Visibility | Public                                                                      |

Setup environment:

```bash
# Clone repository
git clone https://github.com/Sintasitinuriah/HR-ManagmentAttrition.git
cd HR-ManagementAttrition

# Buat file file.yaml yang sesuai dengan konfigurasi folder ini

# Jalankan Metabase dan PostgreSQL dengan Docker Compose
docker-compose up -d

# Hentikan kontainer jika selesai
docker-compose down

```

## Business Dashboard
[Lihat PDF Laporan](./hr-project-dashboard.pdf)

Untuk mempermudah pemantauan dan analisis risiko attrition secara berkala, telah dibuat sebuah dashboard interaktif menggunakan Metabase. Dashboard ini menyajikan visualisasi data yang intuitif dan informatif mengenai faktor-faktor yang mempengaruhi attrition, seperti:

- Distribusi attrition berdasarkan jabatan (Job Role), Gender, rata-rata income dan frekuensi lembur (Overtime).
- Top 5 Karyawan berpotensi keluar sesuai JobRole berdasarkan Attrition_Probablity. 
- Segmentasi karyawan berdasarkan tingkat risiko attrition.

Dashboard ini dapat diakses melalui tautan berikut (hanya dapat diakses di lingkungan lokal proyek):

[Link Dashboard – Visualisasi Attrition](http://localhost:3000/public/dashboard/fdbc614a-8b6f-4d53-a5e8-084b485d1c12?tab=4-visualisasi-attrition)

Dashboard ini menjadi alat penting bagi tim HR dalam merancang intervensi yang lebih proaktif dan berbasis data untuk mengurangi tingkat attrition di Jaya Jaya Maju.

## Conclusion
Berdasarkan analisis terhadap data karyawan Jaya Jaya Maju, ditemukan bahwa tingkat attrition yang tinggi (lebih dari 10%) disebabkan oleh sejumlah faktor internal yang dapat diidentifikasi dan ditindaklanjuti. Faktor-faktor yang paling berpengaruh terhadap keputusan karyawan untuk resign antara lain adalah frekuensi lembur, jenis jabatan tertentu, serta tingkat keterlibatan kerja.

Dari hasil analisis, mayoritas karyawan yang meninggalkan perusahaan berasal dari posisi-posisi seperti Sales Executive, Research Scientist, dan Laboratory Technician, yang juga cenderung memiliki tingkat beban kerja dan lembur lebih tinggi. Selain itu, karyawan yang sering melakukan perjalanan dinas dan memiliki jam kerja yang berlebihan menunjukkan risiko resign yang lebih tinggi dibandingkan kelompok lainnya.

Dashboard interaktif yang telah dikembangkan memungkinkan tim HR untuk memonitor kondisi ini secara real-time dan melakukan deteksi dini terhadap karyawan yang berisiko tinggi untuk keluar. Hal ini akan sangat membantu dalam merancang strategi retensi yang lebih tepat sasaran dan efisien.

Secara keseluruhan, proyek ini berhasil memberikan wawasan yang kuat mengenai penyebab utama attrition di perusahaan serta menyediakan alat bantu visualisasi data untuk pengambilan keputusan yang lebih baik ke depannya.

### Rekomendasi Action Items (Optional)
 Beberapa rekomendasi item yang bisa diterapkan oleh perusahaan Jaya Jaya Maju:
 1. Sebanyak 65% karyawan yang sering resign adalah overtime, maka dari itu perusahaan bisa melakukan evaluasi beban kerja dan distribusi jam lembur
 2. Potensi prediksi attrition dibagian JobRole tertinggi adalah Sales Executive, Research Scientist, dan Laboratory Technician, bisa  diakukan survei kepuasan kerja internal atau evaluasi kepemiminan di depatremen tersebut.
 3. Evaluasi faktor Program Keseimbangan Kerja dan Kehidupan (Work-Life Balance): Mengingat tingginya tingkat lembur berhubungan erat dengan attrition, perusahaan bisa menginisiasi program kerja fleksibel, cuti tambahan, atau kebijakan remote working terbatas untuk jabatan tertentu.