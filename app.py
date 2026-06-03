import streamlit as st

st.set_page_config(
    page_title = "MATEMATIKA GEOMETRI",
    page_icon = ":heart:"
)

with st.sidebar:
    col1, col2, col3  = st.columns([1,2,1])
    with col2 :
        st.image("pj.png")
    st.title("BANGUN DATAR")
    pilihan = st.selectbox ("Pilihan Bangun Datar",["PERSEGI", "PERSEGI PANJANG", "LINGKARAN","TRAPESIUM","SEGITIGA","LAYANG-LAYANG","BELAH KETUPAT","JAJAR GENJANG",])
    st.caption("Dibuat dengan :strawberry: oleh ***dillyaww***")
   



match pilihan:
    case "PERSEGI":
        st.title("PERSEGI")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("HITUNG", type = "primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.balloons()
            

    case "PERSEGI PANJANG":
        st.title("PERSEGI PANJANG")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("HITUNG", type = "primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.snow()


    case "LINGKARAN":
        st.title("LINGKARAN")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi panjang")
        jari = st.number_input("Masukkan Jari-Jari")
        if st.button("HITUNG", type = "primary"):
            luas = 3.14 * jari * jari
            keliling = 2 * 3.14 * jari 
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.balloons()


    case "JAJAR GENJANG":
        st.title("JAJAR GENJANG")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi panjang")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi = st.number_input("Masukkan Sisi Miring")
        if st.button("HITUNG", type = "primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisi)
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.snow()

    case "TRAPESIUM":
        st.title("TRAPESIUM")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi panjang")
        a = st.number_input("Masukkan Sisi sejajar 1")
        b = st.number_input("Masukkan Sisi sejajar 2")
        atas = st.number_input("Masukkan Sisi sejajar Bawah")
        bawah = st.number_input("Masukkan Sisi Atas")
        t = st.number_input("Masukkan Tinggi")
        if st.button("HITUNG", type = "primary"):
            luas = 0.5 * (a+b)*t
            keliling =  a+b+atas+bawah
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.balloons()

    case "SEGITIGA":
        st.title("SEGITIGA")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi panjang")
        a = st.number_input("Masukkan Alas")
        s1 = st.number_input("Masukkan Sisi Miring 1")
        s2 = st.number_input("Masukkan Sisi Miring 2")
        t = st.number_input("Masukkan Tinggi")
        if st.button("HITUNG", type = "primary"):
            luas = 0.5 * a*t
            keliling = a+s1+s2
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.snow()

    case "LAYANG-LAYANG":
        st.title("LAYANG")
        st.markdown("Menghitung `LUAS` dan  `KELILING` persegi panjang")
        s1 = st.number_input("Masukkan Sisi Berdekatan 1")
        s2 = st.number_input("Masukkan Sisi Berdekatan 2")
        d1 = st.number_input("Masukkan Diagoanl 1")
        d2 = st.number_input("Masukkan Diagonal 2")
        if st.button("HITUNG", type = "primary"):
            luas = 0.5 * d1*d2
            keliling = 2 *(s1+s2)
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.balloons()

    case "BELAH KETUPAT":
        st.title("BELAH KETUPAT")
        st.markdown("Menghitung `LUAS` dan  `KELILING` ")
        sisi = st.number_input("Masukkan Sisi")
        d1 = st.number_input("Masukkan Diagonal 1")
        d2 = st.number_input("Masukkan Diagonal 2")
        if st.button("HITUNG", type = "primary"):
            luas = 0.5 * d1 *d2
            keliling = 4*sisi
            st.success(f"LUAS Persegi adalah {luas:.2f} dan KELILING Persegi adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value = luas, border=True)
            with col2:
                st.metric("Luas", value = luas, border=True)
            st.snow()

    case _ :
        st.error("TERJADI KESALAHAN")