# Makeup by Iremi - Proje Kuralları ve Yönergeleri

## Genel Kurallar
- Tüm görünür metinler Türkçe olmalıdır. (Marka adı "MAKEUP by IREMI" İngilizce bırakılabilir).
- Kesinlikle yapay zeka ile görsel/resim üretilmeyecektir.
- Görsel gereken yerlerde geçici olarak tek renkli (örneğin var(--bg-muted)) dikdörtgenler (placeholder) kullanılacaktır.
- Görsel kod bloklarında, geliştiricinin resmi nereye ve hangi isimle atacağını anlaması için açıklayıcı yorum satırları eklenecektir. Örnek: `/* PHOTO: bridal-1.jpg (1000x1000) */`
- Tasarımda kenarlık (border) ve kutu gölgesi (box-shadow) kullanılmayacak, temiz ve editoryal bir görünüm sağlanacaktır.
- Mobil uyumluluk zorunludur.

## Renkler ve Tipografi (Tasarım Sistemi)
Tüm renk ve fontlar `:root` seviyesinde CSS değişkenleri (CSS variables) olarak tanımlanmalı ve projenin hiçbir yerinde hardcoded (elle yazılmış sabit) renk veya font kullanılmamalıdır.

**Değişkenler:**
- `--bg`: `#f6f4f0` (Krem/Bej arka plan)
- `--bg-dark`: `#111111` (Koyu arka plan - About ve Contact kısımları)
- `--ink`: `#0b0b0b` (Ana metin rengi)
- `--gold`: `#c9a97a` (Vurgu/Accent rengi)
- `--muted`: `#8a8a8a` (Soluk metin rengi)
- `--font-serif`: `'Playfair Display', serif` (Başlıklar, italik vurgular)
- `--font-sans`: `'Jost', sans-serif` (Gövde metni, menüler, etiketler)

## Sayfa Bölümleri
1.  **Hero:** Tam ekran, sabit (fixed) başlık. Ortalı fotoğraf galerisi ve transparan geçişli devasa "MAKEUP by IREMI" yazısı. Alt kısımda "Her yüz bir hikaye anlatır..." yazısı ve "Serik · Antalya" lokasyon bilgisi.
2.  **About (Curtain):** Scroll yapıldığında Hero'nun üzerine çıkan siyah perde efektli bölüm. Sol tarafta portre (placeholder), sağ tarafta editoryal metin.
3.  **Services:** 3x3 grid yapısında zebra desenli bölüm.
    *   Satır 1: Görsel | Görsel | Metin (Bridal Pro)
    *   Satır 2: Metin (Hair & Türban) | Görsel | Görsel
    *   Satır 3: Görsel | Görsel | Metin (Freelance & Set)
4.  **References:** Sonsuz kayan (infinite marquee) yatay şerit. Müşteri yorumları kartları. 5 yıldızlı değerlendirme ve yorum metni. Üzerine gelince (hover) kayma durur.
5.  **Contact:** Tam ekran siyah arka plan. "İletişim" başlığı, iletişim bilgileri ve form. Alt kısımda "Serik · Antalya".
