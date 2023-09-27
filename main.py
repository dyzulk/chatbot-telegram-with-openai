import os
import openai
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from keep_alive import keep_alive

load_dotenv()

bot = Bot(token=os.getenv("tgBot_token"))
dp = Dispatcher(bot)

openai.api_key = os.getenv("openAi_token")

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
  await message.reply(
    "Halo! Saya Enday With GPT chat bot. Tanyakan saya sesuatu 😊"
  )
  await message.reply(
    "Project ini dibuat untuk menuntaskan salah satu persyaratan dari tahapan seleksi OPREC LAB SEIC ITPLN 👨🏻‍💻 ⚡"
  )
  await message.reply(
    "- Catatan :\n\nEndayWithGPT memiliki pengetahuan terbatas tentang dunia dan peristiwa mulai dari Tahun 2021 M ke belakang hingga seterusnya.\n\n-----------------------------------\n\"/command\" untuk mengetahui perintah yang ada.\n\"/help\" Dapatkan sedikit bantuan.\n\n\nAtau lebih lengkapnya baca panduan berikut : t.me/NdayWithGPT"
  )

@dp.message_handler(commands=['command'])
async def left(message: types.Message):
  await message.reply("\"/start\" memulai aktivitas bot\n\"/command\" untuk mengetahui perintah yang ada.\n\"/help\" Dapatkan sedikit bantuan\n\"/stop\" meberhentikan aktivitas bot")

@dp.message_handler(commands=['help'])
async def documentation(message: types.Message):
  await message.reply(
    "** TULIS INSTRUKSI YANG JELAS\n\nGPT tidak dapat membaca pikiran Anda. Jika hasilnya terlalu panjang, mintalah balasan singkat. Jika hasilnya terlalu sederhana, mintalah tulisan tingkat ahli. Jika Anda tidak menyukai formatnya, tunjukkan format yang ingin Anda lihat. Semakin sedikit GPT yang harus menebak apa yang Anda inginkan, semakin besar kemungkinan Anda mendapatkannya.\n\n* Contoh :\n=> Ringkas teks yang dibatasi oleh tanda kutip tiga dengan haiku. \"\"\"masukkan teks di sini\"\"\""
  )
  await message.reply(
    "** TAKTIK: SERTAKAN DETAIL DALAM KUERI ANDA UNTUK MENDAPATKAN JAWABAN YANG LEBIH RELEVAN\n\nUntuk mendapatkan respons yang sangat relevan, pastikan permintaan memberikan detail atau konteks penting. Kalau tidak, Anda menyerahkannya kepada model untuk menebak apa yang Anda maksud.\n\n* Contoh Lebih Buruk\n=> Siapa presiden?\n\n* Contoh Lebih Baik\n=> Siapa presiden Indonesia pada tahun 2023, dan seberapa sering pemilu diadakan?"
  )
  await message.reply(
    "** TAKTIK: GUNAKAN PEMBATAS UNTUK MENUNJUKKAN DENGAN JELAS BAGIAN INPUT YANG BERBEDA\n\nPembatas seperti tanda kutip tiga, tag XML, judul bagian, dll. Dapat membantu membatasi bagian teks agar diperlakukan berbeda."
  )
  await message.reply(
    "** TAKTIK: TENTUKAN PANJANG OUTPUT YANG DIINGINKAN\n\nAnda dapat meminta model untuk menghasilkan output dengan panjang target tertentu. Panjang keluaran yang ditargetkan dapat ditentukan dalam hal jumlah kata, kalimat, paragraf, poin-poin, dll. Namun perlu dicatat bahwa menginstruksikan model untuk menghasilkan sejumlah kata tertentu tidak bekerja dengan presisi tinggi. Model dapat lebih andal menghasilkan keluaran dengan jumlah paragraf atau poin-poin tertentu.\n\n* Contoh :\n=> Ringkas teks yang dibatasi oleh tanda kutip tiga dalam sekitar 50 kata. \"\"\"masukkan teks di sini\"\"\"\n\n=> Ringkas teks yang dibatasi oleh tanda kutip tiga dalam 2 paragraf. \"\"\"masukkan teks di sini\"\"\""
  )

@dp.message_handler(commands=['stop'])
async def left(message: types.Message):
  await message.reply("Sampai Jumpa!\nTerimakasih Telah Berkunjung 😊")

@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=message.text,
                                      temperature=0.5,
                                      max_tokens=924,
                                      top_p=1,
                                      frequency_penalty=0.0,
                                      presence_penalty=0.0)
  await message.reply(response.choices[0].text)

keep_alive()
if __name__ == "__main__":
  executor.start_polling(dp)
