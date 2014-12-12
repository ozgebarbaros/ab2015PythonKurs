# -*- coding: utf-8 -*-
'''
Created on 12 Ara 2014

Anagram, bir sozcugun veya sozcuk grubunun harflerinin degisik duzende baska bir sozcuk veya sozcuk grubunu olustrurulmasidir. 
Iki sozcuk aralarinda anagram olup olmamasi icinde bulundugu harflerle birbirlerini elde edip edememekle alakalidir.
Bahri - ihbar sozcukleri anagram sozcuklerdir. 

Program verilen iki sozcuk veya sozcuk grubunun anagram olup olmadigini soyleyecektir. Buyuk kucuk harf duyarsiz olmalidir
'''

def anagram(birinci_soz, ikinci_soz):
    return sorted(birinci_soz.upper().replace(' ', '')) == sorted(ikinci_soz.upper().replace(' ', ''))


#anagram icin baska bir metot - uzun yol
#def anagram(birinci_soz, ikinci_soz):
#    birinci_soz = list(birinci_soz.lower().replace(' ', ''))
#    ikinci_soz = list(ikinci_soz.lower().replace(' ', ''))
#    for i in birinci_soz:
#        if i not in ikinci_soz:
#            return False
#        del(ikinci_soz[ikinci_soz.index(i)])
#    return True
        
if __name__ == "__main__":
    birinci_soz = raw_input("ilk sozcugu giriniz: ")
    ikinci_soz = raw_input("ikinci sozcugu giriniz: ")
    print anagram(birinci_soz, ikinci_soz)
