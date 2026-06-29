from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Menu Unggulan ──────────────────────────────────────────────
UNGGULAN = [
    {
        "id": 101,
        "name": "Singkong Keju D9",
        "category": "OLAHAN SINGKONG",
        "price": 25000,
        "rating": 5.0,
        "reviews": 1244,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Singkong+Keju"
    },
    {
        "id": 102,
        "name": "Getuk D9 Pelangi",
        "category": "MANIS TRADISIONAL",
        "price": 20000,
        "rating": 4.9,
        "reviews": 982,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Getuk+Pelangi"
    },
    {
        "id": 103,
        "name": "Kroket Singkong D9",
        "category": "CEMILAN GURIH",
        "price": 22000,
        "rating": 4.8,
        "reviews": 843,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Kroket+Singkong"
    },
    {
        "id": 104,
        "name": "Prol Tape Keju D9",
        "category": "VARIAN TAPE",
        "price": 35000,
        "rating": 4.9,
        "reviews": 528,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Prol+Tape"
    },
    {
        "id": 105,
        "name": "Timus Manis D9",
        "category": "KUDAPAN SORE",
        "price": 18000,
        "rating": 4.7,
        "reviews": 315,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Timus+Manis"
    },
    {
        "id": 106,
        "name": "Gemblong Cotot D9",
        "category": "TRADISI SALATIGA",
        "price": 20000,
        "rating": 4.8,
        "reviews": 526,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Gemblong+Cotot"
    }
]

# ── Makanan Berat ──────────────────────────────────────────────
MAKANAN_BERAT = [
    {
        "id": 1,
        "name": "Bakmi Jawa Godog (Rebus)",
        "category": "MAKANAN BERAT",
        "description": "Mie rebus tradisional dengan kuah kaldu kentol dan rempah pilihan.",
        "price": 22000,
        "rating": 4.5,
        "reviews": 320,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Bakmi+Godog"
    },
    {
        "id": 2,
        "name": "Bakmi Jawa Goreng",
        "category": "MAKANAN BERAT",
        "description": "Mie goreng khas Jawa dengan aroma smokey dan cita rasa manis gurih.",
        "price": 22000,
        "rating": 4.5,
        "reviews": 285,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Bakmi+Goreng"
    },
    {
        "id": 3,
        "name": "Nasi Goreng Spesial",
        "category": "FAVORIT",
        "description": "Nasi goreng dengan telur, ayam, dan sayuran segar khas D9.",
        "price": 25000,
        "rating": 4.8,
        "reviews": 510,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Nasgor+Spesial"
    },
    {
        "id": 4,
        "name": "Nasi Goreng Babat",
        "category": "MAKANAN BERAT",
        "description": "Nasi goreng gurih dengan potongan babat empuk bumbu rempah.",
        "price": 28000,
        "rating": 4.6,
        "reviews": 198,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Nasgor+Babat"
    },
    {
        "id": 5,
        "name": "Nasi Pecel",
        "category": "MENU TRADISIONAL",
        "description": "Sayuran segar dengan siraman bumbu kacang gurih dan rempeyek renyah.",
        "price": 18000,
        "rating": 4.7,
        "reviews": 425,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Nasi+Pecel"
    },
    {
        "id": 6,
        "name": "Nasi Ayam Goreng",
        "category": "MAKANAN BERAT",
        "description": "Ayam goreng bumbu lengkap dengan sambal kentol dan lalapan.",
        "price": 25000,
        "rating": 4.8,
        "reviews": 480,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Nasi+Ayam+Goreng"
    },
    {
        "id": 7,
        "name": "Nasi Ayam Bakar",
        "category": "MAKANAN BERAT",
        "description": "Ayam bakar bumbu kecap meresap dengan aroma bakaran yang menggoda.",
        "price": 26000,
        "rating": 4.9,
        "reviews": 390,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Nasi+Ayam+Bakar"
    },
    {
        "id": 8,
        "name": "Soto Ayam / Sop",
        "category": "MENU SEGAR",
        "description": "Soto ayam kuah bening segar dengan irisan dan rempah dan kuva gurih.",
        "price": 20000,
        "rating": 4.6,
        "reviews": 310,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Soto+Ayam"
    },
]

# ── Makanan Ringan ─────────────────────────────────────────────
MAKANAN_RINGAN = [
    {
        "id": 9,
        "name": "Singkong Keju Original",
        "category": "OLAHAN TERLARIS",
        "description": "Singkong goreng renyah dengan taburan keju yang melimpah.",
        "price": 25000,
        "rating": 5.0,
        "reviews": 1244,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Singkong+Keju"
    },
    {
        "id": 10,
        "name": "Singkong Keju Cokelat / Meises",
        "category": "MANIS TRADISIONAL",
        "description": "Perpaduan gurihnya singkong dengan manisnya cokelat meises.",
        "price": 25000,
        "rating": 4.9,
        "reviews": 982,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Singkong+Cokelat"
    },
    {
        "id": 11,
        "name": "Singkong Sambal Roa",
        "category": "CAMILAN GURIH",
        "description": "Singkong goreng khas D9 disajikan dengan sambal roa pedas mantap.",
        "price": 22000,
        "rating": 4.8,
        "reviews": 843,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Singkong+Sambal"
    },
    {
        "id": 12,
        "name": "Tahu Serasi Goreng",
        "category": "KHAS BANDUNGAN",
        "description": "Tahu goreng khas Bandungan yang lembut dan gurih.",
        "price": 18000,
        "rating": 4.7,
        "reviews": 315,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Tahu+Serasi"
    },
    {
        "id": 13,
        "name": "Tempe Mendoan",
        "category": "GORENGAN FAVORIT",
        "description": "Tempe goreng tepung setengah matang dengan irisan daun bawang.",
        "price": 15000,
        "rating": 4.6,
        "reviews": 290,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Tempe+Mendoan"
    },
    {
        "id": 14,
        "name": "Pisang Goreng",
        "category": "MANIS ALAMI",
        "description": "Pisang goreng manis dengan pilihan topping keju atau cokelat.",
        "price": 18000,
        "rating": 4.7,
        "reviews": 350,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Pisang+Goreng"
    },
    {
        "id": 15,
        "name": "Kroket Singkong",
        "category": "CAMILAN GURIH",
        "description": "Kroket lembut berbahan dasar singkong pilihan.",
        "price": 20000,
        "rating": 4.8,
        "reviews": 526,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Kroket+Singkong"
    },
    {
        "id": 16,
        "name": "Tape Goreng",
        "category": "MANIS LEGIT",
        "description": "Tape singkong goreng yang manis dan legit.",
        "price": 15000,
        "rating": 4.5,
        "reviews": 210,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Tape+Goreng"
    },
    {
        "id": 17,
        "name": "Getuk Goreng",
        "category": "TRADISI SALATIGA",
        "description": "Getuk singkong manis yang digoreng hingga renyah di luar.",
        "price": 18000,
        "rating": 4.8,
        "reviews": 420,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Getuk+Goreng"
    },
    {
        "id": 18,
        "name": "Roti Bakar (Aneka Topping)",
        "category": "CAMILAN POPULER",
        "description": "Roti bakar hangat dengan berbagai pilihan topping toast.",
        "price": 20000,
        "rating": 4.6,
        "reviews": 380,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Roti+Bakar"
    },
]

# ── Minuman ────────────────────────────────────────────────────
MINUMAN = [
    {
        "id": 19,
        "name": "Teh Poci",
        "category": "SEDUHAN TRADISIONAL",
        "description": "Teh poci tradisional yang harum dan menyegarkan.",
        "price": 13000,
        "rating": 4.8,
        "reviews": 860,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Teh+Poci"
    },
    {
        "id": 20,
        "name": "Es Teh Kampul",
        "category": "SEGARNYA ALAMI",
        "description": "Es teh segar dengan sensasi kampul yang khas.",
        "price": 8000,
        "rating": 4.7,
        "reviews": 945,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Es+Teh+Kampul"
    },
    {
        "id": 21,
        "name": "Wedang Uwuh",
        "category": "SEDUHAN ALAMI",
        "description": "Wedang uwuh hangat dengan rempah-rempah tradisional.",
        "price": 12000,
        "rating": 4.9,
        "reviews": 990,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Wedang+Uwuh"
    },
    {
        "id": 22,
        "name": "Wedang Jahe",
        "category": "HANGAT MENYEHATKAN",
        "description": "Wedang jahe hangat yang menyehatkan tubuh.",
        "price": 10000,
        "rating": 4.7,
        "reviews": 710,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Wedang+Jahe"
    },
    {
        "id": 23,
        "name": "Wedang Ronde",
        "category": "LEGENDA HANGAT",
        "description": "Wedang ronde dengan isian kacang yang gurih.",
        "price": 15000,
        "rating": 4.8,
        "reviews": 850,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Wedang+Ronde"
    },
    {
        "id": 24,
        "name": "Kopi Hitam Tubruk",
        "category": "KOPI KLASIK",
        "description": "Kopi hitam tubruk khas yang kuat dan nikmat.",
        "price": 12000,
        "rating": 4.6,
        "reviews": 620,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Kopi+Tubruk"
    },
    {
        "id": 25,
        "name": "Kopi Susu",
        "category": "LEMBUT & CREAMY",
        "description": "Kopi susu lembut yang creamy dan nikmat.",
        "price": 18000,
        "rating": 4.9,
        "reviews": 1050,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Kopi+Susu"
    },
    {
        "id": 26,
        "name": "Es Campur",
        "category": "MINUMAN PALING SEGAR",
        "description": "Es campur segar dengan aneka buah dan sirup.",
        "price": 22000,
        "rating": 4.8,
        "reviews": 880,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Es+Campur"
    },
    {
        "id": 27,
        "name": "Es Teler",
        "category": "FAVORIT NUSANTARA",
        "description": "Es teler segar dengan alpukat, kelapa, dan nangka.",
        "price": 25000,
        "rating": 4.9,
        "reviews": 730,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Es+Teler"
    },
    {
        "id": 28,
        "name": "Aneka Jus Buah",
        "category": "FRESH & SEHAT",
        "description": "Jus buah segar pilihan yang menyehatkan.",
        "price": 15000,
        "rating": 4.7,
        "reviews": 480,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Jus+Buah"
    },
    {
        "id": 29,
        "name": "Lemon Tea (Panas / Es)",
        "category": "SEGAR & SEHAT",
        "description": "Lemon tea yang segar dan menyehatkan.",
        "price": 10000,
        "rating": 4.6,
        "reviews": 390,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Lemon+Tea"
    },
    {
        "id": 30,
        "name": "Teh Manis / Tawar",
        "category": "MINUMAN SEPANJANG",
        "description": "Teh manis atau tawar hangat/dingin.",
        "price": 5000,
        "rating": 4.5,
        "reviews": 1200,
        "image": "https://placehold.co/300x250/fdfbf7/7a6353?text=Teh+Manis"
    },
]

@app.route('/')
def index():
    return render_template(
        'index.html',
        unggulan=UNGGULAN,
        makanan_berat=MAKANAN_BERAT,
        makanan_ringan=MAKANAN_RINGAN,
        minuman=MINUMAN
    )

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    password = data.get('password')
    # Simple dummy check
    if password == 'admin123':
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Incorrect password."}), 401

if __name__ == '__main__':
    app.run(debug=True)
