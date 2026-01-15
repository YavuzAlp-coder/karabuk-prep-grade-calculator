def not_iste(mesaj, min_deger, max_deger):
    """
    Kullanıcıdan belirli aralıkta sayısal bir değer ister.
    Hatalı girişte (harf veya aralık dışı) uyarır ve tekrar sorar.
    """
    while True:
        girdi = input(mesaj)
        try:
            deger = float(girdi)
            if min_deger <= deger <= max_deger:
                return deger
            else:
                print(
                    f"UYARI: Lütfen {min_deger} ile {max_deger} arasında bir değer giriniz!"
                )
        except ValueError:
            print("HATA: Lütfen harf değil, sayısal bir değer giriniz!")


def ana_program():
    print("=========================================")
    print("--- HAZIRLIK ORTALAMA HESAPLAYICI ---")
    print("        --- by YavuzAlpTeber ---        ")
    print("=========================================")

    while True:
        try:
            print("\n--- Yeni Hesaplama ---")

            # Kullanıcıdan not girişlerini alıyoruz
            vize = not_iste("Vize Notunuz (0-100): ", 0, 100)

            writing_1 = not_iste("Writing 1 Notunuz (0-20): ", 0, 20)
            writing_2 = not_iste("Writing 2 Notunuz (0-20): ", 0, 20)
            speaking = not_iste("Speaking Notunuz (0-20): ", 0, 20)

            ogretmen = not_iste("Öğretmen Notu (0-100): ", 0, 100)
            katılım = not_iste("Derse Katılım Notunuz (0-100): ", 0, 100)
            online = not_iste("Online Çalışma Notunuz (0-100): ", 0, 100)
            quiz_1 = not_iste("Quiz 1 Notunuz (0-100): ", 0, 100)
            quiz_2 = not_iste("Quiz 2 Notunuz (0-100): ", 0, 100)
            final = not_iste("Final Notunuz (0-100): ", 0, 100)

            # Ağırlıklı ortalama hesaplama
            sonuc = (
                (vize * 0.30)
                + (writing_1 / 20 * 3.33)
                + (writing_2 / 20 * 3.33)
                + (speaking / 20 * 3.33)
                + (ogretmen * 0.06)
                + (katılım * 0.04)
                + (online * 0.06)
                + (quiz_1 * 0.02)
                + (quiz_2 * 0.02)
                + (final * 0.40)
            )

            print("-" * 30)
            print(f"Genel Ortalamanız: {sonuc:.2f}")

            # Başarı durumu kontrolü
            if sonuc >= 65:
                print("✅ Tebrikler, bu kuru geçtiniz!")
            else:
                print("❌ Maalesef bu kuru geçemediniz!")

            print("-" * 30)

            # Programın devamlılığı kontrolü
            devam = input(
                "Yeniden hesaplamak için 'x' tuşuna basın (Çıkmak için başka bir tuşa basın): "
            )

            if devam.lower() != "x":
                print("Programdan çıkılıyor... İyi çalışmalar!")
                break

        except KeyboardInterrupt:
            print("\nProgram zorla kapatıldı.")
            break


if __name__ == "__main__":
    ana_program()
