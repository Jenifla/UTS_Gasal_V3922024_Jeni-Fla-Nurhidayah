# Enkripsi dengan Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = "" # Variabel untuk menyimpan hasil enkripsi 
    for char in text: # Mengiterasi setiap karakter dalam teks yang akan dienkripsi
        if char.isalpha(): # Memeriksa apakah karakter adalah huruf
            is_upper = char.isupper() # Memeriksa apakah karakter adalah huruf kapital
            char = char.lower() # Mengonversi karakter menjadi huruf kecil
            encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97) # Mengenkripsi karakter dengan Caesar Cipher, kemudian mengonversi kembali ke huruf kecil
            if is_upper: # Memeriksa karakter asli adalah huruf kapital,maka hasil enkripsi dikonversi menjadi huruf kapital
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Enkripsi dengan Vigenere Cipher
def vigenere_encrypt(input_text, key):
    input_text = input_text.lower()  # Mengonversi teks menjadi huruf kecil
    key = key.lower()  # Mengonversi kunci menjadi huruf kecil
    input_length = len(input_text)  # Menghitung panjang teks
    key_length = len(key)  # Menghitung panjang kunci
    cipher_text = ''  # Variabel untuk menyimpan teks hasil enkripsi
    j = 0  # Inisialisasi indeks kunci (dimulai dari 0)

    for i in range(input_length):  # Mengiterasi setiap karakter dalam teks
        if input_text[i] == ' ':
            cipher_text += ' '  # Jika karakter adalah spasi, tambahkan spasi ke teks hasil enkripsi dan lanjutkan ke karakter berikutnya
            continue
        if input_text[i] == ',':
            cipher_text += ','  # Jika karakter adalah koma, tambahkan koma ke teks hasil enkripsi dan lanjutkan ke karakter berikutnya
            continue

        char_input = ord(input_text[i]) - 97  # Mengonversi karakter menjadi angka dari 0 hingga 25 
        char_key = ord(key[j % key_length]) - 97  # Mengonversi karakter kunci yang sesuai menjadi angka dari 0 hingga 25
        char_cipher = (char_input + char_key) % 26  # Melakukan operasi enkripsi Vigenere dengan menghitung sisa bagi 26
        cipher_text += chr(char_cipher + 97)  # Mengonversi hasil enkripsi kembali menjadi karakter huruf kecil
        j += 1  # Pindah ke karakter kunci berikutnya (jika sudah mencapai akhir kunci, kembali ke awal)

    return cipher_text  # Mengembalikan teks hasil enkripsi


# Dekripsi dengan Vigenere Cipher
def vigenere_decrypt(input_text, key):
    input_text = input_text.lower()  # Mengonversi teks menjadi huruf kecil
    key = key.lower() # Mengonversi kunci menjadi huruf kecil
    input_length = len(input_text)  # Menghitung panjang teks
    key_length = len(key)  # Menghitung panjang kunci
    plain_text = ''  # Variabel untuk menyimpan teks hasil dekripsi
    j = 0  # Inisialisasi indeks kunci

    for i in range(input_length):  # Mengiterasi setiap karakter dalam teks
        if input_text[i] == ' ':
            plain_text += ' '  # Jika karakter adalah spasi, tambahkan spasi ke teks hasil dekripsi dan lanjutkan ke karakter berikutnya
            continue
        if input_text[i] == ',':
            plain_text += ','  # Jika karakter adalah koma, tambahkan koma ke teks hasil dekripsi dan lanjutkan ke karakter berikutnya
            continue

        char_cipher = ord(input_text[i]) - 97  # Konversi karakter enkripsi menjadi angka 0 hingga 25 
        char_key = ord(key[j % key_length]) - 97  # Konversi karakter kunci yang sesuai menjadi angka 0 hingga 25 
        char_plain = (char_cipher - char_key + 26) % 26  # Melakukan operasi dekripsi Vigenere
        plain_text += chr(char_plain + 97)  # Mengonversi angka hasil dekripsi kembali menjadi karakter huruf kecil
        j += 1  # Pindah ke karakter kunci berikutnya

    return plain_text  # Mengembalikan teks hasil dekripsi


# Dekripsi dengan Caesar Cipher
def caesar_decrypt(text, shift):
    decrypted_text = ""  # Variabel untuk menyimpan hasil dekripsi
    for char in text:  # Mengiterasi setiap karakter dalam teks yang akan didekripsi
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            is_upper = char.isupper()  # Memeriksa apakah karakter adalah huruf kapital
            char = char.lower()  # Mengonversi karakter menjadi huruf kecil
            decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97) # Dekripsi dengan rumus Caesar Cipher, lalu mengonversi kembali ke huruf kecil
            if is_upper: # Memeriksa karakter asli adalah huruf kapital,maka hasil dekripsi dikonversi menjadi huruf kapital
                decrypted_char = decrypted_char.upper()  
            decrypted_text += decrypted_char  
        else:
            decrypted_text += char  # Jika bukan huruf, karakter hasil dekripsi akan sama tanpa perubahan
    return decrypted_text  # Mengembalikan teks yang sudah didekripsi


# Teks yang akan dienkripsi
original_text = "Success is not final, failure is not fatal, it is the courage to continue that counts"

# Kunci 
key = "jeni"

# Enkripsi dengan Caesar Cipher
caesar_shift = 31
caesar_encrypted_text = caesar_encrypt(original_text, caesar_shift)

# Enkripsi hasil enkripsi Caesar Cipher dengan Vigenere Cipher
vigenere_encrypted_text = vigenere_encrypt(caesar_encrypted_text, key)

# Dekripsi hasil enkripsi Vigenere Cipher dengan Caesar Cipher
caesar_decrypted_text = caesar_decrypt(vigenere_encrypted_text, caesar_shift)

# Dekripsi dengan Vigenere Cipher
vigenere_decrypted_text = vigenere_decrypt(caesar_decrypted_text, key)

# Output hasil enkripsi dan dekripsi
print("Pesan Asli:", original_text)
print("Pesan yang Dienkripsi (Caesar):", caesar_encrypted_text)
print("Pesan yang Dienkripsi (Vigenere):", vigenere_encrypted_text)
print("Pesan yang Didekripsi (Caesar):", caesar_decrypted_text)
print("Pesan yang Didekripsi (Vigenere):", vigenere_decrypted_text)
