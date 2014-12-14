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


from itertools import groupby

#def lookandsay(n):
#    '''
#        lookandsay(n)
#            n: kacinci look and say dizisini gosterigi bilgisi
#    '''
#    sequence_line = "1"
#    for i in range(n):
#        new_sequence_line = ""
#        for number, group in groupby(sequence_line):
#            new_sequence_line += "".join(str(len(list(group))) + number)
#        sequence_line = new_sequence_line 
#    return sequence_line
    
    
#itertool kullanan baska bir metot
def lookandsay(n):
    '''
        lookandsay(n)
            n: kacinci look and say dizisini gosterigi bilgisi
    '''
    sequence_line = "1"
    for i in range(n):
        new_sequence_line = ""
        new_sequence_line += ''.join( str(len(list(group))) + number for number,group in groupby(sequence_line))
        sequence_line = new_sequence_line
    return sequence_line
    
if __name__ == "__main__":
    n = input("n degerini giriniz: ")
    print lookandsay(n)