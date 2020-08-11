#Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains 3 elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

#The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

#The file may look as follows:
#John	Smith	5
#Anna	Boleyn	4.5
#John	Smith	2
#Anna	Boleyn	11
#Andrew	Cox	1.5

#Your task is to write a program which:

    #asks the user for Prof. Jekyll's file name;
    #reads the file contents and counts the sum of the received points for each student;
    #prints a simple (but sorted) report, just like this one:

#Andrew Cox 	 1.5
#Anna Boleyn 	 15.5
#John Smith 	 7.0

teks = open("daftar nilai.txt").read().splitlines()

dict_siswa = {}

for line in teks :
    data_siswa = line.split()
    nama = data_siswa [0] + " " + data_siswa [1]
    nilai = float(data_siswa[2])
    if nama in dict_siswa :
        dict_siswa [nama]=dict_siswa[nama]+nilai
    else :
        dict_siswa[nama]=nilai

for key,value in sorted(dict_siswa.items()):
    print (key, ":", value)
    

