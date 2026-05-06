import speedtest

def hiz_testi_yap():
    st = speedtest.Speedtest()
    
    # En yakın ve en iyi sunucuyu bulma.
    print("En iyi sunucu aranıyor")
    st.get_best_server()
    
    # Download hızını ölçme.
    print("İndirme hızı ölçülüyor...")
    indirme_hizi = st.download()
    
    # Upload hızını ölçme.
    print("Yükleme hızı ölçülüyor...")
    yukleme_hizi = st.upload()
    
    # Ping süresini alıyor.
    ping = st.results.ping
    
    # Kütüphane sonuçları bit cinsinden verdiği için sonucu 1.000.000 a bölüyor.
    indirme_mbps = indirme_hizi / (1000000)
    yukleme_mbps = yukleme_hizi / (1000000)
    
    # Sonuçları ekrana düzgün bir şekilde yazdırıyor.
    print("\n" + "="*30)
    print("     HIZ TESTİ SONUÇLARI")
    print("="*30)
    print(f"İndirme Hızı : {indirme_mbps:.2f} Mbps")
    print(f"Yükleme Hızı : {yukleme_mbps:.2f} Mbps")
    print(f"Ping         : {ping} ms")
    print("="*30)

if __name__ == "__main__":
    hiz_testi_yap()