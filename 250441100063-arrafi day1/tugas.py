tugas = 85
uts = 75
uas = 90

# bobot
bobot_tugas = 0.3
bobot_uts = 0.3
bobot_uas = 0.4

#hitung nilai akhir
nilai_akhir = (tugas * bobot_tugas) + (uts * bobot_uts) + (uas * bobot_uas)

#output
print(f"""
      --- nilai yang kamu peroleh ---
      nilai tugas: {tugas}
      nilai uts: {uts}
      nilai uas: {uas}
      -------------------------
      nilai akhir dari tugas (30%) :  {tugas * bobot_tugas}
      nilai akhir dari uts (30%) :  {uts * bobot_uts}
      nilai akhir dari uas (40%) : {uas * bobot_uas}
      -------------------------
      total nilai akhir kamu: {nilai_akhir}""")