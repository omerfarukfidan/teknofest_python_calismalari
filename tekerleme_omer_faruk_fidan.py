from typing import Counter


tekerleme="Tekerleme: Şu tarlaya bi şinik kekere mekere ekmişler. Bu tarlaya da bi şinik kekere mekere ekmişler. Şu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuk, bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğa demiş ki; ben bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğum demiş. Öteki tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsukta; ben de; bu tarlaya ekilen bir şinik kekere mekereye dadanan boz ala boz başlıklı pis porsuğum demiş."
aranan=input("Aranan kelimeyi giriniz: ")

Counter
print('Tekerlemede '+aranan+ ' kelimesinin gecme sayisi: ', tekerleme.count(aranan))