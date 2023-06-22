import pyodbc

db = pyodbc.connect('Driver={SQL Server};'+ 'Server=LAPTOP-M2LJ0R6T;'+ 'Database=PythonRehber;'+ 'Trusted_Connection=yes')
imlec = db.cursor()

def kisiekle(ad,soyad,tel_no,email,sehir):
    imlec.execute("INSERT INTO Kisiler (ad, soyad, tel_no, email, sehir) VALUES (?, ?, ?, ?, ?)",
                  (ad, soyad, tel_no, email, sehir))
    db.commit()


ad = input("Ad : ")
soyad = input("Soyad : ")
tel_no = input("Telefon Numarası : ")
email = input("Email : ")
sehir = input("Şehir : ")
kisiekle(ad,soyad,tel_no,email,sehir)

db.close()
