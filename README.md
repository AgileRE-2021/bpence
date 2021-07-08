
Bpence (styled: bpence) adalah sebuah sistem yang mengonversi Sequence Diagram menjadi Business Process Modeling Notation (BPMN). Proyek ini dikembangkan oleh Kelompok 1 kelas I1 mata kuliah Pembangunan Perangkat Lunak (Praktikum).

Anggota kelompok:<br />
Rafikaputri Dwi 081811633012<br />
Zidan Nur Karim 081811633020<br />
Ais Triamirza F.A 081811633025<br />
Abdullah M. Al Kamal 081811633030<br />
Fadya Salsa N. 081811633032<br />
Afiyah Mabruzah Aziz 081811633044<br />
Tania R. Natalnael 081811633051<br />
Rani Permata Sari 081811633062<br />
<br />
-----
<br />
Cara menginstall:<br />
A. Basis Data<br />
   1. Jalankan MySQL dan Apache via XAMPP.<br />
   2. Buat sebuah basis data bernama 'bpence'.<br />
<br />
B. Integrasi Basis Data dengan Situs<br />
   1. Unduh repository ini ke perangkat keras Anda.<br />
   2. Buka terminal dari direktori repo lokal.<br />
   3. Migrasikan dengan python manage.py makemigrations.<br />
   4. Dilanjutkan dengan python manage.py migrate.<br />
   5. Integrasi berhasil dilakukan.<br />
<br />
C. Mengakses Situs <br />
   1. Menjalankan server dengan python manage.py runserver via terminal.<br />
   2. Buka browser Anda dan akses localhost:8000.<br />
   3. Situs berhasil diakses. <br />

Cara menggunakan:<br/>
1. Klik tombol "Mulai konversi". <br/>
2. Tempelkan kode PlantUML berformatkan sequence diagram di textarea yang tersedia.<br/>
   Sesudahnya, klik tombol "Submit".
3. Hasil konversi akan muncul. Anda dapat menyimpan diagram dalam format SVG maupun PNG<br/>
   dengan mengklik tombol yang tersedia.