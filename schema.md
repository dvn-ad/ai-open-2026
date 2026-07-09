# Import
## BC 2.0 - Schema
```json
{

 "$schema": "http://json-schema.org/draft-07/schema",

 "type": "object",

 "title": "Schema Kirim Dokumen BC 20",

 "description": "JSON Schema untuk Kirim Dokumen Pabean v.0.5.7.23. Terdiri atas data header dan data barang. Data header merupakan data umum dokumen pabean sedangkan data barang merupakan data detil atas barang pada dokumen pabean",

 "properties": {

  "asalData": {

   "type": "string",

   "description": "set value [S]",

   "enum": [

    "S",

    "SQ"

   ],

   "message": "Asal pengiriman data secara Host to Host: S"

  },

  "asuransi": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.24 Asuransi LN/DN",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai asuransi maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "bruto": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.29 Berat Kotor (kg)",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Nilai bruto maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "cif": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.26 Nilai Pabean",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai cif maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "disclaimer": {

   "type": "string",

   "description": "Persetujuan pengguna dalam kirim dokumen pabean: [1] Ya atau [0] Tidak",

   "enum": [

    "0",

    "1"

   ],

   "message": "Persetujuan pengguna dalam kirim dokumen pabean: 1 untuk Ya atau 0 untuk Tidak"

  },

  "kodeJenisProsedur": {

   "type": "string",

   "description": "Lihat Referensi Jenis Prosedur",

   "message": "Format kode sesuai Referensi Jenis Prosedur"

  },

  "kodeJenisImpor": {

   "type": "string",

   "description": "Lihat Referensi Jenis Impor",

   "message": "Format kode sesuai Referensi Jenis Impor"

  },

  "kodeJenisEkspor": {

   "type": "string",

   "description": "Lihat Referensi Jenis Ekspor",

   "message": "Format kode sesuai Referensi Jenis Ekspor"

  },

  "flagVd": {

   "type": "string",

   "description": "flag Voluntary declaration: [Y] Ya atau [T] Tidak",

   "enum": [

    "Y",

    "T"

   ],

   "message": "flag Voluntary declaration: Y untuk Ya atau T untuk Tidak"

  },

  "fob": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.23 Nilai",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai fob maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "freight": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.25 Freight",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai freight maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "hargaPenyerahan": {

   "type": "number",

   "description": "Nilai Harga Penyerahan",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Nilai harga penyerahan maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "idPengguna": {

   "type": "string",

   "description": "Identitas pengguna",

   "message": "Identitas pengguna"

  },

  "jabatanTtd": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - F Jabatan pengguna yang mengajukan dokumen impor",

   "message": "Jabatan pengguna yang mengajukan dokumen impor"

  },

  "jumlahKontainer": {

   "type": "integer",

   "description": "jumlah peti kemas yang digunakan untuk mengangkut barang",

   "message": "Jumlah kontainer atau peti kemas"

  },

  "jumlahTandaPengaman": {

   "type": "integer",

   "description": "Jumlah Tanda Pengaman FTZ 03",

   "message": "Jumlah tanda pengaman pada FTZ 03"

  },

  "kodeAsuransi": {

   "type": "string",

   "description": "kode asuransi yang dibayar di [LN] luar negeri atau [DN] dalam negeri",

   "enum": [

    "LN",

    "DN"

   ],

   "message": "Kode asuransi yang dibayar: LN untuk luar negeri atau DN untuk dalam negeri"

  },

  "kodeCaraBayar": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - C. Cara Pembayaran. Lihat Referensi Cara Bayar",

   "message": "Format kode sesuai Referensi Cara Bayar"

  },

  "kodeDokumen": {

   "type": "string",

   "description": "set value [20]",

   "const": "20",

   "message": "Format kode sesuai Referensi Dokumen Impor BC 2.0: 20"

  },

  "kodeIncoterm": {

   "type": "string",

   "description": "Lihat Referensi Incoterm",

   "message": "Format kode sesuai Referensi Incoterm"

  },

  "kodeJenisNilai": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.16 Transaksi. Lihat Referensi Jenis Transaksi Perdagangan",

   "message": "Format kode sesuai Referensi Jenis Transaksi Perdagangan"

  },

  "kodeKantor": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - Kantor Pabean. Lihat Referensi Kantor",

   "message": "Format kode sesuai Referensi Kantor"

  },

  "kodePelMuat": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.12 Pelabuhan Muat. Lihat Referensi Pelabuhan",

   "message": "Format kode pelabuhan muat sesuai Referensi Pelabuhan"

  },

  "kodePelTujuan": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.14 Pelabuhan Tujuan. Lihat Referensi Pelabuhan",

   "message": "Format kode pelabuhan tujuan sesuai Referensi Pelabuhan"

  },

  "kodeTps": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.20 Tempat Penimbunan. Kode tps sesuai dengan yang dibuat oleh Kantor Pabean masing-masing",

   "message": "Format kode tps sesuai dengan yang dibuat oleh Kantor Pabean masing-masing "

  },

  "kodeTutupPu": {

   "type": "string",

   "description": "Referensi TutupPu: [11] BC 1.1, [12] BC 1.2, [14] BC 1.4",

   "enum": [

    "11",

    "12",

    "14"

   ],

   "message": "Format kode sesuai Referensi TutupPu"

  },

  "kodeValuta": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.21 Valuta. Lihat Referensi Valuta",

   "message": "Format kode sesuai Referensi Valuta"

  },

  "kotaTtd": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - F Kota tempat pengguna membuat dokumen impor",

   "message": "Kota tempat pengguna membuat dokumen impor"

  },

  "namaTtd": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - F Nama pengguna yang membuat dokumen impor",

   "message": "Nama pengguna yang membuat dokumen impor"

  },

  "ndpbm": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.22 NDPBM",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Ndpbm maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "netto": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 2.0 - D.30 Berat Bersih (Kg)",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Nilai netto/berat bersih maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "nilaiBarang": {

   "type": "number",

   "description": "nilai barang impor dalam mata uang sesuai kode valuta yang dimasukkan",

   "maxlength": 38,

   "multipleOf": 0.01,

   "message": "Nilai barang maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "nilaiIncoterm": {

   "type": "number",

   "description": "nilai barang impor sesuai kode incoterm yang dimasukkan",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai incoterm maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "nilaiMaklon": {

   "type": "number",

   "description": "nilai jasa subkon",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai maklon maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "nomorAju": {

   "type": "string",

   "description": "nomor pengajuan dokumen pabean 26 digit dengan format 4 digit kode kantor, 2 digit kode dokumen pabean, 6 digit unik perusahaan, 8 digit tanggal pengajuan dengan format YYYYMMDD, 6 digit sequence/nomor urut pengajuan dokumen pabean",

   "pattern": "^[A-Za-z0-9]{26}$",

   "message": "Sesuaikan format nomor pengajuan dokumen impor terdiri 26 digit: 4 digit kode kantor, 2 digit kode dokumen pabean, 6 digit unik perusahaan, 8 digit tanggal pengajuan dengan format YYYYMMDD, 6 digit sequence/nomor urut pengajuan dokumen impor"

  },

  "nomorBc11": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.18 BC 1.1",

   "message": "Nomor BC 1.1 terdiri dari 6 digit"

  },

  "posBc11": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.18 BC 1.1",

   "message": "Pos BC 1.1 terdiri dari 4 digit"

  },

  "seri": {

   "type": "integer",

   "description": "seri dokumen impor",

   "message": "seri dokumen impor"

  },

  "subposBc11": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 2.0 - D.18 BC 1.1",

   "message": "Pos BC 1.1 terdiri dari 8 digit"

  },

  "tanggalAju": {

   "type": "string",

   "format": "date",

   "description": "tanggal pengajuan dokumen impor dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal pengajuan dokumen: YYYY-MM-DD"

  },

  "tanggalBc11": {

   "type": "string",

   "format": "date",

   "description": "Sesuai kolom formulir BC 2.0 - D.18 Tanggal BC 1.1 dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal BC 1.1: YYYY-MM-DD"

  },

  "tanggalTiba": {

   "type": "string",

   "format": "date",

   "description": "Sesuai kolom formulir BC 2.0 - D.11 Perkiraan Tanggal Tiba dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal perkiraan tiba: YYYY-MM-DD"

  },

  "tanggalTtd": {

   "type": "string",

   "format": "date",

   "description": "Sesuai kolom formulir BC 2.0 - F Tanggal penandatanganan dokumen pabean dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal penandatanganan dokumen: YYYY-MM-DD"

  },

  "totalDanaSawit": {

   "type": "number",

   "description": "total dana sawit",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Total dana sawit maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "volume": {

   "type": "number",

   "description": "total volume",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Total volume maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "vd": {

   "type": "number",

   "description": "Total nilai voluntary declaration",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Total nilai barang voluntary declaration maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "biayaTambahan": {

   "type": "number",

   "description": "biaya tambahan yang dikenakan",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Biaya tambahan maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "biayaPengurang": {

   "type": "number",

   "description": "biaya pengurang yang dikenakan",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Biaya pengurang maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "barang": {

   "type": "array",

   "items": {

     "type": "object",

     "description": "detil data barang dalam satu pengajuan dokumen impor",

     "properties": {

      "asuransi": {

       "type": "number",

       "description": "nilai asuransi"

      },

      "bruto": {

       "type": "number",

       "maxlength": 24,

       "multipleOf": 0.0001,

       "description": "berat kotor/bruto dalam kilogram"

      },

      "cif": {

       "type": "number",

       "description": "harga cif"

      },

      "cifRupiah": {

       "type": "number",

       "description": "harga cif rupiah"

      },

      "diskon": {

       "type": "number",

       "description": "diskon"

      },

      "fob": {

       "type": "number",

       "description": "free on board"

      },

      "freight": {

       "type": "number",

       "description": "freight"

      },

      "hargaEkspor": {

       "type": "number",

       "description": "harga ekspor"

      },

      "hargaPatokan": {

       "type": "number",

       "description": "harga patokan barang"

      },

      "hargaPenyerahan": {

       "type": "number",

       "description": "harga penyerahan barang"

      },

      "hargaPerolehan": {

       "type": "number",

       "description": "harga perolehan barang"

      },

      "hargaSatuan": {

       "type": "number",

       "description": "harga satuan barang"

      },

      "hjeCukai": {

       "type": "number",

       "description": "harga jual eceran"

      },

      "isiPerKemasan": {

       "type": "number",

       "description": "isi per kemasan",

       "multipleOf": 0.01

      },

      "jumlahBahanBaku": {

       "type": "integer",

       "description": "jumlah bahan baku"

      },

      "jumlahDilekatkan": {

       "type": "integer",

       "description": "jumlah yang dilekatkan"

      },

      "jumlahKemasan": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 2.0 - D.35 Jumlah Kemasan",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "jumlahPitaCukai": {

       "type": "integer",

       "description": "jumlah pita cukai"

      },

      "jumlahRealisasi": {

       "type": "number",

       "description": "jumlah realisasi"

      },

      "jumlahSatuan": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 2.0 - D.35 Jumlah Satuan Barang",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "kapasitasSilinder": {

       "type": "integer",

       "description": "kapasitas silinder"

      },

      "kodeJenisKemasan": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.35 Jenis Kemasan. Lihat Referensi Jenis Kemasan"

      },

      "kodeKondisiBarang": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.32 Spesifikasi Wajib. Referensi Kondisi Barang: [1] Baik, [2] Baru, [3] Bekas, [4] Segar, [5] Beku, [6] Baik/Baru, [7] Baik/Baru, [8] Baik/Bekas",

       "enum": [

        "1",

        "2",

        "3",

        "4",

        "5",

        "6",

        "7",

        "8"

       ]

      },

      "kodeNegaraAsal": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.32 Negara Asal Barang. Lihat Referensi Negara",

       "pattern": "^[A-Z]{2}$"

      },

      "kodeSatuanBarang": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.35 Jenis Satuan Barang. Lihat Referensi Satuan Barang"

      },

      "kodeBarang": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.34 Kode barang"

      },

      "merk": {

       "type": "string",

        "minLength": 2,

       "description": "Sesuai kolom formulir BC 2.0 - D.32 Merek Barang"

      },

      "ndpbm": {

       "type": "number",

       "description": "nilai dasar penghitungan bea masuk"

      },

      "netto": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 2.0 - D.35 Berat Bersih (kg)",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "nilaiBarang": {

       "type": "number",

       "description": "nilai barang"

      },

      "nilaiDanaSawit": {

       "type": "number",

       "description": "nilai dana sawit"

      },

      "nilaiDevisa": {

       "type": "number",

       "description": "nilai devisa"

      },

      "nilaiTambah": {

       "type": "number",

       "description": "nilai tambah"

      },

      "pernyataanLartas": {

       "type": "string",

       "description": "pernyataan barang lartas: [Y] Ya atau [T] Tidak",

       "enum": [

        "Y",

        "T"

       ]

      },

      "persentaseImpor": {

       "type": "number",

       "description": "persentase impor"

      },

      "posTarif": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.32 Pos Tarif HS"

      },

      "saldoAkhir": {

       "type": "number",

       "description": "saldo akhir"

      },

      "saldoAwal": {

       "type": "number",

       "description": "saldo awal"

      },

      "seriBarang": {

       "type": "integer",

       "description": "Sesuai kolom formulir BC 2.0 - D.31 No. Seri data barang"

      },

      "seriBarangDokAsal": {

       "type": "integer",

       "description": "seri barang dokumen asal"

      },

      "seriIjin": {

       "type": "integer",

       "description": "seri ijin barang"

      },

      "tahunPembuatan": {

       "type": "integer",

       "description": "tahun pembuatan barang"

      },

      "tarifCukai": {

       "type": "number",

       "description": "tarif cukai"

      },

      "tipe": {

       "type": "string",

       "minLength": 2,

       "description": "Sesuai kolom formulir BC 2.0 - D.32 Tipe Barang"

      },

      "uraian": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.32 Uraian Barang"

      },

      "volume": {

       "type": "number",

       "description": "volume barang",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "metodePenentuanNilai": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.36 Metode Penentuan Nilai Pabean: [Metode 1] Metode Nilai Transaksi Barang yang bersangkutan; [Metode 2] Metode Nilai Transaksi Barang Identik; [Metode 3] Metode Nilai Transaksi Barang Serupa; [Metode 4] Metode Deduksi; [Metode 5] Metode Komputasi; [Metode 6] Metode Fallback",

       "enum": [

        "Metode 1",

        "Metode 2",

        "Metode 3",

        "Metode 4",

        "Metode 5",

        "Metode 6"

       ]

      },

      "alasanMetodePenentuanNilai": {

       "type": ["string", "null"],

       "description": "Diisi apabila memilih selain Metode 1. Sesuai kolom formulir BC 2.0 - D.36 Alasan Penentuan Nilai Pabean: [KON] bukan transaksi jual beli berupa barang konsinyasi; [CMA] bukan transaksi jual beli berupa barang hadiah/promosi/contoh; [ITM] bukan transaksi jual beli berupa barang yang diimpor oleh intermediary yang tidak membeli barang; [LES] bukan transaksi jual beli berupa barang sewa (leasing); [HBH] bukan transaksi jual beli berupa barang bantuan/hibah; [BTR] bukan transaksi jual beli lainnya; [TTS] Transaksi jual beli tidak memenuhi persyaratan nilai transaksi;",

       "enum":[

        "KON",

        "CMA",

        "ITM",

        "LES",

        "HBH",

        "BTR",

        "TTS",

        null

       ]

      },

      "statementPerbedaanHarga": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.36 Perbedaan Harga Penawaran: [Y] Ya/Ada; [T] Tidak/Tidak Ada",

       "enum": [

        "Y",

        "T"

       ],

       "default": "T"

      },

      "barangTarif": {

       "type": "array",

       "description": "data barang tarif per barang",

       "items": [

        {

         "type": "object",

         "description": "data barang tarif BM",

         "properties": {

          "kodeJenisTarif": {

           "type": "string",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Jenis Tarif/Pembebanan. Referensi Jenis Tarif: [1] Advalorum atau [2] Spesifik",

           "enum": [

            "1",

            "2"

           ]

          },

          "jumlahSatuan": {

           "type": "number",

           "description": "jumlah satuan barang tarif BM",

           "maxlength": 24,

           "multipleOf": 0.0001

          },

          "kodeFasilitasTarif": {

           "type": "string",

           "description": "Kode fasilitas tarif BM. Sesuai kolom formulir BC 2.0 - D.34 Kode Fasilitas. Lihat Referensi Fasilitas Tarif"

          },

          "kodeJenisPungutan": {

           "type": "string",

           "description": "Set kode jenis pungutan Bea Masuk (BM) atau Bea Masuk Kemudahan Impor Tujuan Ekspor (BMKITE)",

           "enum": [

            "BM",

            "BMKITE"

           ]

          },

          "nilaiBayar": {

           "type": "number",

           "description": "nilai bayar barang tarif BM",

           "maxlength": 24,

           "multipleOf": 0.01

          },

          "seriBarang": {

           "type": "integer",

           "description": "seri barang"

          },

          "tarif": {

           "type": "number",

           "description": "Tarif BM. Sesuai kolom formulir BC 2.0 - D.34 Tarif",

           "maxlength": 24,

           "multipleOf": 0.01

          },

          "tarifFasilitas": {

           "type": "number",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Tarif dan Fasilitas",

           "maxlength": 5,

           "multipleOf": 0.01

          },

          "nilaiFasilitas": {

           "type": "number",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Tarif dan Fasilitas. Dapat diisi apabila Kode Fasilitas Tarif selain dibayar [1]",

           "maxlength": 24,

           "multipleOf": 0.01

          }

         },

         "required": [

          "kodeJenisTarif",

          "kodeFasilitasTarif",

          "kodeJenisPungutan",

          "tarifFasilitas",

          "nilaiBayar",

          "tarif",

          "nilaiFasilitas"

         ],

         "message": {

          "required": "Wajib mengisi kodeJenisTarif, kodeFasilitasTarif, kodeJenisPungutan, tarifFasilitas, nilaiBayar, tarif, dan nilaiFasilitas BM"

         }

        },

        {

         "type": "object",

         "properties": {

          "kodeJenisTarif": {

           "type": "string",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Jenis Tarif/Pembebanan. Referensi Jenis Tarif: [1] Advalorum atau [2] Spesifik",

           "enum": [

            "1",

            "2"

           ]

          },

          "jumlahSatuan": {

           "type": "number",

           "description": "jumlah satuan barang tarif",

           "maxlength": 24,

           "multipleOf": 0.0001

          },

          "kodeFasilitasTarif": {

           "type": "string",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Kode Fasilitas. Lihat Referensi Fasilitas Tarif"

          },

          "kodeJenisPungutan": {

           "type": "string",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Tarif dan Fasilitas. Lihat Referensi Jenis Pungutan"

          },

          "nilaiBayar": {

           "type": "number",

           "description": "nilai bayar barang tarif",

           "maxlength": 24,

           "multipleOf": 0.01

          },

          "seriBarang": {

           "type": "integer",

           "description": "seri barang"

          },

          "tarif": {

           "type": "number",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Tarif",

           "maxlength": 24,

           "multipleOf": 0.01

          },

          "tarifFasilitas": {

           "type": "number",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Tarif dan Fasilitas",

           "maxlength": 5,

           "multipleOf": 0.01

          },

          "nilaiFasilitas": {

           "type": "number",

           "description": "Sesuai kolom formulir BC 2.0 - D.34 Tarif dan Fasilitas. Dapat diisi apabila Kode Fasilitas Tarif selain dibayar [1]",

           "maxlength": 24,

           "multipleOf": 0.01

          }

         },

         "dependencies": {

          "kodeJenisPungutan": [

           "kodeFasilitasTarif",

           "tarifFasilitas",

           "nilaiBayar",

           "tarif",

           "nilaiFasilitas"

          ]

         },

         "message": {

          "required": "Wajib mengisi kodeJenisTarif, kodeFasilitasTarif, kodeJenisPungutan, tarifFasilitas, nilaiBayar, tarif, dan nilaiFasilitas"

         }

        }

       ]

      },

      "barangDokumen": {

       "type": "array",

       "description": "Sesuai kolom formulir BC 2.0 - D.33 Keterangan Fasilitas/Persyaratan dan Nomor Urut",

       "items":{

         "type": "object",

         "properties": {

          "seriDokumen": {

           "type": "string",

           "description": "seri dokumen"

          }

         }

        }

      },



      "barangSpekKhusus": {

       "type": "array",

       "description": "data barang dengan spesifikasi khusus",

       "items": {

         "type": "object",

         "properties": {

          "seriBarangSpekKhusus": {

           "type": "integer",

           "description": "seri barang spesifikasi khusus"

          },

          "kodeSpekKhusus": {

           "type": "integer",

           "description": "Lihat Referensi Spesifikasi Khusus [1] NOMOR MESIN; [2] NOMOR RANGKA; [3] SILINDER; [4] TAHUN PEMBUATAN; [5] JENIS KENDARAAN; [6] MERK; [7] MODEL; [8] NOMOR BPKB; [9] TANGGAL BPKB; [10] NOMOR FORM A; [11] TANGGAL FORM A; [12] NOMOR STNK; [13] TANGGAL STNK; [14] TIPE; [15] NOMOR CASI; [16] MUTU; [17] DAYA; [18] KUALITAS WARNA GULA; [19] CBU; [1001] ALAT DAPUR; [1002] TINGKAT KEPECAHAN; [1003] JENIS PREKURSOR; [1004] KUALITAS WARNA GULA; [1005] TPT BATIK MOTIF BATIK; [1006] JENIS PERKAKAS TANGAN; [1007] JENIS REFRIGERANT; [1008] JENIS BATERAI LITHIUM TIDAK BARU; [1009] JENIS FITUR TELEKOMUNIKASI; [1010] KOMPUTER TABLET ATAU GENGGAM; [1011] SMARTPHONE ATAU SMARTWATCH PHONE; [1012] TELEPON SELULER ATAU SATELIT; [1013] TELEPON ANALOG DAN PABX SYSTEM; [1014] BASE TRANSCEIVER STATION; [1015] ANTENA; [1016] PENYIARAN; [1017] RADAR MARITIM DAN PENERBANGAN; [1018] RADAR KENDARAAN DAN CUACA; [1019] RADAR SURVEILLANCE DAN GPS TRACKER; [1020] RADIO MARITIM PENERBANGAN BEACON",

           "enum": [

            1,

            2,

            3,

            4,

            5,

            6,

            7,

            8,

            9,

            10,

            11,

            12,

            13,

            14,

            15,

            16,

            17,

            18,

            19,

            1001,

            1002,

            1003,

            1004,

            1005,

            1006,

            1007,

            1008,

            1009,

            1010,

            1011,

            1012,

            1013,

            1014,

            1015,

            1016,

            1017,

            1018,

            1019,

            1020

           ]

          },

          "uraianBarangSpekKhusus": {

           "type": "string",

           "description": "uraian barang spesifikasi khusus"

          }

         }

        }

      },

      "barangVd": {

       "type": "array",

       "description": "data barang voluntary declaration",

       "items": {

         "type": "object",

         "properties": {

          "kodeJenisVd": {

           "type": "string",

           "description": "Lihat Referensi Jenis VD"

          },

          "nilaiBarangVd": {

           "type": "number",

           "maxlength": 24,

           "multipleOf": 0.0001,

           "description": "nilai barang voluntary declaration"

          }

         },

         "required": [

          "kodeJenisVd",

          "nilaiBarangVd"

         ],

         "message": {

          "required": "Wajib mengisi kodeJenisVd dan nilaiBarangVd"

         }

        }

      },

      "barangPemilik": {

       "type": "array",

       "description": "data barang entitas pemilik",

       "items": {

         "type": "object",

         "properties": {

          "seriBarang": {

           "type": "integer",

           "description": "seri barang"

          },

          "seriBarangPemilik": {

           "type": "integer",

           "description": "seri barang entitas pemilik"

          },

          "seriEntitas": {

           "type": "integer",

           "description": "seri entitas pemilik"

          }

         },

         "required": [

          "seriBarang",

          "seriBarangPemilik",

          "seriEntitas"

         ],

         "message": {

          "required": "Wajib mengisi seriBarang, seriBarangPemiliki, dan seriEntitas"

         }

        }

      }

     },

     "required": [

      "asuransi",

      "cif",

      "fob",

      "freight",

      "hargaSatuan",

      "jumlahKemasan",

      "jumlahSatuan",

      "kodeJenisKemasan",

      "kodeSatuanBarang",

      "merk",

      "posTarif",

      "saldoAkhir",

      "saldoAwal",

      "seriBarang",

      "tipe",

      "uraian",

      "metodePenentuanNilai",

      "alasanMetodePenentuanNilai",

      "statementPerbedaanHarga",

      "barangTarif",

      "barangVd"

     ],

     "message": {

      "required": "Wajib mengisi asuransi, cif, fob, freight, hargaSatuan, jumlahKemasan, jumlahSatuan, kodeJenisKemasan, kodeSatuanBarang, merk, posTarif, saldoAkhir, saldoAwal, seriBarang, tipe, uraian, metodePenentuanNilai, statementPerbedaanHarga, barangTarif dan barangVd"

     }

    }

  },

  "entitas": {

   "type": "array",

   "description": "data entitas dalam pengajuan dokumen pabean",

   "items": [

    {

     "type": "object",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.3 Alamat Importir"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas importir (1). Mengacu pada Referensi Entitas",

       "const": "1"

      },

      "kodeJenisApi": {

       "type": "string",

       "description": "Referensi Jenis Api entitas: [01] APIU atau [02] APIP",

       "enum": [

        "01",

        "02"

       ]

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "kodeStatus": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.4 Status. Status importir"

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.3 Nama Importir"

      },

      "nibEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.5 NIB. Nomor Induk Berusaha"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.2 Identitas Importir"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeJenisApi",

      "kodeJenisIdentitas",

      "kodeStatus",

      "namaEntitas",

      "nibEntitas",

      "nomorIdentitas",

      "seriEntitas"

     ],

     "message": {

      "required": "Wajib mengisi alamatEntitas, kodeEntitas, kodeJenisApi, kodeJenisIdentitas, kodeStatus, namaEntitas, nibEntitas, nomorIdentitas, dan seriEntitas Importir"

     }

    },

    {

     "type": "object",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.3a Alamat Pemilik Barang"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas pemilik barang (7). Mengacu pada Referensi Entitas",

       "const": "7"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.3a Nama Pemilik Barang"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.2a Identitas Pemilik Barang"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      },

      "kodeAfiliasi": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.4a Hubungan dengan Penjual: [AFL] Affiliated Company; [CTR] Financial/legally controlled; [FAM] Family member; [TAH] Tidak Berhubungan",

       "enum": [

        "AFL",

        "CTR",

        "FAM",

        "TAH"

       ]

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeJenisIdentitas",

      "namaEntitas",

      "nomorIdentitas",

      "seriEntitas",

      "kodeAfiliasi"

     ],

     "message": {

      "required": "Wajib mengisi alamatEntitas, kodeEntitas, kodeJenisIdentitas, namaEntitas, nomorIdentitas, dan seriEntitas Pemilik Barang"

     }

    },

    {

     "type": "object",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.1 Alamat Pengirim"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas pengirim (9). Mengacu pada Referensi Entitas",

       "const": "9"

      },

      "kodeNegara": {

       "type": "string",

       "description": "Lihat Referensi Negara",

       "pattern": "^[A-Za-z]{2}$"

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.1 Nama Pengirim"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeNegara",

      "namaEntitas",

      "seriEntitas"

     ],

     "message": {

      "required": "Wajib mengisi alamatEntitas, kodeEntitas, kodeNegara, namaEntitas, dan seriEntitas Pengirim"

     }

    },

    {

     "type": "object",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.1a Alamat Penjual"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas penjual (10). Mengacu pada Referensi Entitas",

       "const": "10"

      },

      "kodeNegara": {

       "type": "string",

       "description": "Lihat Referensi Negara",

       "pattern": "^[A-Za-z]{2}$"

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.1a Nama Penjual"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeNegara",

      "namaEntitas",

      "seriEntitas"

     ],

     "message": {

      "required": "Wajib mengisi alamatEntitas, kodeEntitas, kodeNegara, namaEntitas, dan seriEntitas Penjual"

     }

    },

    {

     "type": "object",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Alamat Pemusatan"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas pemusatan (11). Mengacu pada Referensi Entitas",

       "const": "11"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Nama Pemusatan"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Nomor identitas pemusatan"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeJenisIdentitas",

      "namaEntitas",

      "nomorIdentitas",

      "seriEntitas"

     ],

     "message": {

      "required": "Wajib mengisi alamatEntitas, kodeEntitas, kodeJenisApi, kodeJenisIdentitas, namaEntitas, nibEntitas, nomorIdentitas, dan seriEntitas Pemusatan"

     }

    },

    {

     "type": "object",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.7 Alamat PPJK"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas PPJK (4). Mengacu pada Referensi Entitas",

       "const": "4"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.7 Nama PPJK"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.6 NPWP"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     }

    }

   ]

  },

  "kemasan": {

   "type": "array",

   "description": "data kemasan dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "description": "data kemasan yang digunakan untuk mengemas barang impor",

     "properties": {

      "jumlahKemasan": {

       "type": "integer",

       "description": "Sesuai kolom formulir BC 2.0 - D.28 Jumlah Kemasan"

      },

      "kodeJenisKemasan": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.28 Jenis Kemasan. Lihat Referensi Jenis Kemasan"

      },

      "merkKemasan": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.28 Merek Kemasan"

      },

      "seriKemasan": {

       "type": "integer",

       "description": "seri data kemasan berdasarkan data yang dimasukkan"

      }

     },

     "required": [

      "jumlahKemasan",

      "kodeJenisKemasan",

      "merkKemasan",

      "seriKemasan"

     ],

     "message": {

      "required": "Wajib mengisi jumlahKemasan, kodeJenisKemasan, merkKemasan, dan seriKemasan"

     }

    }

  },

  "kontainer": {

   "type": "array",

   "description": "data kontainer dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "description": "data peti kemas/kontainer yang digunakan untuk mengangkut barang impor, apabila pengangkutan menggunakan peti kemas/kontainer",

     "properties": {

      "kodeJenisKontainer": {

       "type": "string",

       "description": "Referensi Jenis Kontainer: [4] Empty, [7] LCL, [8] FCL",

       "enum": [

        "4",

        "7",

        "8"

       ]

      },

      "kodeTipeKontainer": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.27 Tipe Peti Kemas. Referensi Tipe Kontainer: [1] General/Dry Cargo, [2] Tunne Type, [3] Open Top Steel, [4] Flat Rack, [5] Reefer/Refregete, [6] Barge Container, [7] Bulk Container, [8] Isotank, [99] Lain-lain ",

       "enum": [

        "1",

        "2",

        "3",

        "4",

        "5",

        "6",

        "7",

        "8",

        "99"

       ]

      },

      "kodeUkuranKontainer": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.27 Ukuran Peti Kemas. Referensi Ukuran Kontainer: [20] 20 feet, [40] 40 feet, [45] 45 feet, [60] 60 feet",

       "enum": [

        "20",

        "40",

        "45",

        "60"

       ]

      },

      "nomorKontainer": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.27 Nomor Peti Kemas"

      },

      "seriKontainer": {

       "type": "integer",

       "description": "seri data kontainer berdasarkan data yang dimasukkan"

      }

     },

     "dependencies": {

      "seriKontainer": [

       "kodeTipeKontainer",

       "kodeUkuranKontainer",

       "nomorKontainer"

      ]

     },

     "message": {

      "required": "Wajib mengisi kodeTipeKontainer, kodeUkuranKontainer, nomorKontainer, dan seriKontainer"

     }

    }

  },

  "dokumen": {

   "type": "array",

   "description": "data dokumen pelengkap dalam pengajuan dokumen pabean",

   "items": [

    {

     "type": "object",

     "description": "data invoice sebagai dokumen pelengkap",

     "properties": {

      "idDokumen": {

       "type": "string",

       "description": "ID Dokumen"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "Set kode dokumen invoice (380)",

       "const": "380"

      },

      "kodeFasilitas": {

       "type": "string",

       "description": "Lihat Referensi Fasilitas"

      },

      "kodeIjin": {

       "type": "string",

       "description": "Lihat Referensi Ijin"

      },

      "nomorDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.15 Nomor Invoice"

      },

      "seriDokumen": {

       "type": "integer",

       "description": "seri dokumen pelengkap pabean"

      },

      "tanggalDokumen": {

       "type": "string",

       "format": "date",

       "description": "Sesuai kolom formulir BC 2.0 - D.15 Tanggal Invoice dengan format YYYY-MM-DD"

      },

      "urlDokumen": {

       "type": "string",

       "description": "url dokumen invoice"

      }

     },

     "required": [

      "kodeDokumen",

      "nomorDokumen",

      "seriDokumen",

      "tanggalDokumen"

     ],

     "message": {

      "required": "Wajib mengisi kodeDokumen, nomorDokumen, seriDokumen, dan tanggalDokumen Invoice"

     }

    },

    {

     "type": "object",

     "description": "data house-bl/awb sebagai dokumen pelengkap",

     "properties": {

      "idDokumen": {

       "type": "string",

       "description": "ID Dokumen"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "Set kode dokumen House-BL/AWB (705 / 740)",

       "enum": [

        "705",

        "740"

       ]

      },

      "kodeFasilitas": {

       "type": "string",

       "description": "Lihat Referensi Fasilitas"

      },

      "kodeIjin": {

       "type": "string",

       "description": "Lihat Referensi Ijin"

      },

      "nomorDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.17 Nomor House-BL/AWB"

      },

      "seriDokumen": {

       "type": "integer",

       "description": "seri dokumen pelengkap pabean"

      },

      "tanggalDokumen": {

       "type": "string",

       "format": "date",

       "description": "Sesuai kolom formulir BC 3.0 - D.17 Tanggal House-BL/AWB dengan format YYYY-MM-DD"

      },

      "urlDokumen": {

       "type": "string",

       "description": "url dokumen Nomor House-BL/AWB"

      }

     },

     "dependencies": {

      "seriDokumen": [

       "kodeDokumen",

       "nomorDokumen",

       "tanggalDokumen"

      ]

     },

     "message": {

      "dependencies": "Jika terdapat seriDokumen House-BL/AWB, maka wajib mengisi kodeDokumen, nomorDokumen, dan tanggalDokumen House-BL/AWB"

     }

    },

    {

     "type": "object",

     "description": "data dokumen persyaratan impor dan/atau surat keputusan fasilitas impor dalam pengajuan dokumen pabean",

     "properties": {

      "idDokumen": {

       "type": "string",

       "description": "ID Dokumen"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.19 Pemenuhan Persyaratan/Fasilitas Impor. Lihat Referensi Dokumen"

      },

      "kodeFasilitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.19 Pemenuhan Persyaratan/Fasilitas Impor. Lihat Referensi Fasilitas"

      },

      "kodeIjin": {

       "type": "string",

       "description": "Lihat Referensi Ijin"

      },

      "namaFasilitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.19 Pemenuhan Persyaratan/Fasilitas Impor"

      },

      "nomorDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.19 Nomor Pemenuhan Persyaratan/Fasilitas Impor"

      },

      "seriDokumen": {

       "type": "integer",

       "description": "seri dokumen pelengkap pabean"

      },

      "tanggalDokumen": {

       "type": "string",

       "format": "date",

       "description": "Sesuai kolom formulir BC 2.0 - D.19 Tanggal Pemenuhan Persyaratan/Fasilitas Impor dengan format YYYY-MM-DD"

      },

      "urlDokumen": {

       "type": "string",

       "description": "url dokumen pelengkap pabean"

      }

     },

     "dependencies": {

      "seriDokumen": [

       "kodeDokumen",

       "nomorDokumen",

       "tanggalDokumen"

      ]

     },

     "message": {

      "dependencies": "Jika terdapat seriDokumen Pemenuhan Persyaratan/Fasilitas Impor, maka wajib mengisi kodeDokumen, nomorDokumen, dan tanggalDokumen Pemenuhan Persyaratan/Fasilitas Impor"

     }

    }

   ]

  },

  "pengangkut": {

   "type": "array",

   "description": "data pengangkut dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "properties": {

      "kodeBendera": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.10 Bendera. Lihat Referensi Bendera"

      },

      "namaPengangkut": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.10 Nama Sarana Pengangkutan"

      },

      "nomorPengangkut": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.10 No. Voy/Flight"

      },

      "kodeCaraAngkut": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.9 Cara Pengangkutan. Referensi Cara Angkut: [1] Laut, [2] Kereta Api, [3] Darat, [4] Udara, [5] Pos, [6] Multimoda, [7] Instalasi/Pipa, [8] Perairan, [9] Lainnya",

       "enum": [

        "1",

        "2",

        "3",

        "4",

        "5",

        "6",

        "7",

        "8",

        "9"

       ]

      },

      "seriPengangkut": {

       "type": "integer",

       "description": "seri data pengangkut"

      }

     },

     "required": [

      "kodeBendera",

      "namaPengangkut",

      "nomorPengangkut",

      "kodeCaraAngkut",

      "seriPengangkut"

     ],

     "message": {

      "required": "Wajib mengisi kodeBendera, namaPengangkut, nomorPengangkut, kodeCaraAngkut, dan seriPengangkut"

     }

    }

  },

  "informasiKomponenBiaya": {

   "type": "array",

   "description": "Data Informasi Komponen Biaya",

   "items": {

     "type": "object",

     "properties": {

      "jenisNilai": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 2.0 - D.25a Informasi Komponen Biaya: [1] Nilai Pasti; [2] Nilai Perkiraan (VD)",

       "enum": [

        "1",

        "2"

       ]

      },

      "hargaInvoice": {

       "type": "number",

       "description": "Harga Invoice",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "pembayaranTidakLangsung": {

       "type": "number",

       "description": "Pembayaran Tidak Langsung",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "diskon": {

       "type": "number",

       "description": "Diskon",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "komisiPenjualan": {

       "type": "number",

       "description": "Komisi Penjualan",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaPengemasan": {

       "type": "number",

       "description": "Biaya Pengemasan",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaPengepakan": {

       "type": "number",

       "description": "Biaya Pengepakan",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "assist": {

       "type": "number",

       "description": "Assist",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "royalti": {

       "type": "number",

       "description": "Royalti",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "proceeds": {

       "type": "number",

       "description": "Proceeds",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaTransportasi": {

       "type": "number",

       "description": "Biaya Transportasi",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaPemuatan": {

       "type": "number",

       "description": "Biaya Pemuatan",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "asuransi": {

       "type": "number",

       "description": "Asuransi",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "garansi": {

       "type": "number",

       "description": "Garansi",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaKepentinganSendiri": {

       "type": "number",

       "description": "Biaya Kepentingan Sendiri",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaPascaImpor": {

       "type": "number",

       "description": "Biaya Pasca Impor",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "biayaPajakInternal": {

       "type": "number",

       "description": "Biaya Pajak Internal",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "bunga": {

       "type": "number",

       "description": "Bunga",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "deviden": {

       "type": "number",

       "description": "Deviden",

       "maxlength": 24,

       "multipleOf": 0.0001

      }

     },

     "required": [

      "jenisNilai"

     ],

     "message": {

      "required": "Wajib mengisi jenisNilai"

     }

    }

  }

 },

 "required": [

  "asuransi",

  "bruto",

  "cif",

  "kodeJenisImpor",

  "freight",

  "jabatanTtd",

  "jumlahKontainer",

  "kodeCaraBayar",

  "kodeKantor",

  "kodePelMuat",

  "kodePelTujuan",

  "kodeTps",

  "kodeTutupPu",

  "kodeValuta",

  "kotaTtd",

  "namaTtd",

  "ndpbm",

  "netto",

  "nomorAju",

  "tanggalTtd",

  "tanggalTiba",

  "biayaTambahan",

  "biayaPengurang",

  "barang",

  "entitas",

  "kemasan",

  "dokumen",

  "pengangkut"

 ],

 "message": {

  "required": "Wajib mengisi asuransi, bruto, cif, kodeJenisImpor, freight, jabatanTtd, jumlahKontainer, kodeCaraBayar, kodeKantor, kodePelMuat, kodePelTujuan, kodeTps, kodeTutupPu, kodeValuta, kotaTtd, namaTtd, ndpbm, netto, nomorAju, tanggalTiba, tanggalTtd, biayaTambahan, biayaPengurang, barang, entitas, kemasan, dokumen, dan pengangkut"

 }

}
```
## BC 2.0 - Payload
```json
{
    "asalData": "S",
    "flagSsm": "3",
    "nik": "nik,
    "kodeKenaPajak": "1",
    "asuransi": 0,
    "biayaPengurang": 0,
    "biayaTambahan": 0,
    "bruto": 1281.5,
    "cif": 101731.26,
    "disclaimer": "0",
    "flagVd": "T",
    "fob": 101231.26,
    "freight": 500,
    "hargaPenyerahan": 0,
    "idPengguna": "id_pengguna
    "jabatanTtd": "-",
    "jumlahKontainer": 4,
    "jumlahTandaPengaman": 0,
    "kodeAsuransi": "DN",
    "kodeCaraBayar": "1",
    "kodeDokumen": "20",
    "kodeIncoterm": "FOB",
    "kodeJenisImpor": "",
    "kodeJenisNilai": "IMB",
    "kodeKantor": "060600",
    "kodePelMuat": "CNSHA",
    "kodePelTransit": "",
    "kodePelTujuan": "IDTES",
    "kodePelBongkar": "IDTES",
    "kodeKantorBongkar": "060100",
    "kodeTujuanTpb": "1",
    "kodeTps": "UTPK",
    "kodeTutupPu": "11",
    "kodeValuta": "USD",
    "kotaTtd": "kota_ttd",
    "namaTtd": "nama_ttd",
    "ndpbm": 16343,
    "netto": 1238,
    "nilaiBarang": 1662593982.18,
    "nilaiIncoterm": 101231.26,
    "nilaiMaklon": 0,
    "nomorAju": "nomor_aju",
    "nomorBc11": "000545",
    "posBc11": "0109",
    "seri": 0,
    "subposBc11": "00000000",
    "tanggalAju": "2024-06-25",
    "tanggalBc11": "2024-05-02",
    "tanggalTiba": "2024-01-01",
    "tanggalTtd": "2024-06-25",
    "totalDanaSawit": 0,
    "volume": 0,
    "vd": 0,
    "barang": [
        {
            "asuransi": 0,
            "bruto": 1281.5,
            "cif": 101731.26,
            "cifRupiah": 1662593982.18,
            "diskon": 0,
            "fob": 101231.26,
            "freight": 500,
            "kodeBarang": "kode_barang
            "kodeDokumen": "23",
            "kodeKategoriBarang": "11",
            "spesifikasiLain": "--",
            "ukuran": "-",
            "ndpbm": 16343,
            "hargaEkspor": 0,
            "hargaPatokan": 0,
            "hargaPenyerahan": 0,
            "hargaPerolehan": 0,
            "hargaSatuan": 81.77,
            "hjeCukai": 0,
            "isiPerKemasan": 0,
            "jumlahBahanBaku": 0,
            "jumlahDilekatkan": 0,
            "jumlahKemasan": 21,
            "jumlahPitaCukai": 0,
            "jumlahRealisasi": 0,
            "jumlahSatuan": 1238,
            "kapasitasSilinder": 0,
            "kodePerhitungan": "0",
            "kodeAsalBahanBaku": "0",
            "kodeJenisKemasan": "BL",
            "kodeKondisiBarang": "null",
            "kodeNegaraAsal": "CL",
            "kodeSatuanBarang": "KGM",
            "merk": "A",
            "ndbpm": 16343,
            "netto": 1238,
            "nilaiBarang": 101231.26,
            "nilaiDanaSawit": 0,
            "nilaiDevisa": 0,
            "nilaiTambah": 0,
            "pernyataanLartas": "Y",
            "persentaseImpor": 0,
            "posTarif": "05051010",
            "saldoAkhir": 0,
            "saldoAwal": 0,
            "seriBarang": 1,
            "tarifCukai": 0,
            "tipe": "-",
            "uraian": "uraian_barang
            "volume": 0,
            "barangDokumen": [
                {
                    "seriDokumen": "1",
                    "seriIjin": null
                }
            ],
            "barangTarif": [
                {
                    "jumlahSatuan": 1238,
                    "kodeFasilitasTarif": "3",
                    "kodeJenisPungutan": "BM",
                    "kodeSatuanBarang": "KGM",
                    "kodeJenisTarif": "1",
                    "nilaiBayar": 0,
                    "nilaiSudahDilunasi": 0,
                    "nilaiFasilitas": 83129699.11,
                    "seriBarang": 1,
                    "tarif": 5,
                    "tarifFasilitas": 100
                },
                {
                    "jumlahSatuan": 1238,
                    "kodeFasilitasTarif": "6",
                    "kodeJenisPungutan": "PPH",
                    "kodeJenisTarif": "1",
                    "kodeSatuanBarang": "KGM",
                    "nilaiBayar": 0,
                    "nilaiFasilitas": 43643092.03,
                    "seriBarang": 1,
                    "nilaiSudahDilunasi": 0,
                    "tarif": 2.5,
                    "tarifFasilitas": 100
                },
                {
                    "jumlahSatuan": 1238,
                    "kodeFasilitasTarif": "6",
                    "kodeJenisPungutan": "PPN",
                    "kodeJenisTarif": "1",
                    "kodeSatuanBarang": "KGM",
                    "nilaiBayar": 0,
                    "nilaiFasilitas": 192029604.94,
                    "seriBarang": 1,
                    "nilaiSudahDilunasi": 0,
                    "tarif": 11,
                    "tarifFasilitas": 100
                }
            ],
            "barangVd": [
                {
                    "kodeJenisVd": "NTR",
                    "nilaiBarangVd": 0
                }
            ],
            "barangSpekKhusus": [],
            "barangPemilik": [
                {
                    "seriBarang": 1,
                    "seriBarangPemilik": 7,
                    "seriEntitas": 7
                }
            ]
        }
    ],
    "entitas": [
        {
            "alamatEntitas": "alamat_entitas",
            "kodeEntitas": "3",
            "nomorIjinEntitas": "nomor_ijin_entitas",
            "tanggalIjinEntitas": "2024-06-26",
            "kodeJenisApi": "02",
            "kodeJenisIdentitas": "5",
            "kodeStatus": null,
            "namaEntitas": "nama_entitias",
            "nibEntitas": "nib_entitas",
            "nomorIdentitas": "nomor_identitas",
            "seriEntitas": 1,
            "kodeNegara": "ID"
        },
        {
            "alamatEntitas": "alamat_entitas",
            "kodeEntitas": "5",
            "nomorIjinEntitas": "",
            "tanggalIjinEntitas": "",
            "kodeJenisApi": "",
            "kodeJenisIdentitas": "0",
            "kodeStatus": null,
            "namaEntitas": "nama_entitias",
            "nibEntitas": "",
            "nomorIdentitas": "",
            "seriEntitas": 3,
            "kodeNegara": "CN"
        },
        {
            "alamatEntitas": "alamat_entitas",
            "kodeEntitas": "7",
            "nomorIjinEntitas": "nomor_ijin_entitas",
            "tanggalIjinEntitas": "2024-06-24",
            "kodeJenisApi": "",
            "kodeJenisIdentitas": "5",
            "kodeStatus": "5",
            "namaEntitas": "nama_entitias",
            "nibEntitas": "",
            "nomorIdentitas": "nomor_identitas",
            "seriEntitas": 7,
            "kodeNegara": "ID"
        }
    ],
    "kemasan": [
        {
            "jumlahKemasan": 21,
            "kodeJenisKemasan": "BL",
            "merkKemasan": "-",
            "seriKemasan": 1
        }
    ],
    "kontainer": [
        {
            "kodeJenisKontainer": "8",
            "kodeTipeKontainer": "1",
            "kodeUkuranKontainer": "20",
            "nomorKontainer": "DFOU6117210",
            "seriKontainer": 2
        },
        {
            "kodeJenisKontainer": "8",
            "kodeTipeKontainer": "1",
            "kodeUkuranKontainer": "20",
            "nomorKontainer": "CCLU7696335",
            "seriKontainer": 4
        },
        {
            "kodeJenisKontainer": "8",
            "kodeTipeKontainer": "1",
            "kodeUkuranKontainer": "20",
            "nomorKontainer": "SITU2881167",
            "seriKontainer": 1
        },
        {
            "kodeJenisKontainer": "8",
            "kodeTipeKontainer": "1",
            "kodeUkuranKontainer": "20",
            "nomorKontainer": "MSKU6766687",
            "seriKontainer": 3
        }
    ],
    "dokumen": [
        {
            "idDokumen": "id_dokumen",
            "kodeDokumen": "380",
            "nomorDokumen": "142680",
            "seriDokumen": 2,
            "tanggalDokumen": "2024-04-09",
            "urlDokumen": "url_dokumen"
        },
        {
            "idDokumen": "id_dokumen",
            "kodeDokumen": "705",
            "nomorDokumen": "SITGSHDRK85694",
            "seriDokumen": 4,
            "tanggalDokumen": "2023-10-14",
            "urlDokumen": "url_dokumen"
        },
        {
            "idDokumen": "id_dokumen",
            "kodeDokumen": "944",
            "nomorDokumen": "2024.1.1401.0K07.I.000373",
            "seriDokumen": 6,
            "tanggalDokumen": "2024-05-03",
            "urlDokumen": "url_dokumen"
        },
        {
            "idDokumen": "id_dokumen",
            "kodeDokumen": "111",
            "nomorDokumen": "9120100781919",
            "seriDokumen": 1,
            "tanggalDokumen": "2019-01-01",
            "urlDokumen": "url_dokumen"
        },
        {
            "idDokumen": "id_dokumen",
            "kodeDokumen": "465",
            "kodeFasilitas": "00",
            "nomorDokumen": "RCMLC042596",
            "seriDokumen": 3,
            "tanggalDokumen": "2023-10-16",
            "urlDokumen": "url_dokumen"
        },
        {
            "idDokumen": "id_dokumen",
            "kodeDokumen": "943",
            "nomorDokumen": "2024.1.1401.0.K05.I.000373",
            "seriDokumen": 5,
            "tanggalDokumen": "2024-05-03",
            "urlDokumen": "url_dokumen"
        }
    ],
    "pengangkut": [
        {
            "kodeBendera": "kode_bendera",
            "namaPengangkut": "nama_pengangkut",
            "nomorPengangkut": "2408S",
            "kodeCaraAngkut": "1",
            "seriPengangkut": 1
        }
    ]
}
```
## BC 2.0 - Dokumen
```json
{

  "info": {

    "_postman_id": "6092dc98-41af-4e54-8d2f-72ebf77e6ef6",

    "name": "H2H Upload Dokap dan Gambar PROD OpenAPI",

    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",

    "_exporter_id": "15271979"

  },

  "item": [

    {

      "name": "UPLOAD DOKAP-SINGLE",

      "protocolProfileBehavior": {

        "disabledSystemHeaders": {

          "accept-encoding": true

        }

      },

      "request": {

        "auth": {

          "type": "bearer",

          "bearer": [

            {

              "key": "token",

              "value": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIzbXo1OTYwdE9MbkhhT0JLTHRQSG15N2VmT0plQVo5UmVZdk...",

              "type": "string"

            }

          ]

        },

        "method": "POST",

        "header": [

          { "key": "Accept-Language", "value": "en-US,en;q=0.9" },

          { "key": "Sec-Fetch-Dest", "value": "empty" },

          { "key": "Sec-Fetch-Mode", "value": "cors" },

          { "key": "Sec-Fetch-Site", "value": "same-site" },

          { "key": "Beacukai-Api-Key", "value": "f662de2e-1d35-4b11-b2fd-ee164a5c9d83", "type": "text" }

        ],

        "body": {

          "mode": "formdata",

          "formdata": [

            { "type": "file", "key": "file", "src": "/C:/Users/User/Downloads/dummy_4mb.pdf" },

            { "type": "text", "key": "param", "value": "{\"nomorAju\": \"000020SUJ64320260130000001\", \"seriDokumen\": 1, \"npwp\": \"1000000000554429\"}" }

          ]

        },

        "url": {

          "raw": "https://apis-gw.beacukai.go.id/v2/openapi/file/dokumen",

          "protocol": "https",

          "host": ["apis-gw", "beacukai", "go", "id"],

          "path": ["v2", "openapi", "file", "dokumen"]

        }

      },

      "response": []

    },

    {

      "name": "UPLOAD GAMBAR-SINGLE",

      "protocolProfileBehavior": {

        "disabledSystemHeaders": {

          "accept-encoding": true

        }

      },

      "request": {

        "auth": {

          "type": "bearer",

          "bearer": [

            {

              "key": "token",

              "value": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIzbXo1OTYwdE9MbkhhT0JLTHRQSG15N2VmT0plQVo5UmVZdk...",

              "type": "string"

            }

          ]

        },

        "method": "POST",

        "header": [

          { "key": "Beacukai-Api-Key", "value": "f662de2e-1d35-4b11-b2fd-ee164a5c9d83", "type": "text" }

        ],

        "body": {

          "mode": "formdata",

          "formdata": [

            { "type": "file", "key": "file", "src": "/C:/Users/User/Downloads/Screenshot 2026-05-06 125947.jpg" },

            { "type": "text", "key": "param", "value": "{\"keterangan\":\"barang1\", \"nomorAju\": \"000020SUJ64320260130000001\", \"seriBarang\": 2, \"npwp\": \"1000000000554429\"}" }

          ]

        },

        "url": {

          "raw": "https://apis-gw.beacukai.go.id/v2/openapi/file/barang",

          "protocol": "https",

          "host": ["apis-gw", "beacukai", "go", "id"],

          "path": ["v2", "openapi", "file", "barang"]

        }

      },

      "response": []

    },

    {

      "name": "UPLOAD DOKAP NPD",

      "protocolProfileBehavior": {

        "disabledSystemHeaders": {

          "accept-encoding": true

        }

      },

      "request": {

        "auth": {

          "type": "bearer",

          "bearer": [

            {

              "key": "token",

              "value": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIzbXo1OTYwdE9MbkhhT0JLTHRQSG15N2VmT0plQVo5UmVZdk...",

              "type": "string"

            }

          ]

        },

        "method": "POST",

        "header": [

          { "key": "Accept-Language", "value": "en-US,en;q=0.9" },

          { "key": "Beacukai-Api-Key", "value": "f662de2e-1d35-4b11-b2fd-ee164a5c9d83" },

          { "key": "Sec-Fetch-Dest", "value": "empty" },

          { "key": "Sec-Fetch-Mode", "value": "cors" },

          { "key": "Sec-Fetch-Site", "value": "same-site" }

        ],

        "body": {

          "mode": "formdata",

          "formdata": [

            { "type": "file", "key": "file", "src": "/C:/Users/User/Downloads/dummy_4mb.pdf" },

            { "type": "text", "key": "param", "value": "{\"nomorAju\": \"000020LIP58420260507788007\", \"seriDokumen\": 1, \"npwp\": \"0123456789012345\"}" }

          ]

        },

        "url": {

          "raw": "https://apis-gw.beacukai.go.id/v2/openapi/file/upload-dokap-npd",

          "protocol": "https",

          "host": ["apis-gw", "beacukai", "go", "id"],

          "path": ["v2", "openapi", "file", "upload-dokap-npd"]

        }

      },

      "response": []

    }

  ]

}
```

# Ekspor
## BC 3.0 - Schema
```json
{

 "$schema": "http://json-schema.org/draft-07/schema",

 "type": "object",

 "title": "Schema Kirim Dokumen BC 30",

 "description": "JSON Schema untuk Kirim Dokumen Pabean v.0.5.29. Terdiri atas data header dan data barang. Data header merupakan data umum dokumen pabean sedangkan data barang merupakan data detil atas barang pada dokumen pabean",

 "properties": {

  "asalData": {

   "type": "string",

   "description": "set value [S]",

   "enum":[

    "S"

   ],

   "message": "Asal pengiriman data secara Host to Host: S"

  },

  "asuransi": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.37 Nilai Asuransi",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai asuransi maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "bruto": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.42 Berat Kotor (kg)",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Nilai bruto maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "cif": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.35 Nilai Ekspor",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai cif maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "disclaimer": {

   "type": "string",

   "description": "Persetujuan pengguna dalam kirim dokumen pabean: [1] Ya atau [0] Tidak",

   "enum": [

    "0",

    "1"

   ],

   "message": "Persetujuan pengguna dalam kirim dokumen pabean: 1 untuk Ya atau 0 untuk Tidak"

  },

  "flagCurah": {

   "type": "string",

   "description": "flag barang curah [1] atau non curah [2]",

   "enum": [

    "1",

    "2"

   ],

   "message": "Flag barang curah: 1 untuk barang curah atau 2 untuk barang non curah "

  },

  "flagMigas": {

   "type": "string",

   "description": "flag barang migas [1] atau non migas [2]",

   "enum": [

    "1",

    "2"

   ],

   "message": "Flag barang migas: 1 untuk barang migas atau 2 untuk barang non migas "

  },

  "fob": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.35 Nilai Ekspor",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai fob maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "freight": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.36 Nilai Freight",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai freight maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "idPengguna": {

   "type": "string",

   "description": "Identitas pengguna",

   "message": "Identitas pengguna"

  },

  "jabatanTtd": {

   "type": "string",

   "description": "Jabatan pengguna yang mengajukan dokumen ekspor",

   "message": "Jabatan pengguna yang mengajukan dokumen ekspor"

  },

  "jumlahKontainer": {

   "type": "integer",

   "description": "Sesuai kolom formulir BC 3.0 - F.39 Jumlah Peti Kemas",

   "message": "Jumlah kontainer atau peti kemas. Jika tidak ada kontainer dapat diisi 0"

  },

  "kodeAsuransi": {

   "type": "string",

   "description": "kode asuransi yang dibayar di [LN] luar negeri atau [DN] dalam negeri",

   "enum": [

    "LN",

    "DN"

   ],

   "message": "Kode asuransi yang dibayar: LN untuk luar negeri atau DN untuk dalam negeri"

  },

  "kodeCaraBayar": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - E. Cara Bayar. Lihat Referensi Cara Bayar",

   "message": "Format kode sesuai Referensi Cara Bayar"

  },

  "kodeCaraDagang": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - D. Cara Dagang. Lihat Referensi Cara Dagang",

   "message": "Format kode sesuai Referensi Cara Dagang"

  },

  "kodeDokumen": {

   "type": "string",

   "description": "set value [30]",

   "const": "30",

   "message": "Format kode sesuai Referensi Dokumen Ekspor: 30"

  },

  "kodeIncoterm": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.32 Cara Penyerahan Barang. Lihat Referensi Incoterm",

   "message": "Format kode sesuai Referensi Incoterm"

  },

  "kodeJenisProsedur": {

   "type": "string",

   "description": "Lihat Referensi Jenis Prosedur",

   "message": "Format kode sesuai Referensi Jenis Prosedur"

  },

  "kodeJenisEkspor": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - B. Jenis Ekspor. Lihat Referensi Jenis Ekspor",

   "message": "Format kode sesuai Referensi Jenis Ekspor"

  },

  "kodeJenisNilai": {

   "type": "string",

   "description": "Lihat Referensi Jenis Nilai",

   "message": "Format kode sesuai Referensi Jenis Nilai"

  },

  "kodeKantor": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.26. Kantor Bea Cukai Pendaftaran. Lihat Referensi Kantor",

   "message": "Format kode sesuai Referensi Kantor"

  },

  "kodeKantorEkspor": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - A.2. Kantor Pabean Ekspor. Lihat Referensi Kantor",

   "message": "Format kode sesuai Referensi Kantor"

  },

  "kodeKantorMuat": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - A.1. Kantor Pabean Pemuatan. Lihat Referensi Kantor",

   "message": "Format kode sesuai Referensi Kantor"

  },

  "kodeKantorPeriksa": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.31 Kantor Pabean Pemeriksaan. Lihat Referensi Kantor",

   "message": "Format kode sesuai Referensi Kantor"

  },

  "kodeKategoriEkspor": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - C. Kategori Ekspor. Lihat Referensi Kategori Ekspor",

   "message": "Format kode sesuai Referensi Kategori Ekspor"

  },

  "kodeLokasi": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.30 Lokasi pemeriksaan: [1] KP Tempat Pemuatan; [2] Gudang Eksportir; [3] Tempat Lain yang diizinkan; [4] TPS; [5] TPP; [6] TPB; [7] Tempat Penimbunan Lainnya; [8] Gudang Konsolidator",

   "enum": [

    "1",

    "2",

    "3",

    "4",

    "5",

    "6",

    "7",

    "8"

   ],

   "message": "Kode lokasi pemeriksaan: 1 untuk KP Tempat Pemuatan; 2 untuk Gudang Eksportir; 3 untuk Tempat Lain yang diizinkan; 4 untuk TPS; 5 untuk TPP; 6 untuk TPB; 7 untuk Tempat Penimbunan Lainnya; 8 untuk Gudang Konsolidator"

  },

  "kodeNegaraTujuan": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.26 Negara Tujuan Ekspor. Lihat Referensi Negara",

   "message": "Format kode sesuai Referensi Negara",

   "pattern": "^[A-Z]{2}$"

  },

  "kodePelEkspor": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.22 Pelabuhan/Tempat Muat Ekspor. Lihat Referensi Pelabuhan",

   "message": "Format kode pelabuhan/tempat muat ekspor sesuai Referensi Pelabuhan"

  },

  "kodePelMuat": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.21 Pelabuhan Muat Asal. Lihat Referensi Pelabuhan",

   "message": "Format kode pelabuhan muat sesuai Referensi Pelabuhan"

  },

  "kodePelTujuan": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.25 Pelabuhan Tujuan. Lihat Referensi Pelabuhan",

   "message": "Format kode pelabuhan tujuan sesuai Referensi Pelabuhan"

  },

  "kodePembayar": {

   "type": "string",

   "description": "Keterangan pembayaran apabila memilih Cara Bayar [9] Gabungan/Lainnya",

   "message": "Keterangan pembayaran apabila memilih Cara Bayar [9] Gabungan/Lainnya"

  },

  "kodeTps": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.23 Tempat Penimbunan. Lihat Referensi Tps",

   "message": "Format kode sesuai Referensi Tps"

  },

  "kodeValuta": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.34 Jenis Valuta. Lihat Referensi Valuta",

   "message": "Format kode sesuai Referensi Valuta"

  },

  "kotaTtd": {

   "type": "string",

   "description": "kota tempat pengguna membuat dokumen ekspor",

   "message": "Kota tempat pengguna membuat dokumen ekspor"

  },

  "namaTtd": {

   "type": "string",

   "description": "nama pengguna yang membuat dokumen ekspor",

   "message": "Nama pengguna yang membuat dokumen ekspor"

  },

  "ndpbm": {

   "type": "number",

   "description": "Nilai tukar mata uang rupiah terhadap mata uang asing dalam harga ekspor",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Ndpbm maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "netto": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.43 Berat Bersih (kg)",

   "maxlength": 24,

   "multipleOf": 0.0001,

   "message": "Nilai netto/berat bersih maksimal 24 digit dengan empat angka dibelakang koma"

  },

  "nilaiMaklon": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - F.38 Nilai Maklon / Nilai Jasa Subkon",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Nilai maklon maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "nomorAju": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - Nomor Pengajuan. Nomor pengajuan dokumen pabean 26 digit dengan format 4 digit kode kantor, 2 digit kode dokumen pabean, 6 digit unik perusahaan, 8 digit tanggal pengajuan dengan format YYYYMMDD, 6 digit sequence/nomor urut pengajuan dokumen pabean",

   "pattern": "^[A-Za-z0-9]{26}$",

   "message": "Sesuaikan format nomor pengajuan dokumen ekspor terdiri 26 digit: 4 digit kode kantor, 2 digit kode dokumen pabean, 6 digit unik perusahaan, 8 digit tanggal pengajuan dengan format YYYYMMDD, 6 digit sequence/nomor urut pengajuan dokumen ekspor"

  },

  "seri": {

   "type": "integer",

   "description": "seri dokumen ekspor",

   "message": "seri dokumen ekspor"

  },

  "tanggalAju": {

   "type": "string",

   "format": "date",

   "description": "tanggal pengajuan dokumen pabean dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal pengajuan dokumen: YYYY-MM-DD"

  },

  "tanggalEkspor": {

   "type": "string",

   "format": "date",

   "description": "Sesuai kolom formulir BC 3.0 - F.20 Tanggal Perkiraan Ekspor dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal ekspor: YYYY-MM-DD"

  },

  "tanggalPeriksa": {

   "type": "string",

   "format": "date",

   "description": "tanggal periksa dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal periksa: YYYY-MM-DD"

  },

  "tanggalTtd": {

   "type": "string",

   "format": "date",

   "description": "tanggal penandatanganan dokumen pabean dengan format YYYY-MM-DD",

   "message": "Sesuaikan format tanggal penandatanganan dokumen: YYYY-MM-DD"

  },

  "totalDanaSawit": {

   "type": "number",

   "description": "Sesuai kolom formulir BC 3.0 - Pungutan Sawit (total)",

   "maxlength": 24,

   "multipleOf": 0.01,

   "message": "Total dana sawit maksimal 24 digit dengan dua angka dibelakang koma"

  },

  "flagBarkir": {

   "type": "string",

   "description": "flag barang kiriman [Y] atau non barang kiriman [T]",

   "enum": [

    "Y",

    "T"

   ],

   "message": "Flag barang kiriman: Y untuk barang kiriman atau Y untuk non barang kiriman "

  },

  "kodeJenisPengangkutan": {

   "type": "string",

   "description": "Sesuai kolom formulir BC 3.0 - F.21 Jenis Pengangkutan. Lihat Referensi Jenis Pengangkutan",

   "message": "Format kode sesuai Referensi Jenis Pengangkutan"

  },

  "barang": {

   "type": "array",

   "items": {

     "type": "object",

     "description": "detil data barang dalam satu pengajuan dokumen ekspor",

     "properties": {

      "fob": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 3.0 - F.51 Jumlah Nilai FOB",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "hargaEkspor": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 3.0 - F.47 Harga Ekspor Barang",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "hargaPatokan": {

       "type": "number",

       "description": "harga patokan barang",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "hargaPerolehan": {

       "type": "number",

       "description": "harga perolehan barang",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "hargaSatuan": {

       "type": "number",

       "description": "harga satuan barang",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "jumlahKemasan": {

       "type": "number",

       "description": "jumlah kemasan",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "jumlahSatuan": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 3.0 - F.48 Jumlah Satuan",

       "maxlength": 24,

       "multipleOf": 0.0001

      },

      "kodeAsalBahanBaku": {

       "type": "string",

       "description": "Lihat Referensi Asal Bahan Baku"

      },

      "kodeBarang": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.45 Kode Barang"

      },

      "kodeDaerahAsal": {

       "type": "string",

       "maxlength": 4,

       "description": "Sesuai kolom formulir BC 3.0 - F.50 Daerah Asal Barang"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "set value [30]",

       "const": "30"

      },

      "kodeJenisKemasan": {

       "type": "string",

       "description": "Lihat Referensi Jenis Kemasan"

      },

      "kodeNegaraAsal": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.49 Negara Asal Barang. Lihat Referensi Negara",

       "pattern": "^[A-Z]{2}$"

      },

      "kodeSatuanBarang": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.48 Jenis Satuan Barang. Lihat Referensi Satuan Barang"

      },

      "merk": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.45 Merk Barang"

      },

      "ndpbm": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 3.0 - F.52 Nilai Tukar Mata Uang"

      },

      "netto": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 3.0 - F.48 Berat Bersih (kg)",

       "maxlength": 20,

       "multipleOf": 0.0001

      },

      "nilaiBarang": {

       "type": "number",

       "description": "nilai barang",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "nilaiDanaSawit": {

       "type": "number",

       "description": "Sesuai kolom formulir BC 3.0 - F.55 Pungutan Sawit",

       "maxlength": 24,

       "multipleOf": 0.01

      },

      "posTarif": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.45 Pos Tarif/HS"

      },

      "seriBarang": {

       "type": "integer",

       "description": "Sesuai kolom formulir BC 3.0 - F.44 No. Data Barang Ekspor. Seri data barang"

      },

      "spesifikasiLain": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.45 Spesifikasi Lain"

      },

      "tipe": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.45 Tipe Barang"

      },

      "ukuran": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.45 Ukuran Barang"

      },

      "uraian": {

       "type": "string",

       "decription": "Sesuai kolom formulir BC 3.0 - F.45 Uraian Barang"

      },

      "kodeJenisEkspor": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - B. Jenis Ekspor. Lihat Referensi Jenis Ekspor",

       "message": "Format kode sesuai Referensi Jenis Ekspor"

      },

      "barangTarif": {

       "type": "array",

       "description": "data barang tarif per barang",

       "items": {

         "type": "object",

         "properties": {

          "kodeJenisTarif": {

           "type": "string",

           "description": "Lihat Referensi Jenis Tarif"

          },

          "jumlahSatuan": {

           "type": "number",

           "description": "jumlah satuan barang tarif",

           "maxlength": 20,

           "multipleOf": 0.0001

          },

          "kodeFasilitasTarif": {

           "type": "string",

           "description": "Lihat Referensi Fasilitas Tarif"

          },

          "kodeSatuanBarang": {

           "type": "string",

           "description": "Lihat Referensi Satuan Barang"

          },

          "kodeJenisPungutan": {

           "type": "string",

           "description": "Lihat Referensi Jenis Pungutan"

          },

          "nilaiBayar": {

           "type": "number",

           "description": "nilai bayar barang tarif",

           "maxlength": 24,

           "multipleOf": 0.01

          },

          "seriBarang": {

           "type": "integer",

           "description": "seri barang"

          },

          "tarif": {

           "type": "number",

           "description": "tarif",

           "maxlength": 24,

           "multipleOf": 0.0001

          },

          "tarifFasilitas": {

           "type": "number",

           "description": "tarif fasilitas",

           "maxlength": 5,

           "multipleOf": 0.01

          }

         },

         "required": [

          "jumlahSatuan"

         ]

        }

      },

      "barangDokumen": {

       "type": "array",

       "items": {

        "seriDokumen": {

         "type": "integer",

         "description": "seri dokumen"

        },

        "seriIjin": {

         "type": "integer",

         "description": "seri ijin"

        }

       }

      },

      "barangSpekKhusus": {

       "type": "array",

       "description": "data barang dengan spesifikasi khusus",

       "items": {

         "type": "object",

         "properties": {

          "seriBarangSpekKhusus": {

           "type": "integer",

           "description": "seri barang spesifikasi khusus"

          },

          "kodeSpekKhusus": {

           "type": "integer",

           "description": "Lihat Referensi Spesifikasi Khusus: [3001] Jenis; [3002] Bentuk; [3003] Kadar; [3004] Jenis; [3005] Bentuk; [3006] Jenis; [3007] Jenis",

           "enum": [

            3001,

            3002,

            3003,

            3004,

            3005,

            3006,

            3007

           ]

          },

          "uraianBarangSpekKhusus": {

           "type": "string",

           "description": "uraian barang spesifikasi khusus"

          }

         }

        }

      },

      "barangPemilik": {

       "type": "array",

       "items": {

         "type": "object",

         "properties": {

          "seriEntitas": {

           "type": "integer",

           "description": "seri entitas"

          }

         }

        }

      }

     },

     "required": [

      "fob",

      "hargaPatokan",

      "hargaSatuan",

      "jumlahKemasan",

      "kodeJenisKemasan",

      "merk",

      "posTarif",

      "spesifikasiLain",

      "tipe",

      "uraian",

      "kodeJenisEkspor"

     ]

    }

  },

  "entitas": {

   "type": "array",

   "description": "Sesuai kolom formulir BC 3.0 - F.1-16 Data Perdagangan. Data entitas Eksportir, Pemilik, Penerima, Pembeli, dan PPJK dalam pengajuan dokumen pabean",

   "items": [

    {

     "type": "object",

     "description": "Sesuai kolom formulir BC 3.0 - F.1-4 Eksportir. Data eksportir dalam pengajuan dokumen pabean",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.3 Alamat Eksportir"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas eksportir (2). Mengacu pada Referensi Entitas",

       "const": "2"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.2 Nama Eksportir"

      },

      "nibEntitas": {

       "type": "string",

       "description": "Nomor Induk Berusaha"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.1 Nomor Identitas Eksportir"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeJenisIdentitas",

      "namaEntitas",

      "nomorIdentitas",

      "seriEntitas"

     ]

    },

    {

     "type": "object",

     "description": "Sesuai kolom formulir BC 3.0 - F.5-7 Pemilik Barang. Data pemilik barang dalam pengajuan dokumen pabean",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.7 Alamat Pemilik"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas pemilik (7). Mengacu pada Referensi Entitas",

       "const": "7"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.6 Nama Pemilik"

      },

      "nibEntitas": {

       "type": "string",

       "description": "Nomor Induk Berusaha"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.5 Nomor Identitas Pemilik"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeJenisIdentitas",

      "namaEntitas",

      "nomorIdentitas",

      "seriEntitas"

     ]

    },

    {

     "type": "object",

     "description": "Sesuai kolom formulir BC 3.0 - F.11-13 Penerima. Data penerima barang dalam pengajuan dokumen pabean",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.12 Alamat Penerima"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas Penerima (8). Mengacu pada Referensi Entitas",

       "const": "8"

      },

      "kodeNegara": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.13 Negara. Lihat Referensi Negara",

       "pattern": "(^[A-Z]{2}$)|(^$)"

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.11 Nama Penerima"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeNegara",

      "namaEntitas",

      "seriEntitas"

     ]

    },

    {

     "type": "object",

     "description": "Sesuai kolom formulir BC 3.0 - F.14-16 Pembeli. Data pembeli barang dalam pengajuan dokumen pabean",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.15 Alamat Pembeli"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas Pembeli (6). Mengacu pada Referensi Entitas",

       "const": "6"

      },

      "kodeNegara": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.16 Negara. Lihat Referensi Negara",

       "pattern": "(^[A-Z]{2}$)|(^$)"

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.14 Nama Pembeli"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     },

     "required": [

      "alamatEntitas",

      "kodeEntitas",

      "kodeNegara",

      "namaEntitas",

      "seriEntitas"

     ]

    },

    {

     "type": "object",

     "description": "Sesuai kolom formulir BC 3.0 - F.8-10 PPJK. Data PPJK dalam pengajuan dokumen pabean",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.10 Alamat PPJK"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas PPJK (4). Mengacu pada Referensi Entitas",

       "default": "4"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.9 Nama PPJK"

      },

      "nibEntitas": {

       "type": "string",

       "description": "Nomor Induk Berusaha"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.8 NPWP PPJK"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      }

     }

    },

    {

     "type": "object",

     "description": "Sesuai kolom formulir BC 3.0 - F.8-10 PPJK. Data Pihak Yang Melakukan Konsolidasi dalam pengajuan dokumen pabean",

     "properties": {

      "alamatEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.10 Alamat Konsolidasi"

      },

      "kodeEntitas": {

       "type": "string",

       "description": "Set kode entitas Konsolidator (23). Mengacu pada Referensi Entitas",

       "default": "23"

      },

      "kodeJenisIdentitas": {

       "type": "string",

       "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

       "enum": [

        "2",

        "3",

        "4",

        "5",

        "6"

       ]

      },

      "namaEntitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.9 Nama Pihak Yang Melakukan Konsolidasi"

      },

      "nibEntitas": {

       "type": "string",

       "description": "Nomor Induk Berusaha"

      },

      "nomorIdentitas": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.8 NPWP Pihak Yang Melakukan Konsolidasi"

      },

      "seriEntitas": {

       "type": "integer",

       "description": "seri entitas"

      },

      "kodeKategoriKonsolidator": {

       "type": "string",

       "description": "Lihat Referensi Jenis Konsolidator"

      }

     }

    }

   ]

  },

  "kemasan": {

   "type": "array",

   "description": "data kemasan dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "description": "data kemasan yang digunakan untuk mengemas barang ekspor",

     "properties": {

      "jumlahKemasan": {

       "type": "integer",

       "description": "Sesuai kolom formulir BC 3.0 - F.41 Jumlah Kemasan"

      },

      "kodeJenisKemasan": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.41 Jenis Kemasan. Lihat Referensi Jenis Kemasan"

      },

      "merkKemasan": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.41 Merek Kemasan"

      },

      "seriKemasan": {

       "type": "integer",

       "description": "seri data kemasan berdasarkan data yang dimasukkan"

      }

     },

     "required": [

      "jumlahKemasan",

      "kodeJenisKemasan",

      "merkKemasan",

      "seriKemasan"

     ],

     "message": {

      "required": "Wajib mengisi jumlahKemasan, kodeJenisKemasan, merkKemasan dan seriKemasan"

     }

    }

  },

  "kontainer": {

   "type": "array",

   "description": "data kontainer dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "description": "data peti kemas/kontainer yang digunakan untuk mengangkut barang ekspor, apabila pengangkutan menggunakan peti kemas/kontainer",

     "properties": {

      "kodeJenisKontainer": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.40 Status Peti Kemas. Lihat Referensi Jenis Kontainer"

      },

      "kodeTipeKontainer": {

       "type": "string",

       "description": "Lihat Referensi Tipe Kontainer"

      },

      "kodeUkuranKontainer": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.40 Ukuran Peti Kemas. Kode ukuran kontainer: [20], [40], [45] atau [60]",

       "enum": [

        "20",

        "40",

        "45",

        "60"

       ]

      },

      "nomorKontainer": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.40 Nomor Kontainer"

      },

      "seriKontainer": {

       "type": "integer",

       "description": "seri data kontainer berdasarkan data yang dimasukkan"

      }

     },

     "dependencies": {

      "seriKontainer": [

       "kodeTipeKontainer",

       "kodeUkuranKontainer",

       "nomorKontainer"

      ]

     },

     "message": {

      "dependencies": "Wajib mengisi kodeTipeKontainer, kodeUkuranKontainer, nomorKontainer, dan seriKontainer"

     }

    }

  },

  "dokumen": {

   "type": "array",

   "description": "data dokumen pelengkap dalam pengajuan dokumen pabean",

   "items": [

    {

     "type": "object",

     "description": "data invoice sebagai dokumen pelengkap",

     "properties": {

      "idDokumen": {

       "type": "string",

       "description": "ID Dokumen"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "Set kode dokumen invoice (380)",

       "const": "380"

      },

      "kodeFasilitas": {

       "type": "string",

       "description": "Lihat Referensi Fasilitas"

      },

      "kodeIjin": {

       "type": "string",

       "description": "Lihat Referensi Ijin"

      },

      "nomorDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.27 Nomor Invoice"

      },

      "seriDokumen": {

       "type": "integer",

       "description": "seri dokumen pelengkap pabean"

      },

      "tanggalDokumen": {

       "type": "string",

       "format": "date",

       "description": "Sesuai kolom formulir BC 3.0 - F.27 Tanggal Invoice dengan format YYYY-MM-DD"

      },

      "urlDokumen": {

       "type": "string",

       "description": "url dokumen invoice"

      }

     },

     "required": [

      "kodeDokumen",

      "nomorDokumen",

      "seriDokumen",

      "tanggalDokumen"

     ],

     "message": {

      "required": "Wajib mengisi kodeDokumen, nomorDokumen, seriDokumen, dan tanggalDokumen Invoice"

     }

    },

    {

     "type": "object",

     "description": "data packing list sebagai dokumen pelengkap",

     "properties": {

      "idDokumen": {

       "type": "string",

       "description": "ID Dokumen"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "Set kode dokumen packing list (217)",

       "const": "217"

      },

      "kodeFasilitas": {

       "type": "string",

       "description": "Lihat Referensi Fasilitas"

      },

      "kodeIjin": {

       "type": "string",

       "description": "Lihat Referensi Ijin"

      },

      "nomorDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.28 Nomor Packing List"

      },

      "seriDokumen": {

       "type": "integer",

       "description": "seri dokumen pelengkap pabean"

      },

      "tanggalDokumen": {

       "type": "string",

       "format": "date",

       "description": "Sesuai kolom formulir BC 3.0 - F.28 Tanggal Packing List dengan format YYYY-MM-DD"

      },

      "urlDokumen": {

       "type": "string",

       "description": "url dokumen packing list (217)"

      }

     },

     "required": [

      "kodeDokumen",

      "nomorDokumen",

      "seriDokumen",

      "tanggalDokumen"

     ],

     "message": {

      "required": "Wajib mengisi kodeDokumen, nomorDokumen, seriDokumen, dan tanggalDokumen Packing List"

     }

    },

    {

     "type": "object",

     "description": "data dokumen pelengkap lainnya dalam pengajuan dokumen ekspor",

     "properties": {

      "idDokumen": {

       "type": "string",

       "description": "ID Dokumen"

      },

      "kodeDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.29 Jenis Dokumen Lainnya. Lihat Referensi Dokumen"

      },

      "kodeFasilitas": {

       "type": "string",

       "description": "Lihat Referensi Fasilitas"

      },

      "kodeIjin": {

       "type": "string",

       "description": "Lihat Referensi Ijin"

      },

      "nomorDokumen": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.29 Nomor Dokumen Pelengkap Lainnya"

      },

      "seriDokumen": {

       "type": "integer",

       "description": "seri dokumen pelengkap pabean"

      },

      "tanggalDokumen": {

       "type": "string",

       "format": "date",

       "description": "Sesuai kolom formulir BC 3.0 - F.29 Tanggal Dokumen Pelengkap Lainnya dengan format YYYY-MM-DD"

      },

      "urlDokumen": {

       "type": "string",

       "description": "url dokumen Nomor Dokumen Pelengkap Lainnya"

      }

     },

     "dependencies": {

      "seriDokumen": [

       "kodeDokumen",

       "nomorDokumen",

       "tanggalDokumen"

      ]

     },

     "message": {

      "dependencies": "Jika terdapat seriDokumen Dokumen Pelengkap lainnya, maka wajib mengisi kodeDokumen, nomorDokumen, dan tanggalDokumen Dokumen Pelengkap Lainnya "

     }

    }

   ]

  },

  "pengangkut": {

   "type": "array",

   "description": "data pengangkutan dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "properties": {

      "kodeBendera": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.18 Bendera Sarana Pengangkut. Lihat Referensi Bendera"

      },

      "namaPengangkut": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.18 Nama Sarana Pengangkut"

      },

      "nomorPengangkut": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.19 Nomor Pengangkut"

      },

      "kodeCaraAngkut": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.17 Cara Pengangkutan. Lihat Referensi Cara Angkut"

      },

      "caraPengangkutanLainnya": {

       "type": "string",

       "description": "Diisi Ketika kodeJenisPengangkutan 6-SARANA ANGKUT LAINNYA"

      },

      "seriPengangkut": {

       "type": "integer",

       "description": "seri data pengangkut"

      }

     },

     "required": [

      "kodeBendera",

      "namaPengangkut",

      "nomorPengangkut",

      "kodeCaraAngkut",

      "seriPengangkut"

     ],

     "message": {

      "required": "Wajib mengisi kodeBendera, namaPengangkut, nomorPengangkut, kodeCaraAngkut, dan seriPengangkut"

     }

    }

  },

  "bankDevisa": {

   "type": "array",

   "description": "data bank devisa hasil ekspor",

   "items": {

     "type": "object",

     "properties": {

      "kodeBank": {

       "type": "string",

       "description": "Sesuai kolom formulir BC 3.0 - F.33 Lihat Referensi Bank"

      },

      "namaBank": {

       "type": "string",

       "description": "nama bank devisa"

      },

      "seriBank": {

       "type": "integer",

       "description": "seri bank devisa"

      }

     }

    }

  },

  "kesiapanBarang": {

   "type": "array",

   "description": "kesiapan barang dalam pengajuan dokumen pabean",

   "items": {

     "type": "object",

     "properties": {

      "kodeJenisBarang": {

       "type": "string",

       "description": "Jenis Barang: [1] Barang Ekspor Gabungan; [2] Bahan/Barang Asal Impor Fasilitas",

       "enum": [

        "1",

        "2"

       ]

      },

      "kodeJenisGudang": {

       "type": "string",

       "description": "Jenis Gudang: [1] Gudang Veem; [2] Gudang Pabrik; [3] Gudang Konsolidasi; [4] Lainnya",

       "enum": [

        "1",

        "2",

        "3",

        "4"

       ]

      },

      "namaPic": {

       "type": "string",

       "description": "nama person in charge"

      },

      "alamat": {

       "type": "string",

       "description": "alamat barang siap diperiksa"

      },

      "nomorTelpPic": {

       "type": "string",

       "description": "nomor telpon person in charge"

      },

      "jumlahContainer20": {

       "type": "integer",

       "description": "jumlah kontainer 20 feet"

      },

      "jumlahContainer40": {

       "type": "integer",

       "description": "jumlah kontainer 40 feet"

      },

      "lokasiSiapPeriksa": {

       "type": "string",

       "description": "lokasi siap periksa"

      },

      "kodeCaraStuffing": {

       "type": "string",

       "description": "cara stuffing: [4] Empty; [7] LCL; [8] FCL",

       "enum": [

        "4",

        "7",

        "8"

       ]

      },

      "kodeJenisPartOf": {

       "type": "string",

       "description": "jenis part of: [1] Gabungan kemudahan ekspor; [2] Gabungan ke/non ke",

       "enum": [

        "1",

        "2",

        "",

        "NULL",

        null

       ]

      },

      "tanggalPkb": {

       "type": "string",

       "format": "date",

       "description": "tanggal pemeriksaan kesiapan barang"

      },

      "waktuSiapPeriksa": {

       "type": "string",

       "description": "waktu barang siap periksa dengan format YYYY-MM-DDThh:mm:ss.sTZD",

       "format": "date-time"

      }

     },

     "required": [

      "kodeJenisGudang",

      "namaPic",

      "alamat",

      "nomorTelpPic",

      "lokasiSiapPeriksa",

      "tanggalPkb",

      "waktuSiapPeriksa"

     ]

    }

  }

 },

 "required": [

  "asuransi",

  "bruto",

  "flagBarkir",

  "flagMigas",

  "fob",

  "freight",

  "jabatanTtd",

  "jumlahKontainer",

  "kodeAsuransi",

  "kodeCaraBayar",

  "kodeJenisEkspor",

  "kodeJenisPengangkutan",

  "kodeKantor",

  "kodeKantorEkspor",

  "kodeKantorMuat",

  "kodeKategoriEkspor",

  "kodeLokasi",

  "kodePelEkspor",

  "kodePelMuat",

  "kodePelTujuan",

  "kodeValuta",

  "kotaTtd",

  "namaTtd",

  "ndpbm",

  "netto",

  "nomorAju",

  "tanggalPeriksa",

  "tanggalTtd",

  "barang",

  "entitas",

  "kemasan",

  "dokumen",

  "pengangkut",

  "bankDevisa",

  "kesiapanBarang"

 ],

 "message": {

  "required": "Wajib mengisi asuransi, bruto, flagBarkir, flagMigas, fob, freight, jabatanTtd, jumlahKontainer, kodeAsuransi, kodeCaraBayar, kodeJenisEkspor, kodeJenisPengangkutan, kodeKantor, kodeKategoriEkspor, kodeLokasi, kodePelMuat, kodePelTujuan, kodeValuta, kotaTtd, namaTtd, ndpbm, netto, nomorAju, tanggalPeriksa, tanggalTtd, barang, entitas, kemasan, dokumen, pengangkut, bankDevisa, dan kesiapanBarang"

 },

 "allOf": [

  {

   "if": {

    "properties": {

     "kodeCaraBayar": {

      "const": "9"

     }

    },

    "required": [

     "kodeCaraBayar"

    ]

   },

   "then": {

    "required": [

     "kodePembayar"

    ]

   }

  },

  {

   "if": {

    "properties": {

     "flagBarkir": {

      "const": "T"

     }

    },

    "required": [

     "flagBarkir"

    ]

   },

   "then": {

    "required": [

     "flagCurah"

    ]

   }

  }

 ]

}
```
## BC 3.0 - Payload
```json
{

  "status": false,

  "message": null,

  "idHeader": null,

  "asalData": "S",

  "asuransi": 300395.95,

  "bruto": 4666,

  "cif": 0,

  "disclaimer": null,

  "email": null,

  "kodeJenisProsedur": null,

  "kodeJenisPlb": null,

  "kodeJenisTpb": null,

  "kodeJenisImpor": null,

  "kodeJenisEkspor": "1",

  "kodeKantorPeriksa": "020400",

  "tanggalEkspor": "2026-04-22",

  "roleEntitas": null,

  "jumlahNetto": null,

  "jumlahCif": null,

  "jumlahVolume": null,

  "jumlahHargaPenyerahan": null,

  "jumlahFob": null,

  "jumlahBruto": null,

  "jumlahNilaiVd": null,

  "flagCurah": "2",

  "flagVd": null,

  "fob": 146375000,

  "freight": 2320245,

  "hargaPenyerahan": 0,

  "idPengguna": null,

  "idPelmuatAkhir": null,

  "idPerusahaan": null,

  "jabatanTtd": "PPJK",

  "jatuhTempoBilling": null,

  "jumlahKontainer": 0,

  "jumlahTandaPengaman": null,

  "kodeAsalBarangFtz": null,

  "kodeAsuransi": "DN",

  "kodeBank": null,

  "kodeBilling": null,

  "kodeCaraAngkutPlb": null,

  "kodeCaraBayar": "10",

  "kodeCaraDagang": "15",

  "kodeDaerahAsal": null,

  "kodeDokumen": "30",

  "kodeFaktur": null,

  "kodeGudangAsal": null,

  "kodeGudangTujuan": null,

  "kodeIncoterm": "FOB",

  "kodeJenisKirim": null,

  "kodeJenisPengiriman": null,

  "kodeJenisNilai": null,

  "kodeKantor": "020400",

  "kodeKantorBongkar": null,

  "kodeKantorTujuan": null,

  "kodeKantorEkspor": "020400",

  "kodeKategoriBarangFtz": null,

  "kodeKategoriEkspor": "10",

  "kodeKategoriKeluarFtz": null,

  "kodeKategoriMasukFtz": null,

  "kodeLokasi": "3",

  "kodeLokasiBayar": null,

  "kodeNegaraTujuan": "SG",

  "kodePelBongkar": "SGJUR",

  "kodePelMuat": "IDBPD",

  "kodePelTransit": null,

  "kodePelTujuan": "SGJUR",

  "kodePelEkspor": "IDBPD",

  "kodePembayar": null,

  "kodeTps": "PS01",

  "kodeTujuanPemasukan": null,

  "kodeTujuanPengiriman": null,

  "kodeTujuanTpb": null,

  "kodeTutupPu": null,

  "kodeValuta": "IDR",

  "kotaTtd": "BATAM",

  "lokasiAsal": null,

  "lokasiTujuan": null,

  "namaTransaksiLainnyaFtz": null,

  "namaTtd": "nama_ttd",

  "ndpbm": 1,

  "netto": 4281,

  "nik": "1266000101767",

  "nilaiBarang": 0,

  "npwpPemusatan": null,

  "nilaiIncoterm": null,

  "nilaiMaklon": 0,

  "nomorAju": "nomor_aju",

  "nomorBc11": null,

  "npppjk": null,

  "npwpBilling": null,

  "posBc11": null,

  "seri": 0,

  "subposBc11": null,

  "kodeJenisTandaPengaman": null,

  "tanggalStuffing": null,

  "tanggalAju": "2026-05-04",

  "tanggalBc11": null,

  "tanggalBerangkat": null,

  "tanggalBilling": null,

  "tanggalIjinPenerima": null,

  "tanggalIjinPengusaha": null,

  "tanggalMasuk": null,

  "tanggalMuat": null,

  "tanggalNpppjk": null,

  "tanggalTiba": null,

  "tanggalTtd": "2026-05-08",

  "tanggalPeriksa": "2026-04-22",

  "tempatStuffing": null,

  "totalDanaSawit": null,

  "urlDokumen": null,

  "userPortal": null,

  "versiModul": null,

  "volume": 0,

  "kodeKantorMuat": "020400",

  "nipRekam": null,

  "kodeKenaPajak": null,

  "uangMuka": null,

  "dasarPengenaanPajak": null,

  "nilaiJasa": null,

  "flagMigas": "2",

  "namaIncoterm": null,

  "namaJenisNilai": null,

  "namaValuta": null,

  "nilaiKurs": null,

  "tglAwalBerlaku": null,

  "tglAkhirBerlaku": null,

  "namaPelabuhanTujuan": null,

  "namaPelabuhanMuat": null,

  "namaPelabuhanBongkar": null,

  "namaJenisProsedur": null,

  "namaJenisImpor": null,

  "namaCaraBayar": null,

  "namaKantorTujuan": null,

  "namaKantorMuat": null,

  "namaKantorBongkar": null,

  "namaJenisTpb": null,

  "biayaTambahan": 0,

  "biayaPengurang": 0,

  "vd": null,

  "namaKantorPendek": null,

  "nomorDaftar": null,

  "namaPpjk": null,

  "idPpjk": null,

  "namaPerusahaan": null,

  "tanggalDaftar": null,

  "namaProses": null,

  "ttBarang": null,

  "flagPph": null,

  "barang": [

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 2000000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 20000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 5,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 100,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 100,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 6,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "uraian_barang",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 42000000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 35000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 16,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 1200,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 1200,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "13019090",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 1,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN KACI",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [

        {

          "idBarangTarif": "id_Barang_Tarif",

          "idHeader": "id_Header",

          "idBarang": "id_Barang",

          "idBahanBaku": null,

          "flagBmtSementara": null,

          "flagTis": null,

          "flagPelekatan": null,

          "kodeJenisTarif": "2",

          "jumlahSatuan": 1200,

          "kodeAsalBahanBaku": null,

          "kodeFasilitasTarif": "1",

          "kodeKomoditiCukai": null,

          "kodeSatuanBarang": "TNE",

          "kodeSatuanTarif": null,

          "jumlahKemasan": null,

          "kodeKemasan": null,

          "kodeSubKomoditiCukai": null,

          "kodeJenisPungutan": "BK",

          "nilaiBayar": 6000,

          "nilaiFasilitas": null,

          "nilaiSudahDilunasi": null,

          "seriBarang": 1,

          "tarif": 5,

          "tarifTerkecil": null,

          "tarifFasilitas": 100,

          "namaFasilitasTarif": null,

          "cukaiCount": null,

          "kodeTarif": null

        }

      ],

      "barangDokumen": [],

      "barangSpekKhusus": [

        {

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idBarangSpekKhusus": "id_Barang_Spek_Khusus",

          "kodeSpekKhusus": 3001,

          "uraianBarangSpekKhusus": "13019090AB",

          "namaSpekKhusus": null

        }

      ],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 6000000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 6000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 2,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 1000,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "PCE",

      "merk": "-",

      "namaEksportir": null,

      "netto": 50,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03063910",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 12,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "LOBSTER AIR TAWAR",

      "volume": null,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 1050000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 7000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 2,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 150,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "PCE",

      "merk": "-",

      "namaEksportir": null,

      "netto": 30,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03063311",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 15,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "RAJUNGAN",

      "volume": null,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 1500000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 75000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 1,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 20,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 20,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 3,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN KERAPU",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 3600000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 15000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 2,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 240,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "PCE",

      "merk": "-",

      "namaEksportir": null,

      "netto": 40,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03063629",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 11,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "UDANG BELALANG",

      "volume": null,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 1600000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 20000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 4,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 80,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 80,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 7,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN MANYUNG",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 900000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 75000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 1,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 12,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "PCE",

      "merk": "-",

      "namaEksportir": null,

      "netto": 6,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03063120",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 14,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "LOBSTER",

      "volume": null,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 1500000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 75000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 1,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 20,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 20,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 9,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN KAKAP MERAH",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 1600000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 20000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 4,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 80,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 80,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 4,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN DINGKIS",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 2800000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 20000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 7,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 140,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 140,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 5,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN TIMUN",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 39375000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 35000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 15,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 1125,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 1125,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 2,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN KETARAP",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 1600000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 20000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 4,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 80,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "KGM",

      "merk": "-",

      "namaEksportir": null,

      "netto": 80,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03028919",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 8,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "IKAN AYAM AYAM",

      "volume": 0,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 2000000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 10000,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 4,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 200,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "PCE",

      "merk": "-",

      "namaEksportir": null,

      "netto": 200,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03071110",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 13,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "GONG GONG",

      "volume": null,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    },

    {

      "uangMuka": null,

      "nilaiJasa": null,

      "idBarang": "id_Barang",

      "idHeader": null,

      "asuransi": null,

      "bruto": null,

      "cif": 0,

      "diskon": 0,

      "flagTis": null,

      "kodeJenisTpb": null,

      "fob": 38850000,

      "freight": null,

      "hargaEkspor": 0,

      "hargaPatokan": null,

      "hargaPenyerahan": 0,

      "jumlahNetto": null,

      "jumlahCif": null,

      "jumlahVolume": null,

      "jumlahHargaPenyerahan": null,

      "jumlahFob": null,

      "jumlahBruto": null,

      "hargaSatuan": 17500,

      "hjeCukai": null,

      "identitasEksportir": null,

      "isiPerKemasan": 0,

      "jatuhTempoRoyalti": null,

      "jumlahBahanBaku": null,

      "jumlahDilekatkan": null,

      "jumlahKemasan": 37,

      "jumlahPitaCukai": null,

      "jumlahRealisasi": null,

      "jumlahSatuan": 2220,

      "kapasitasSilinder": null,

      "kodeAsalBarang": null,

      "kodeBarang": "-",

      "kodeDaerahAsal": "2171",

      "kodeGunaBarang": null,

      "kodeDokumen": "30",

      "kodeJenisBkc": null,

      "kodeJenisNilai": null,

      "kodeKategoriBarang": null,

      "kodeJenisKemasan": "CH",

      "kodeKomoditiBkc": null,

      "kodeSubKomoditiBkc": null,

      "kodeKondisiBarang": null,

      "kodeLokasiBayar": null,

      "kodeNegaraAsal": "ID",

      "kodePerhitungan": null,

      "kodeSatuanBarang": "PCE",

      "merk": "-",

      "namaEksportir": null,

      "netto": 1110,

      "nilaiBarang": 0,

      "nilaiDanaSawit": null,

      "nilaiDevisa": null,

      "nilaiTambah": 0,

      "pernyataanLartas": null,

      "flag4tahun": null,

      "persentaseImpor": null,

      "posTarif": "03063311",

      "saldoAkhir": null,

      "saldoAwal": null,

      "seriBarang": 10,

      "seriBarangDokAsal": null,

      "seriIjin": null,

      "spesifikasiLain": "-",

      "tahunPembuatan": null,

      "tarifCukai": null,

      "nilaiKurs": null,

      "tipe": "-",

      "ukuran": "-",

      "uraian": "KEPITING",

      "volume": null,

      "waktuRekam": null,

      "namaKemasan": null,

      "namaSatuanBarang": null,

      "cifRp": null,

      "nilaiCukai": null,

      "dokTpb": null,

      "namaFasilitasTarif": null,

      "idBarangJadi": null,

      "ndpbm": 1,

      "cifRupiah": 0,

      "hargaPerolehan": 0,

      "kodeAsalBahanBaku": "2",

      "kodeDokAsal": null,

      "kodeKantorAsal": null,

      "nomorAjuDokAsal": null,

      "nomorDaftarDokAsal": null,

      "tanggalDaftarDokAsal": null,

      "barangTarif": [],

      "barangDokumen": [],

      "barangSpekKhusus": [],

      "barangVd": [],

      "barangPemilik": [

        {

          "idBarangPemilik": "id_Barang_Pemilik",

          "idBarang": "id_Barang",

          "seriBarang": null,

          "idEntitas": null,

          "idPemilik": "id_Pemilik",

          "alamatEntitas": null,

          "kodeEntitas": null,

          "kodeJenisApi": null,

          "kodeJenisIdentitas": null,

          "kodeNegara": null,

          "kodeStatus": null,

          "namaEntitas": null,

          "seriEntitas": null,

          "nibEntitas": null,

          "niperEntitas": null,

          "nomorIdentitas": null,

          "nomorIjinEntitas": null,

          "namaNegara": null,

          "namaJenisApi": null,

          "namaJenisIdentitas": null,

          "nomorApi": null

        }

      ],

      "bahanBaku": [],

      "metodePenentuanNilai": null,

      "alasanMetodePenentuanNilai": null,

      "statementPerbedaanHarga": null,

      "kodeJenisEkspor": "1"

    }

  ],

  "entitas": [

    {

      "idEntitas": null,

      "idHeader": null,

      "alamatEntitas": "alamat_Entitas",

      "kodeEntitas": "2",

      "kodeJenisApi": "02",

      "kodeJenisIdentitas": "6",

      "kodeNegara": null,

      "kodeStatus": "LAINNYA",

      "namaEntitas": "nama_entitas",

      "nibEntitas": "nib_entitas",

      "niperEntitas": null,

      "nomorIdentitas": "nomor_identitas",

      "nomorIjinEntitas": null,

      "tanggalIjinEntitas": null,

      "namaNegara": null,

      "namaJenisApi": null,

      "namaJenisIdentitas": null,

      "nomorApi": null,

      "seriEntitas": 2,

      "seriEntitasOld": null,

      "kodeAfiliasi": null,

      "npwp16": "npwp_16",

      "kodeKategoriKonsolidator": null

    },

    {

      "idEntitas": null,

      "idHeader": null,

      "alamatEntitas": "alamat_Entitas",

      "kodeEntitas": "4",

      "kodeJenisApi": null,

      "kodeJenisIdentitas": "6",

      "kodeNegara": null,

      "kodeStatus": null,

      "namaEntitas": "nama_entitas",

      "nibEntitas": "nib_entitas",

      "niperEntitas": null,

      "nomorIdentitas": "nomor_identitas",

      "nomorIjinEntitas": null,

      "tanggalIjinEntitas": null,

      "namaNegara": null,

      "namaJenisApi": null,

      "namaJenisIdentitas": null,

      "nomorApi": null,

      "seriEntitas": 4,

      "seriEntitasOld": null,

      "kodeAfiliasi": null,

      "npwp16": "npwp_16",

      "kodeKategoriKonsolidator": null

    },

    {

      "idEntitas": null,

      "idHeader": null,

      "alamatEntitas": "alamat_Entitas",

      "kodeEntitas": "6",

      "kodeJenisApi": null,

      "kodeJenisIdentitas": null,

      "kodeNegara": "SG",

      "kodeStatus": null,

      "namaEntitas": "nama_entitas",

      "nibEntitas": "nib_entitas",

      "niperEntitas": null,

      "nomorIdentitas": null,

      "nomorIjinEntitas": null,

      "tanggalIjinEntitas": null,

      "namaNegara": null,

      "namaJenisApi": null,

      "namaJenisIdentitas": null,

      "nomorApi": null,

      "seriEntitas": 6,

      "seriEntitasOld": null,

      "kodeAfiliasi": null,

      "npwp16": null,

      "kodeKategoriKonsolidator": null

    },

    {

      "idEntitas": null,

      "idHeader": null,

      "alamatEntitas": "alamat_Entitas",

      "kodeEntitas": "8",

      "kodeJenisApi": null,

      "kodeJenisIdentitas": null,

      "kodeNegara": "SG",

      "kodeStatus": null,

      "namaEntitas": "nama_entitas",

      "nibEntitas": "nib_entitas",

      "niperEntitas": null,

      "nomorIdentitas": null,

      "nomorIjinEntitas": null,

      "tanggalIjinEntitas": null,

      "namaNegara": null,

      "namaJenisApi": null,

      "namaJenisIdentitas": null,

      "nomorApi": null,

      "seriEntitas": 8,

      "seriEntitasOld": null,

      "kodeAfiliasi": null,

      "npwp16": null,

      "kodeKategoriKonsolidator": null

    },

    {

      "idEntitas": null,

      "idHeader": null,

      "alamatEntitas": "alamat_Entitas",

      "kodeEntitas": "10",

      "kodeJenisApi": null,

      "kodeJenisIdentitas": null,

      "kodeNegara": null,

      "kodeStatus": null,

      "namaEntitas": "nama_entitas",

      "nibEntitas": "nib_entitas",

      "niperEntitas": null,

      "nomorIdentitas": null,

      "nomorIjinEntitas": null,

      "tanggalIjinEntitas": null,

      "namaNegara": null,

      "namaJenisApi": null,

      "namaJenisIdentitas": null,

      "nomorApi": null,

      "seriEntitas": 10,

      "seriEntitasOld": null,

      "kodeAfiliasi": null,

      "npwp16": null,

      "kodeKategoriKonsolidator": null

    },

    {

      "idEntitas": null,

      "idHeader": null,

      "alamatEntitas": "alamat_Entitas",

      "kodeEntitas": "7",

      "kodeJenisApi": "02",

      "kodeJenisIdentitas": "6",

      "kodeNegara": null,

      "kodeStatus": "LAINNYA",

      "namaEntitas": "nama_entitas",

      "nibEntitas": "nib_entitas",

      "niperEntitas": null,

      "nomorIdentitas": "nomor_identitas",

      "nomorIjinEntitas": null,

      "tanggalIjinEntitas": null,

      "namaNegara": null,

      "namaJenisApi": null,

      "namaJenisIdentitas": null,

      "nomorApi": null,

      "seriEntitas": 13,

      "seriEntitasOld": null,

      "kodeAfiliasi": null,

      "npwp16": "npwp_16",

      "kodeKategoriKonsolidator": null

    }

  ],

  "kemasan": [

    {

      "idKemasan": null,

      "idHeader": null,

      "jumlahKemasan": 105,

      "kesesuaianDokumen": null,

      "keterangan": null,

      "kodeJenisKemasan": "PK",

      "latitude": null,

      "longitude": null,

      "merkKemasan": "TANPA MEREK",

      "nomorPolisi": null,

      "nomorPolisiGateMandiri": null,

      "nomorSegel": null,

      "nomorSegelGateMandiri": null,

      "seriKemasan": 1,

      "urlImage": null,

      "nipGateIn": null,

      "waktuGateIn": null,

      "nipGateOut": null,

      "waktuGateOut": null,

      "nipNotifTpb": null,

      "waktuNotifTpb": null,

      "waktuRekamGateMandiri": null,

      "namaKemasan": null,

      "fileType": null

    }

  ],

  "kontainer": [],

  "dokumen": [

    {

      "idBarangDokumen": null,

      "idBarang": null,

      "seriIjin": null,

      "idDokumen": "id_dokumen",

      "idHeader": null,

      "flagSudahDipenuhi": null,

      "flagTerima": null,

      "kodeDokumen": "217",

      "kodeFasilitas": null,

      "kodeIjin": null,

      "nomorDokumen": "nomor_dokumen",

      "seriDokumen": 2,

      "seriBarang": null,

      "tanggalDokumen": "2026-04-22",

      "urlDokumen": null,

      "waktuTerimaHc": null,

      "namaDokumen": null,

      "namaFasilitas": null,

      "namaIjin": null,

      "kodeKantor": null,

      "fileType": null,

      "catatan": null,

      "keterangan": null,

      "waktuTerimaRespon": null,

      "waktuRespon": null,

      "idDokumenRespon": null

    },

    {

      "idBarangDokumen": null,

      "idBarang": null,

      "seriIjin": null,

      "idDokumen": "id_dokumen",

      "idHeader": null,

      "flagSudahDipenuhi": null,

      "flagTerima": null,

      "kodeDokumen": "380",

      "kodeFasilitas": null,

      "kodeIjin": null,

      "nomorDokumen": "nomor_dokumen",

      "seriDokumen": 1,

      "seriBarang": null,

      "tanggalDokumen": "2026-04-22",

      "urlDokumen": null,

      "waktuTerimaHc": null,

      "namaDokumen": null,

      "namaFasilitas": null,

      "namaIjin": null,

      "kodeKantor": null,

      "fileType": null,

      "catatan": null,

      "keterangan": null,

      "waktuTerimaRespon": null,

      "waktuRespon": null,

      "idDokumenRespon": null

    },

    {

      "idBarangDokumen": null,

      "idBarang": null,

      "seriIjin": null,

      "idDokumen": "id_dokumen",

      "idHeader": null,

      "flagSudahDipenuhi": null,

      "flagTerima": null,

      "kodeDokumen": "705",

      "kodeFasilitas": null,

      "kodeIjin": null,

      "nomorDokumen": "nomor_dokumen",

      "seriDokumen": 3,

      "seriBarang": null,

      "tanggalDokumen": "2026-04-22",

      "urlDokumen": null,

      "waktuTerimaHc": null,

      "namaDokumen": null,

      "namaFasilitas": null,

      "namaIjin": null,

      "kodeKantor": null,

      "fileType": null,

      "catatan": null,

      "keterangan": null,

      "waktuTerimaRespon": null,

      "waktuRespon": null,

      "idDokumenRespon": null

    },

    {

      "idBarangDokumen": null,

      "idBarang": null,

      "seriIjin": null,

      "idDokumen": "id_dokumen",

      "idHeader": null,

      "flagSudahDipenuhi": null,

      "flagTerima": null,

      "kodeDokumen": "951",

      "kodeFasilitas": null,

      "kodeIjin": null,

      "nomorDokumen": "nomor_dokumrn







 "seriDokumen": 5,

      "seriBarang": null,

      "tanggalDokumen": "2026-04-22",

      "urlDokumen": null,

      "waktuTerimaHc": null,

      "namaDokumen": null,

      "namaFasilitas": null,

      "namaIjin": null,

      "kodeKantor": null,

      "fileType": null,

      "catatan": null,

      "keterangan": null,

      "waktuTerimaRespon": null,

      "waktuRespon": null,

      "idDokumenRespon": null

    },

    {

      "idBarangDokumen": null,

      "idBarang": null,

      "seriIjin": null,

      "idDokumen": "id_dokumen",

      "idHeader": null,

      "flagSudahDipenuhi": null,

      "flagTerima": null,

      "kodeDokumen": "951",

      "kodeFasilitas": null,

      "kodeIjin": null,

      "nomorDokumen": "nomor_dokumen







 "seriDokumen": 4,

      "seriBarang": null,

      "tanggalDokumen": "2026-04-22",

      "urlDokumen": null,

      "waktuTerimaHc": null,

      "namaDokumen": null,

      "namaFasilitas": null,

      "namaIjin": null,

      "kodeKantor": null,

      "fileType": null,

      "catatan": null,

      "keterangan": null,

      "waktuTerimaRespon": null,

      "waktuRespon": null,

      "idDokumenRespon": null

    }

  ],

  "jaminan": null,

  "pemilik": null,

  "pengangkut": [

    {

      "idPengangkut": null,

      "idHeader": null,

      "kodeBendera": "ID",

      "namaPengangkut": "nama_pengangkut







 "nomorPengangkut": "nomor_pengangkut







 "kodeCaraAngkut": "1",

      "seriPengangkut": 1,

      "callSign": null,

      "tanggalBc11": null,

      "tanggalTiba": null,

      "nomorBc11": null,

      "posBc11": null,

      "subPosBc11": null,

      "kodePelabuhanMuat": null,

      "kodePelabuhanTransit": null,

      "kodePelabuhanTujuan": null,

      "kodeKantor": null,

      "kodeNegaraTujuan": null,

      "kodePelabuhanBongkar": null,

      "kodeTps": null,

      "namaPelabuhan": null,

      "namaNegara": null,

      "namaPelMuat": null,

      "namaPelTransit": null,

      "namaPelTujuan": null,

      "namaTpsWajib": null,

      "kodeCaraAngkutPlb": null,

      "namaPelabuhanBongkar": null,

      "caraPengangkutanLainnya": null

    }

  ],

  "bankDevisa": [],

  "kesiapanBarang": [],

  "pungutan": [

    {

      "idPungutan": "id_pungutan" 







 "idHeader": "id_header",

      "idBarang": null,

      "kodeFasilitasTarif": "1",

      "kodeJenisPungutan": "BK",

      "nilaiPungutan": 6000,

      "nilaiBayar": null,

      "nilaiFasilitas": null,

      "nilaiSudahDilunasi": null,

      "npwpBilling": null

    }

  ],

  "flagBarkir": "T",

  "flagKonsol": null,

  "kodeJenisPengangkutan": "1"

}
```
## BC 3.3 - Schema
```json
{

  "$schema": "http://json-schema.org/draft-07/schema",

  "type": "object",

  "title": "Schema Kirim Dokumen BC 33",

  "description": "JSON Schema untuk Kirim Dokumen Pabean v.0.4. Terdiri atas data header dan data barang. Data header merupakan data umum dokumen pabean sedangkan data barang merupakan data detil atas barang pada dokumen pabean",

  "properties": {

    "asalData": {

      "type": "string",

      "description": "set value [S]",

      "const": "S",

      "message": "Asal pengiriman data secara Host to Host: S"

    },

    "asuransi": {

      "type": "number",

      "description": "Nilai Asuransi",

      "maxlength": 24,

      "multipleOf": 0.01,

      "message": "Nilai asuransi maksimal 24 digit dengan dua angka dibelakang koma"

    },

    "bruto": {

      "type": "number",

      "description": "Sesuai kolom formulir BC 3.3 - H.46 Berat Kotor (kg)",

      "maxlength": 24,

      "multipleOf": 0.0001,

      "message": "Nilai bruto maksimal 24 digit dengan empat angka dibelakang koma"

    },

    "cif": {

      "type": "number",

      "description": "Sesuai kolom formulir BC 3.3 - H.33 Nilai Barang",

      "maxlength": 24,

      "multipleOf": 0.01,

      "message": "Nilai cif maksimal 24 digit dengan dua angka dibelakang koma"

    },

    "disclaimer": {

      "type": "string",

      "description": "Persetujuan pengguna dalam kirim dokumen pabean: [1] Ya atau [0] Tidak",

      "enum": [

        "0",

        "1"

      ],

      "message": "Persetujuan pengguna dalam kirim dokumen pabean: 1 untuk Ya atau 0 untuk Tidak"

    },

    "flagCurah": {

      "type": "string",

      "description": "flag barang curah [1] atau non curah [2]",

      "enum": [

        "1",

        "2"

      ],

      "message": "Flag barang curah: 1 untuk barang curah atau 2 untuk barang non curah "

    },

    "freight": {

      "type": "number",

      "description": "Nilai Freight",

      "maxlength": 24,

      "multipleOf": 0.01,

      "message": "Nilai freight maksimal 24 digit dengan dua angka dibelakang koma"

    },

    "jabatanTtd": {

      "type": "string",

      "description": "Jabatan pengguna yang mengajukan dokumen BC 3.3",

      "message": "Jabatan pengguna yang mengajukan dokumen BC 3.3"

    },

    "jumlahKontainer": {

      "type": "integer",

      "description": "Sesuai kolom formulir BC 3.3 - H.43 Jumlah Peti Kemas",

      "message": "Jumlah kontainer atau peti kemas. Jika tidak ada kontainer dapat diisi 0"

    },

    "kodeJenisProsedur": {

      "type": "string",

      "description": "Lihat Referensi Jenis Prosedur",

      "message": "Format kode sesuai Referensi Jenis Prosedur"

    },

    "kodeJenisEkspor": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - C. Jenis Ekspor. Lihat Referensi Jenis Ekspor",

      "message": "Format kode sesuai Referensi Jenis Ekspor"

    },

    "kodeAsuransi": {

      "type": "string",

      "description": "kode asuransi yang dibayar di [LN] luar negeri atau [DN] dalam negeri",

      "enum": [

        "LN",

        "DN"

      ],

      "message": "Kode asuransi yang dibayar: LN untuk luar negeri atau DN untuk dalam negeri"

    },

    "kodeCaraAngkutPlb": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.26 Cara Pengangkutan ke PLB. Untuk Ekspor melalui PLB mengacu Referensi Cara Angkut"

    },

    "kodeCaraBayar": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - F. Cara Pembayaran. Lihat Referensi Cara Bayar",

      "message": "Format kode sesuai Referensi Cara Bayar"

    },

    "kodeCaraDagang": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - E. Cara Perdagangan. Lihat Referensi Cara Dagang",

      "message": "Format kode sesuai Referensi Cara Dagang"

    },

    "kodeDaerahAsal": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.28 Daerah Asal Barang. Lihat Referensi Daerah Asal"

    },

    "kodeDokumen": {

      "type": "string",

      "description": "set value [33]",

      "const": "33",

      "message": "Format kode sesuai Referensi Dokumen PLB BC 3.3: 33"

    },

    "kodeGudangAsal": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.25 Lokasi/Kode Lokasi. Kode Lokasi Gudang PLB"

    },

    "kodeIncoterm": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.29 Cara Penyerahan Barang. Lihat Referensi Incoterm",

      "message": "Format kode sesuai Referensi Incoterm"

    },

    "kodeKantor": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - A. Kantor Pengawas. Lihat Referensi Kantor",

      "message": "Format kode sesuai Referensi Kantor"

    },

    "kodeKategoriEkspor": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - D. Kategori Ekspor. Lihat Referensi Kategori Ekspor",

      "message": "Format kode sesuai Referensi Kategori Ekspor"

    },

    "kodeNegaraTujuan": {

      "type": "string",

      "description": "Negara Tujuan Ekspor. Lihat Referensi Negara",

      "message": "Format kode sesuai Referensi Negara",

      "pattern": "^[A-Z]{2}$"

    },

    "kodePelBongkar": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.41 Pelabuhan Bongkar. Lihat Referensi Pelabuhan",

      "message": "Format kode pelabuhan muat sesuai Referensi Pelabuhan"

    },

    "kodePelMuat": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.40 Pelabuhan Muat Asal. Lihat Referensi Pelabuhan",

      "message": "Format kode pelabuhan muat sesuai Referensi Pelabuhan"

    },

    "kodePelTujuan": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.42 Pelabuhan Tujuan. Lihat Referensi Pelabuhan",

      "message": "Format kode pelabuhan tujuan sesuai Referensi Pelabuhan"

    },

    "kodeValuta": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - H.31 Jenis Valuta. Lihat Referensi Valuta",

      "message": "Format kode sesuai Referensi Valuta"

    },

    "kotaTtd": {

      "type": "string",

      "description": "kota tempat pengguna membuat dokumen BC 3.3",

      "message": "Kota tempat pengguna membuat dokumen BC 3.3"

    },

    "namaTtd": {

      "type": "string",

      "description": "nama pengguna yang membuat dokumen BC 3.3",

      "message": "Nama pengguna yang membuat dokumen BC 3.3"

    },

    "ndpbm": {

      "type": "number",

      "description": "Sesuai kolom formulir BC 3.3 - H.32 Nilai Tukar. Nilai tukar mata uang rupiah terhadap mata uang asing dalam harga ekspor",

      "maxlength": 24,

      "multipleOf": 0.0001,

      "message": "Ndpbm maksimal 24 digit dengan empat angka dibelakang koma"

    },

    "netto": {

      "type": "number",

      "description": "Sesuai kolom formulir BC 3.3 - H.47 Berat Bersih (kg)",

      "maxlength": 24,

      "multipleOf": 0.0001,

      "message": "Nilai netto/berat bersih maksimal 24 digit dengan empat angka dibelakang koma"

    },

    "nilaiMaklon": {

      "type": "number",

      "description": "Sesuai kolom formulir BC 3.3 - H.35 Nilai Maklon / Nilai Jasa Subkon",

      "maxlength": 24,

      "multipleOf": 0.01,

      "message": "Nilai maklon maksimal 24 digit dengan dua angka dibelakang koma"

    },

    "nilaiBarang": {

      "type": "number",

      "description": "Sesuai kolom formulir BC 3.3 - H.33 Nilai Barang",

      "maxlength": 24,

      "multipleOf": 0.01,

      "message": "Nilai barang maksimal 24 digit dengan dua angka dibelakang koma"

    },

    "nomorAju": {

      "type": "string",

      "description": "Sesuai kolom formulir BC 3.3 - Nomor Pengajuan. Nomor pengajuan dokumen pabean 26 digit dengan format 4 digit kode kantor, 2 digit kode dokumen pabean, 6 digit unik perusahaan, 8 digit tanggal pengajuan dengan format YYYYMMDD, 6 digit sequence/nomor urut pengajuan dokumen pabean",

      "pattern": "^[A-Za-z0-9]{26}$",

      "message": "Sesuaikan format nomor pengajuan dokumen ekspor terdiri 26 digit: 4 digit kode kantor, 2 digit kode dokumen pabean, 6 digit unik perusahaan, 8 digit tanggal pengajuan dengan format YYYYMMDD, 6 digit sequence/nomor urut pengajuan dokumen ekspor"

    },

    "seri": {

      "type": "integer",

      "description": "seri dokumen BC 3.3",

      "message": "seri dokumen BC 3.3"

    },

    "tanggalAju": {

      "type": "string",

      "format": "date",

      "description": "tanggal pengajuan dokumen pabean dengan format YYYY-MM-DD",

      "message": "Sesuaikan format tanggal pengajuan dokumen: YYYY-MM-DD"

    },

    "tanggalMasuk": {

      "type": "string",

      "format": "date",

      "description": "Sesuai kolom formulir BC 3.3 - H.27 Perkiraan Tanggal Pemasukan/Pengeluaran. Dengan format YYYY-MM-DD"

    },

    "tanggalMuat": {

      "type": "string",

      "format": "date",

      "description": "Sesuai kolom formulir BC 3.3 - H.39 Perkiraan Tanggal Pemuatan. Dengan format YYYY-MM-DD"

    },

    "tanggalTtd": {

      "type": "string",

      "format": "date",

      "description": "tanggal penandatanganan dokumen pabean dengan format YYYY-MM-DD",

      "message": "Sesuaikan format tanggal penandatanganan dokumen: YYYY-MM-DD"

    },

    "barang": {

      "type": "array",

      "items": [

        {

          "type": "object",

          "description": "detil data barang dalam satu pengajuan dokumen ekspor melalui/dari PLB",

          "properties": {

            "cif": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.53 Nilai Barang dengan incoterm CIF",

              "maxlength": 24,

              "multipleOf": 0.01,

              "message": "Nilai cif maksimal 24 digit dengan dua angka dibelakang koma"

            },

            "fob": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.53 FOB",

              "maxlength": 24,

              "multipleOf": 0.01

            },

            "hargaEkspor": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.51 Harga Ekspor Barang",

              "maxlength": 24,

              "multipleOf": 0.0001

            },

            "jumlahKemasan": {

              "type": "number",

              "description": "jumlah kemasan",

              "maxlength": 24,

              "multipleOf": 0.01

            },

            "jumlahSatuan": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.52 Jumlah Satuan",

              "maxlength": 24,

              "multipleOf": 0.0001

            },

            "kodeBarang": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.50 Kode Barang"

            },

            "kodeDokumen": {

              "type": "string",

              "description": "set value [33]",

              "const": "33"

            },

            "kodeJenisKemasan": {

              "type": "string",

              "description": "Lihat Referensi Jenis Kemasan"

            },

            "kodeNegaraAsal": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.49 Negara Asal Barang. Lihat Referensi Negara",

              "pattern": "^[A-Z]{2}$"

            },

            "kodeSatuanBarang": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.52 Jenis Satuan Barang. Lihat Referensi Satuan Barang"

            },

            "merk": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.49 Uraian Jenis Barang (merek)"

            },

            "ndpbm": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.32 Nilai Tukar"

            },

            "netto": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.52 Berat Bersih (kg)",

              "maxlength": 20,

              "multipleOf": 0.0001

            },

            "nilaiBarang": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.53 Nilai Barang",

              "maxlength": 24,

              "multipleOf": 0.01

            },

            "posTarif": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.49 Pos Tarif/HS"

            },

            "seriBarang": {

              "type": "integer",

              "description": "Sesuai kolom formulir BC 3.3 - H.50 Seri Barang"

            },

            "spesifikasiLain": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.49 Uraian Jenis Barang (Spesifikasi Wajib)"

            },

            "tipe": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.49 Uraian Jenis Barang (Tipe Barang)"

            },

            "ukuran": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.49 Uraian Jenis Barang (Ukuran Barang)"

            },

            "uraian": {

              "type": "string",

              "decription": "Sesuai kolom formulir BC 3.3 - H.49 Uraian Barang"

            },

            "volume": {

              "type": "number",

              "description": "Sesuai kolom formulir BC 3.3 - H.52 Volume (m3)",

              "maxlength": 24,

              "multipleOf": 0.0001

            },

            "barangTarif": {

              "type": "array",

              "description": "data barang tarif per barang",

              "items": [

                {

                  "type": "object",

                  "properties": {

                    "kodeJenisTarif": {

                      "type": "string",

                      "description": "Lihat Referensi Jenis Tarif"

                    },

                    "jumlahSatuan": {

                      "type": "number",

                      "description": "jumlah satuan barang tarif",

                      "maxlength": 20,

                      "multipleOf": 0.0001

                    },

                    "kodeFasilitasTarif": {

                      "type": "string",

                      "description": "Lihat Referensi Fasilitas Tarif"

                    },

                    "kodeSatuanBarang": {

                      "type": "string",

                      "description": "Lihat Referensi Satuan Barang"

                    },

                    "kodeJenisPungutan": {

                      "type": "string",

                      "description": "Lihat Referensi Jenis Pungutan"

                    },

                    "nilaiBayar": {

                      "type": "number",

                      "description": "nilai bayar barang tarif",

                      "maxlength": 24,

                      "multipleOf": 0.01

                    },

                    "seriBarang": {

                      "type": "integer",

                      "description": "seri barang"

                    },

                    "tarif": {

                      "type": "number",

                      "description": "tarif",

                      "maxlength": 24,

                      "multipleOf": 0.0001

                    },

                    "tarifFasilitas": {

                      "type": "number",

                      "description": "tarif fasilitas",

                      "maxlength": 5,

                      "multipleOf": 0.01

                    }

                  },

                  "required": [

                    "jumlahSatuan"

                  ]

                }

              ]

            },

            "barangDokumen": {

              "type": "array",

              "items": {

                "seriDokumen": {

                  "type": "integer",

                  "description": "seri dokumen"

                },

                "seriIjin": {

                  "type": "integer",

                  "description": "seri ijin"

                }

              }

            },

            "barangPemilik": {

              "type": "array",

              "items": [

                {

                  "type": "object",

                  "properties": {

                    "seriEntitas": {

                      "type": "integer",

                      "description": "seri entitas"

                    }

                  }

                }

              ]

            }

          },

          "required": [

            "fob",

            "jumlahKemasan",

            "kodeJenisKemasan",

            "merk",

            "posTarif",

            "spesifikasiLain",

            "tipe",

            "uraian"

          ]

        }

      ]

    },

    "entitas": {

      "type": "array",

      "description": "Sesuai kolom formulir BC 3.3 - H. Data Perdagangan. Data entitas Eksportir, Pengusaha, Pemilik, Penerima, Pembeli, PPJK dan Pengirim dalam pengajuan dokumen pabean",

      "items": [

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 - H.1-5. Data eksportir dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.3 Alamat Eksportir"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas eksportir (2). Mengacu pada Referensi Entitas",

              "const": "2"

            },

            "kodeJenisIdentitas": {

              "type": "string",

              "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

              "enum": [

                "2",

                "3",

                "4",

                "5",

                "6"

              ]

            },

            "kodeStatus": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.5 Status Perusahaan"

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.2 Nama Eksportir"

            },

            "nibEntitas": {

              "type": "string",

              "description": "Nomor Induk Berusaha"

            },

            "nomorIdentitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.1 Nomor Identitas Eksportir"

            },

            "nomorIjinEntitas": {

              "type":"string",

              "description": "Nomor Ijin Eksportir"

            },

            "tanggalIjinEntitas": {

              "type":"string",

              "format": "date",

              "description": "Tanggal Ijin Eksportir"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          },

          "required": [

            "alamatEntitas",

            "kodeEntitas",

            "kodeJenisIdentitas",

            "namaEntitas",

            "nomorIdentitas",

            "seriEntitas"

          ]

        },

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 -  Data pengusaha dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.24 Alamat Pengusaha"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas pengusaha (3). Mengacu pada Referensi Entitas",

              "const": "3"

            },

            "kodeJenisIdentitas": {

              "type": "string",

              "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

              "enum": [

                "2",

                "3",

                "4",

                "5",

                "6"

              ]

            },

            "kodeStatus": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.24 Status Perusahaan"

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.24 Nama PLB"

            },

            "nibEntitas": {

              "type": "string",

              "description": "Nomor Induk Berusaha"

            },

            "nomorIdentitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.24 Nomor Identitas Pengusaha"

            },

            "nomorIjinEntitas": {

              "type":"string",

              "description": "Nomor Ijin Pengusaha"

            },

            "tanggalIjinEntitas": {

              "type":"string",

              "format": "date",

              "description": "Tanggal Ijin Pengusaha"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          },

          "required": [

            "alamatEntitas",

            "kodeEntitas",

            "kodeJenisIdentitas",

            "namaEntitas",

            "nomorIdentitas",

            "seriEntitas"

          ]

        },

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 - H.17-19 Pembeli. Data pembeli barang dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.18 Alamat Pembeli"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas Pembeli (6). Mengacu pada Referensi Entitas",

              "const": "6"

            },

            "kodeNegara": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.19 Negara. Lihat Referensi Negara",

              "pattern": "(^[A-Z]{2}$)|(^$)"

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.17 Nama Pembeli"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          },

          "required": [

            "alamatEntitas",

            "kodeEntitas",

            "kodeNegara",

            "namaEntitas",

            "seriEntitas"

          ]

        },

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 - H.14-16 Penerima. Data penerima barang dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.15 Alamat Penerima"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas Penerima (8). Mengacu pada Referensi Entitas",

              "const": "8"

            },

            "kodeNegara": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.16 Negara. Lihat Referensi Negara",

              "pattern": "(^[A-Z]{2}$)|(^$)"

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.14 Nama Penerima"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          },

          "required": [

            "alamatEntitas",

            "kodeEntitas",

            "kodeNegara",

            "namaEntitas",

            "seriEntitas"

          ]

        },

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 - Pengirim. Data Pengirim dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - Alamat Pengirim"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas Pengirim (9). Mengacu pada Referensi Entitas",

              "default": "9"

            },

            "kodeJenisIdentitas": {

              "type": "string",

              "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

              "enum": [

                "2",

                "3",

                "4",

                "5",

                "6"

              ]

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - Nama Pengirim"

            },

            "nibEntitas": {

              "type": "string",

              "description": "Nomor Induk Berusaha"

            },

            "nomorIdentitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - Nomor Identitas Pengirim"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          }

        },

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 - H.6-10 Pemilik Barang. Data pemilik barang dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.8 Alamat Pemilik"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas pemilik (7). Mengacu pada Referensi Entitas",

              "const": "7"

            },

            "kodeJenisIdentitas": {

              "type": "string",

              "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

              "enum": [

                "2",

                "3",

                "4",

                "5",

                "6"

              ]

            },

            "kodeStatus": {

              "type": "string",

              "description": "Lihat Referensi Status Perusahaan"

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.7 Nama Pemilik"

            },

            "nibEntitas": {

              "type": "string",

              "description": "Nomor Induk Berusaha"

            },

            "nomorIdentitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.6 Nomor Identitas Pemilik"

            },

            "nomorIjinEntitas": {

              "type":"string",

              "description": "Nomor Ijin Pemilik"

            },

            "tanggalIjinEntitas": {

              "type":"string",

              "format": "date",

              "description": "Tanggal Ijin Pemilik"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          },

          "required": [

            "alamatEntitas",

            "kodeEntitas",

            "kodeJenisIdentitas",

            "namaEntitas",

            "nomorIdentitas",

            "seriEntitas"

          ]

        },

        {

          "type": "object",

          "description": "Sesuai kolom formulir BC 3.3 - H.11-13 PPJK. Data PPJK dalam pengajuan dokumen pabean",

          "properties": {

            "alamatEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.13 Alamat PPJK"

            },

            "kodeEntitas": {

              "type": "string",

              "description": "Set kode entitas PPJK (4). Mengacu pada Referensi Entitas",

              "default": "4"

            },

            "kodeJenisIdentitas": {

              "type": "string",

              "description": "Referensi Jenis Identitas: [2] Paspor, [3] KTP, [4] Lainnya, [5] NPWP 15 Digit, [6] NPWP 16 Digit",

              "enum": [

                "2",

                "3",

                "4",

                "5",

                "6"

              ]

            },

            "namaEntitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.12 Nama PPJK"

            },

            "nibEntitas": {

              "type": "string",

              "description": "Nomor Induk Berusaha"

            },

            "nomorIdentitas": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.11 NPWP PPJK"

            },

            "seriEntitas": {

              "type": "integer",

              "description": "seri entitas"

            }

          }

        }

      ]

    },

    "kemasan": {

      "type": "array",

      "description": "data kemasan dalam pengajuan dokumen pabean",

      "items": [

        {

          "type": "object",

          "description": "data kemasan yang digunakan untuk mengemas barang ekspor",

          "properties": {

            "jumlahKemasan": {

              "type": "integer",

              "description": "Sesuai kolom formulir BC 3.3 - H.45 Jumlah Kemasan"

            },

            "kodeJenisKemasan": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.45 Jenis Kemasan. Lihat Referensi Jenis Kemasan"

            },

            "merkKemasan": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.45 Merek Kemasan"

            },

            "seriKemasan": {

              "type": "integer",

              "description": "seri data kemasan berdasarkan data yang dimasukkan"

            }

          },

          "required": [

            "jumlahKemasan",

            "kodeJenisKemasan",

            "merkKemasan",

            "seriKemasan"

          ],

          "message": {

            "required": "Wajib mengisi jumlahKemasan, kodeJenisKemasan, merkKemasan, dan seriKemasan"

          }

        }

      ]

    },

    "kontainer": {

      "type": "array",

      "description": "data kontainer dalam pengajuan dokumen pabean",

      "items": [

        {

          "type": "object",

          "description": "data peti kemas/kontainer yang digunakan untuk mengangkut barang ekspor, apabila pengangkutan menggunakan peti kemas/kontainer",

          "properties": {

            "kodeJenisKontainer": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.44 Status Peti Kemas. Lihat Referensi Jenis Kontainer"

            },

            "kodeTipeKontainer": {

              "type": "string",

              "description": "Lihat Referensi Tipe Kontainer"

            },

            "kodeUkuranKontainer": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.44 Ukuran Peti Kemas. Kode ukuran kontainer: [20], [40], [45] atau [60]",

              "enum": [

                "20",

                "40",

                "45",

                "60"

              ]

            },

            "nomorKontainer": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.44 Nomor Kontainer"

            },

            "seriKontainer": {

              "type": "integer",

              "description": "seri data kontainer berdasarkan data yang dimasukkan"

            }

          },

          "dependencies": {

            "seriKontainer": [

              "kodeTipeKontainer",

              "kodeUkuranKontainer",

              "nomorKontainer"

            ]

          },

          "message": {

            "dependencies": "Wajib mengisi kodeTipeKontainer, kodeUkuranKontainer, nomorKontainer, dan seriKontainer"

          }

        }

      ]

    },

    "dokumen": {

      "type": "array",

      "description": "data dokumen pelengkap dalam pengajuan dokumen pabean",

      "items": [

        {

          "type": "object",

          "description": "data invoice sebagai dokumen pelengkap",

          "properties": {

            "idDokumen": {

              "type": "string",

              "description": "ID Dokumen"

            },

            "kodeDokumen": {

              "type": "string",

              "description": "Set kode dokumen invoice (380)",

              "const": "380"

            },

            "kodeFasilitas": {

              "type": "string",

              "description": "Lihat Referensi Fasilitas"

            },

            "kodeIjin": {

              "type": "string",

              "description": "Lihat Referensi Ijin"

            },

            "nomorDokumen": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.20 Nomor Invoice"

            },

            "seriDokumen": {

              "type": "integer",

              "description": "seri dokumen pelengkap pabean"

            },

            "tanggalDokumen": {

              "type": "string",

              "format": "date",

              "description": "Sesuai kolom formulir BC 3.3 - H.20 Tanggal Invoice dengan format YYYY-MM-DD"

            },

            "urlDokumen": {

              "type": "string",

              "description": "url dokumen invoice"

            }

          },

          "required": [

            "kodeDokumen",

            "nomorDokumen",

            "seriDokumen",

            "tanggalDokumen"

          ],

          "message": {

            "required": "Wajib mengisi kodeDokumen, nomorDokumen, seriDokumen, dan tanggalDokumen Invoice"

          }

        },

        {

          "type": "object",

          "description": "data packing list sebagai dokumen pelengkap",

          "properties": {

            "idDokumen": {

              "type": "string",

              "description": "ID Dokumen"

            },

            "kodeDokumen": {

              "type": "string",

              "description": "Set kode dokumen packing list (217)",

              "const": "217"

            },

            "kodeFasilitas": {

              "type": "string",

              "description": "Lihat Referensi Fasilitas"

            },

            "kodeIjin": {

              "type": "string",

              "description": "Lihat Referensi Ijin"

            },

            "nomorDokumen": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.21 Nomor Packing List"

            },

            "seriDokumen": {

              "type": "integer",

              "description": "seri dokumen pelengkap pabean"

            },

            "tanggalDokumen": {

              "type": "string",

              "format": "date",

              "description": "Sesuai kolom formulir BC 3.3 - H.21 Tanggal Packing List dengan format YYYY-MM-DD"

            },

            "urlDokumen": {

              "type": "string",

              "description": "url dokumen packing list (217)"

            }

          },

          "required": [

            "kodeDokumen",

            "nomorDokumen",

            "seriDokumen",

            "tanggalDokumen"

          ],

          "message": {

            "required": "Wajib mengisi kodeDokumen, nomorDokumen, seriDokumen, dan tanggalDokumen Packing List"

          }

        },

        {

          "type": "object",

          "description": "data dokumen pelengkap lainnya dalam pengajuan dokumen BC 3.3",

          "properties": {

            "idDokumen": {

              "type": "string",

              "description": "ID Dokumen"

            },

            "kodeDokumen": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.22 Jenis Dokumen Persyaratan Ekspor atau H.23 Jenis Dokumen Fasilitas Fiskal di Bidang Ekspor. Lihat Referensi Dokumen"

            },

            "kodeFasilitas": {

              "type": "string",

              "description": "Lihat Referensi Fasilitas"

            },

            "kodeIjin": {

              "type": "string",

              "description": "Lihat Referensi Ijin"

            },

            "nomorDokumen": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.22 Nomor Dokumen Persyaratan Ekspor atau H.23 Nomor Dokumen Fasilitas Fiskal di Bidang Ekspor"

            },

            "seriDokumen": {

              "type": "integer",

              "description": "seri dokumen pelengkap pabean"

            },

            "tanggalDokumen": {

              "type": "string",

              "format": "date",

              "description": "Sesuai kolom formulir BC 3.3 - H.22 Nomor Dokumen Persyaratan Ekspor atau H.23 Tanggal Dokumen Fasilitas Fiskal di Bidang Ekspor dengan format YYYY-MM-DD"

            },

            "urlDokumen": {

              "type": "string",

              "description": "url dokumen Nomor Dokumen Pelengkap Lainnya"

            }

          },

          "dependencies": {

            "seriDokumen": [

              "kodeDokumen",

              "nomorDokumen",

              "tanggalDokumen"

            ]

          },

          "message": {

            "dependencies": "Jika terdapat seriDokumen Dokumen Pelengkap lainnya, maka wajib mengisi kodeDokumen, nomorDokumen, dan tanggalDokumen Dokumen Pelengkap Lainnya "

          }

        }

      ]

    },

    "pengangkut": {

      "type": "array",

      "description": "data pengangkutan dalam pengajuan dokumen pabean",

      "items": [

        {

          "type": "object",

          "properties": {

            "namaPengangkut": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.37 Nama Sarana Pengangkut"

            },

            "nomorPengangkut": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.38 Nomor Pengangkut"

            },

            "kodeCaraAngkut": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.36 Cara Pengangkutan. Lihat Referensi Cara Angkut"

            },

            "seriPengangkut": {

              "type": "integer",

              "description": "seri data pengangkut"

            }

          },

          "required": [

            "namaPengangkut",

            "nomorPengangkut",

            "kodeCaraAngkut",

            "seriPengangkut"

          ],

          "message": {

            "required": "Wajib mengisi namaPengangkut, nomorPengangkut, kodeCaraAngkut, dan seriPengangkut"

          }

        }

      ]

    },

    "bankDevisa": {

      "type": "array",

      "description": "data bank devisa hasil ekspor",

      "items": [

        {

          "type": "object",

          "properties": {

            "kodeBank": {

              "type": "string",

              "description": "Sesuai kolom formulir BC 3.3 - H.30 Lihat Referensi Bank"

            },

            "namaBank": {

              "type": "string",

              "description": "nama bank devisa"

            },

            "seriBank": {

              "type": "integer",

              "description": "seri bank devisa"

            }

          }

        }

      ]

    }

  },

  "required": [

    "asuransi",

    "bankDevisa",

    "barang",

    "bruto",

    "cif",

    "dokumen",

    "entitas",

    "flagCurah",

    "freight",

    "jabatanTtd",

    "jumlahKontainer",

    "kemasan",

    "kodeAsuransi",

    "kodeCaraAngkutPlb",

    "kodeCaraBayar",

    "kodeCaraDagang",

    "kodeJenisEkspor",

    "kodeJenisProsedur",

    "kodeKantor",

    "kodeKategoriEkspor",

    "kodePelBongkar",

    "kodePelMuat",

    "kodePelTujuan",

    "kodeValuta",

    "kotaTtd",

    "namaTtd",

    "ndpbm",

    "netto",

    "nomorAju",

    "pengangkut",

    "tanggalTtd"

  ]

}
```
## BC 3.3 - Payload
```json
{
    "asalData": "S",
    "kodeDokumen": "33",
    "asuransi": 18377.34,
    "bruto": 11095766.00,
    "kodeCaraDagang": "15",
    "cif": 9277502.83,
    "disclaimer": "1",
    "flagCurah": "1",
    "kodeIncoterm": "FOB",
    "freight": 141945.79,
    "jabatanTtd": "jabatan_ttd",
    "jumlahKontainer": 0,
    "kodeJenisProsedur": "-"
    "kodeAsuransi": "DN",
    "kodeCaraBayar": "1",
    "kodeJenisEkspor": "1",
    "kodeCaraAngkutPlb": "-",
    "kodeDaerahAsal": "-",
    "kodeGudangAsal": "-",
    "kodeKantor": "100300",
    "kodeKantorEkspor": "100300",
    "kodeKategoriEkspor": "10",
    "kodeNegaraTujuan": "SG",
    "kodePelBongkar": "-",
    "kodePelMuat": "IDBPP",
    "kodePelTujuan": "SGSIN",
    "kodeValuta": "USD",
    "kotaTtd": "kota_ttd",
    "namaTtd": "nama_ttd",
    "ndpbm": 17217.0000,
    "netto": 11095766.0000,
    "nilaiMaklon": 0,
    "nilaiBarang": 0,
    "nomorAju": "nomor_aju",
    "seri": 1,
    "tanggalAju": "2026-05-02",
    "tanggalMasuk": "2026-05-02",
    "tanggalTtd": "2026-05-02",
    "barang": [
        {
            "cif": 0,
      "fob": 9277502.83,
            "barangPemilik": [
                {
                    "seriEntitas": 2
                }
            ],
            "hargaEkspor": 0.0000,
            "jumlahKemasan": 1.00,
            "jumlahSatuan": 76132.7700,
            "kodeBarang": "-",
      "kodeDokumen": "33",
            "kodeDaerahAsal": "3301",
            "kodeJenisKemasan": "VL",
            "kodeNegaraAsal": "ID",
            "kodeSatuanBarang": "BLL",
            "merk": "-",
            "ndpbm": 17217.0000,
            "netto": 11095766.0000,
            "nilaiBarang": 0.00,
            "posTarif": "27139000",
            "seriBarang": 1,
            "spesifikasiLain": "-",
            "tipe": "-",
            "ukuran": "-",
            "uraian": "uraian_barang",
      "volume": 0,
            "barangTarif": [
    {
                    "kodeJenisTarif": "-",
        "jumlahSatuan": 0,
        "kodeFasilitasTarif": "-",
        "kodeSatuanBarang": "-",
        "kodeJenisPungutan": "-",
        "nilaiBayar": 0,
        "seriBarang": 1,
        "tarif": 0,
        "tarifFasilitas": 0
                }
      ],
      "barangDokumen": [
    {
                    "seriDokumen": 1,
        "seriIjin": 1
                }
      ],
      "barangSpekKhusus": [
    {
                    "seriBarangSpekKhusus": 1,
        "kodeSpekKhusus": 1,
        "uraianBarangSpekKhusus": "-",
                }
      ],
      "barangPemilik": [
    {
                    "seriEntitas": 1
                }
      ],


        }
    ],
    "entitas": [
        {
            "alamatEntitas": "alamat_entitas",
            "kodeEntitas": "2",
            "kodeStatus": "6",
            "kodeJenisIdentitas": "6",
            "namaEntitas": "nama_entitias",
      "nibEntitas": "-",
      "nomorIjinEntitas": "-",
      "tanggalIjinEntitas": "2026-05-02",
            "nomorIdentitas": "nomor_identitas",
            "seriEntitas": 1
        },
        {
            "alamatEntitas": "alamat_entitas",
            "kodeEntitas": "23",
            "kodeKategoriKonsolidator": "2",
            "kodeJenisIdentitas": "6",
            "namaEntitas": "nama_entitias",
      "nibEntitas": "-",
      "nomorIjinEntitas": "-",
      "tanggalIjinEntitas": "2026-05-02",
            "nomorIdentitas": "nomor_identitas",,
            "seriEntitas": 5
        }
    ],
    "kemasan": [
        {
            "jumlahKemasan": 1,
            "kodeJenisKemasan": "VL",
            "merkKemasan": "merk_kemasan",
            "seriKemasan": 1
        }
    ],
    "kontainer": [
  {
            "kodeJenisKontainer": "-",
            "kodeTipeKontainer": "-",
            "kodeUkuranKontainer": "-",
            "nomorKontainer": "123",
      "seriKontainer": 1
        }
     ],
    "dokumen": [
        {
      "idDokumen": "-",            
      "kodeDokumen": "380",
      "kodeFasilitas": "-",
      "kodeIjin": "110",
            "nomorDokumen": "nomor_dokumen",
            "seriDokumen": 1,
            "tanggalDokumen": "2026-05-02",
      "urlDokumen": "url_dokumen",
        },
        {
      "idDokumen": "-",
      "kodeDokumen": "280",
      "kodeFasilitas": "-",
      "kodeIjin": "220",
            "nomorDokumen": "nomor_dokumen",
            "seriDokumen": 2,
            "tanggalDokumen": "2026-05-02",
      "urlDokumen": "url_dokumen",
        },
  {
      "idDokumen": "-",
      "kodeDokumen": "330",
      "kodeFasilitas": "-",
      "kodeIjin": "650",
            "nomorDokumen": "nomor_dokumen",
            "seriDokumen": 3,
            "tanggalDokumen": "2026-05-02",
      "urlDokumen": "url_dokumen",
        }
    ],
    "pengangkut": [
        {
            "namaPengangkut": "nama_pengangkut",
            "nomorPengangkut": "11/26",
            "kodeCaraAngkut": "1",
            "seriPengangkut": 1
        }
    ],
    "bankDevisa": [
        {
            "kodeBank": "2",
            "namaBank": "nama_bank",
            "seriBank": 1
        }
    ],
    "kesiapanBarang": [
        {
            "kodeJenisBarang": "1",
            "kodeJenisGudang": "2",
            "namaPic": "nama_pic",
            "alamat": "alamat_pic",
            "nomorTelpPic": "no_telp_pic",
            "jumlahContainer20": 0,
            "jumlahContainer40": 0,
            "lokasiSiapPeriksa": "GUDANG EKSPORTIR",
            "kodeCaraStuffing": "8",
            "tanggalPkb": "2026-05-02",
            "waktuSiapPeriksa": "2026-06-12T08:00:00Z"
        }
    ]
}
```