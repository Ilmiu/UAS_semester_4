import pickle
import streamlit as st
from PIL import Image


# title
# st.sidebar[home]

st.title("Prediksi Penyakit Cacar Monyet")

monkeypox_model = pickle.load(open('monkeypox_model5.sav','rb'))

st.write("1. Apa yang anda rasakan saat ini?")
st.success("1.) Tidak merasakan apapun")
st.success("2.) Pembengkakan kelenjar getah bening")
st.success("3.) Demam")
st.success("4.) Nyeri Otot")
systemicIllness = st.radio("Isi salah satu",(1,2,3,4))

st.warning("panduan")
st.write("Isi dengan 1 apabila anda merasakan gejala yang disebutkan")
st.write("dan isi dengan 0 jika anda tidak merasakan gejala yang disebutkan")
st.success("Ya : 1, Tidak : 0")

col1, col2 = st.columns(2)

with col1:
    RectalPain = st.radio(" 2.Apakah anda merasakan Nyeri pada Dubur?",(1,0))
    Sorethroat = st.radio(" 3.Apakah anda merasakan Sakit pada tenggorokan?",(1,0))
    PenileOedema = st.radio(" 4.Apakah anda mengalami pembengkakan pada penis?",(1,0))
    orallesions = st.radio(" 5.Apakah anda mengalami lesi(benjolan, bercak, luka) dalam mulut? seperti sariawan, lepuh herpes, atau radang gusi",(1,0))
with col2:
    solitarylesions = st.radio(" 6.Apakah anda memiliki lesi(benjolan, bercak, luka) ruam pada kulit yang berbentuk cincin bulat kemerahan?",(1,0))
    swollentonsils = st.radio(" 7.Apakah anda mengalami pembengkakan amandel?",(1,0))
    HIV = st.radio(" 8.Apakah anda memiliki riwayat penyakit HIV?",(1,0))
    Sexuallytransmitted = st.radio(" 9.Apakah anda memiliki riwayat penyakit Sexual menular?",(1,0))


# predikssi
monkeypox_diagnosis = ''

# tombol
if st.button('Analisa'):
    monkeypox = monkeypox_model.predict([[systemicIllness, RectalPain, Sorethroat, PenileOedema, orallesions,
                                          solitarylesions, swollentonsils, HIV, Sexuallytransmitted]])
    if(monkeypox[0] == True):
        'Anda Terindikasi terkena cacar monyet'
        st.error(monkeypox_diagnosis)
        st.error("Test ini sebatas prediksi dengan akurasi 61%, segera periksakan ke fasilitas kesehatan terdekat jika gejala terus berlanjut")
    else:
        monkeypox_diagnosis = 'Anda Tidak Terindikasi Cacar monyet'
        st.success(monkeypox_diagnosis)
        
# artikel
with st.sidebar:
    st.title("Penyakit Cacar Monyet")
    image = Image.open('images/cacar air.JPG')
    st.image(image,caption='cacar air pada manusia', use_column_width=True)
    st.subheader("Apa itu Cacar Monyet?")
    st.write("Cacar monyet adalah penyakit zoonosis langka yang disebabkan oleh infeksi virus monkeypox. Virus cacar monyet termasuk dalam genus Orthopoxvirus dalam famili Poxviridae. Genus Orthopoxvirus juga termasuk virus variola (penyebab cacar), virus vaccinia (digunakan dalam vaksin cacar), dan virus cacar sapi."+
             "Cacar monyet pertama kali ditemukan pada tahun 1958. Pada saat itu ditemukan wabah penyakit mirip cacar yang menyerang koloni monyet yang dipelihara untuk penelitian, hal tersebut yang menyebabkan penyakit ini disebut sebagai cacar monyet atau monkeypox.")
    st.write("Kasus cacar monyet pertama yang menginfeksi manusia tercatat pada tahun 1970 di Republik Demokratik Kongo. Sejak saat itu, kasus cacar monyet dilaporkan telah menginfeksi orang-orang di beberapa negara Afrika Tengah dan Barat lainnya seperti : Kamerun, Republik Afrika Tengah, Pantai Gading, Republik Demokratik Kongo, Gabon, Liberia, Nigeria, Republik Kongo, dan Sierra Leone.")


    image2 = Image.open('images/gejala.JPG') 
    st.image(image2,caption='gejala cacar monyet pada manusia', use_column_width=True)
    st.subheader("Apa saja gejala Cacar Monyet?")
    st.write("Pada manusia, gejala cacar monyet mirip dengan gejala cacar air, namun lebih ringan. Gejala dimulai dengan demam, sakit kepala, nyeri otot, dan kelelahan. Perbedaan utama antara gejala cacar air dan cacar monyet adalah bahwa cacar monyet menyebabkan pembengkakan pada kelenjar getah bening (limfadenopati) sedangkan cacar air tidak. Masa inkubasi cacar monyet biasanya berkisar dari 6 hingga 13 hari tetapi dapat pula 5 hingga 21 hari.")
    st.write("Dalam 1 sampai 3 hari (kadang-kadang lebih lama) setelah munculnya demam, penderita akan mengalami ruam, sering dimulai pada wajah kemudian menyebar ke bagian lain dari tubuh.")
    st.write("Penyakit ini biasanya berlangsung selama 2−4 minggu. Di Afrika, cacar monyet telah terbukti menyebabkan kematian pada 1 dari 10 orang yang terinfeksi penyakit tersebut.")

    image3 = Image.open('images/cacar monyet2.PNG')
    st.image(image3,caption='cacar monyet pada manusia', use_column_width=True)
    st.subheader("Bagaimana cara mencegahnya?")
    st.write("- Hindari kontak dengan hewan yang dapat menjadi reservoir virus (termasuk hewan yang sakit atau yang ditemukan mati di daerah di mana cacar monyet terjadi.")
    st.write("- Hindari kontak dengan bahan apa pun, seperti tempat tidur, yang pernah bersentuhan dengan hewan yang sakit.")
    st.write("- Pisahkan pasien yang terinfeksi dari orang lain yang mungkin berisiko terinfeksi.")
    st.write("- Lakukan cuci tangan yang baik dan benar setelah kontak dengan hewan atau manusia yang terinfeksi.")
    st.write("- Menggunakan alat pelindung diri (APD) saat merawat pasien yang terinfeksi.")
    st.write("- Memasak daging dengan benar dan matang.")