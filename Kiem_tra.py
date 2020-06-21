import pyodbc
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

f = open("C:/Users/User/Desktop/hoc_vien1.txt", "r")
print(f.read())

server = 'DESKTOP-SVIU6O4'
database = 'HOC_VIEN'
username = 'Vinh'
password = '123456'
driver = '{SQL Server}' # Driver you need to connect to the database
port = '1433'
cnn = pyodbc.connect('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnn.cursor()

f = open("C:/Users/User/Desktop/hoc_vien1.txt", "r")
listHV = f.readlines()
print(listHV)

#Header
a=listHV[0].split(":")
header = (a[1]).replace("\n","")
print(header)

#date
b=listHV[1].split(":")
date = (b[1]).replace("\n","")
print(date)

#maHV
c=listHV[2].split(":")
maHV = (c[1]).replace("\n","")
print(maHV)

#tenHV
d=listHV[3].split(":")
tenHV = (d[1]).replace("\n","")
print(tenHV)

#lopHV
e=listHV[4].split(":")
lopHV = (e[1]).replace("\n","")
print(lopHV)

#Email
f=listHV[5].split(":")
email = (f[1]).replace("\n","")
print(email)

#SDT
g=listHV[6].split(":")
sdt = (g[1]).replace("\n","")
print(sdt)

cursor.execute("INSERT INTO HOC_VIEN VALUES (?,?,?,?,?,?,?)",(str(header),str(date),str(maHV),str(tenHV),str(lopHV),str(email), str(sdt)))
cursor.commit()

# fromaddr = "hienvinhsieupham@gmail.com"
# toaddr = "tbtoanit@gmail.com"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Kiem tra"
# filename = "Du lieu hoc vien"
# file = open ("C:/Users/User/Desktop/hoc_vien1.txt", "r")
# msg1 = MIMEText(file.read())
# msg.attach(msg1)
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr, "vinh27061993")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()
