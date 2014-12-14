'''
Created on 12 Ara 2014

Bak ve soyle sira dizisi verilen dizinin elamanlarinin sozle soylenmesine gore olusmaktadir. 
Soylerken onemli olan o andaki elamanin dizide kac tane oldugunu da soylenmesidir.

Ornegin
1  -> "1 tane 1" yani gelecek dizi "11" olmaktadir
11 -> "2 tane 1" yani gelecek dizi "21"
21  -> "1 tane 2 1 tane 1" gelecek dizi "1211"
1211 
111221

Bu sekilde devam etmektedir.

girdi: n
cikti: n. lookandsay sira dizisini veren program
'''

def find_repeated(current_sequence_line):
    repeat = 0
    number = current_sequence_line[0]
    new_sequence_line = ""

    for i in current_sequence_line + " ":
        if i == number:
            repeat += 1                
        else:
            new_sequence_line += str(repeat) + number
            repeat = 1  
            number = i
    return new_sequence_line
            

def readline(n):
    current_sequence_line = "1"
    for i in range(n):
        current_sequence_line = find_repeated(current_sequence_line)
    return current_sequence_line

if __name__ == "__main__":
    n = input("n degerini giriniz: ")
    print readline(n)




