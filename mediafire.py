import requests, json, os, sys, shutil

key = "apivinz"
api = "https://api.zeks.xyz/api/mediafire?apikey={}&url=".format(key)

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

kosong = ""

logo = """
{:>6}        ╭╮    ╭━╮
{:>6}        ┃┃    ┃╭╯
{:>6}╭╮╭┳━━┳━╯┣┳━━┳╯╰┳┳━┳━━╮
{:>6}┃╰╯┃┃━┫╭╮┣┫╭╮┣╮╭╋┫╭┫┃━┫
{:>6}┃┃┃┃┃━┫╰╯┃┃╭╮┃┃┃┃┃┃┃┃━┫
{:>6}╰┻┻┻━━┻━━┻┻╯╰╯╰╯╰┻╯╰━━╯
{:>6}
{:>6}  :: Coded Tegar Dev
{:>6}
""".format(kosong, kosong, kosong, kosong, kosong, kosong, kosong, kosong, kosong)


def download():
    file_url = donlot
    nama_file = file_url.split("/")[-1]
    r = requests.get(file_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(nama_file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print(f'{CGREEN}Berhasil, nama file {CWHITE}:',nama_file)
    else:
        print(f'{CRED}Terjadi Kesalahan')


os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
link = input(f"{CGREEN}link mediafire {CWHITE}: ")
req = requests.get(api+link)
jeson = json.loads(req.text)
data = jeson
try:
    print(f"{CGREEN}status {CWHITE}:",data["status"])
    print(f"{CGREEN}nama file {CWHITE}:",data["name_file"])
    print(f"{CGREEN}tanggal upload {CWHITE}:",data["upload_date"])
    print(f"{CGREEN}tipe file {CWHITE}:",data["file_type"])
    print(f"{CGREEN}deskripsi {CWHITE}:",data["description"])
    print(f"{CGREEN}link download {CWHITE}:",data["download"])
    lanjut=input(f"ingin mendownload nya?(y/n) : {CGREEN}")
    if lanjut == "y":
        print(f"{CYELLOW}silahkan tunggu...")
        donlot = data["download"]
        download()
    else:
        sys.exit(f"{CRED}anda tidak mendownload nya")
except:
    print(f"{CGREEN}pesan {CWHITE}:",data["message"])
    sys.exit()
