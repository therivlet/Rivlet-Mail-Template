import urllib.request
import urllib.parse
import json
import os

def upload_catbox(file_path):
    url = 'https://catbox.moe/user/api.php'
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    body = []
    body.append(f'--{boundary}\r\n'.encode('utf-8'))
    body.append(b'Content-Disposition: form-data; name="reqtype"\r\n\r\n')
    body.append(b'fileupload\r\n')
    
    filename = os.path.basename(file_path)
    body.append(f'--{boundary}\r\n'.encode('utf-8'))
    body.append(f'Content-Disposition: form-data; name="fileToUpload"; filename="{filename}"\r\nContent-Type: image/png\r\n\r\n'.encode('utf-8'))
    body.append(file_data)
    body.append(b'\r\n')
    body.append(f'--{boundary}--\r\n'.encode('utf-8'))
    
    payload = b''.join(body)
    req = urllib.request.Request(url, data=payload, headers={
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        res = resp.read().decode('utf-8').strip()
        print(f'{file_path} -> {res}')
        return res

if __name__ == '__main__':
    hosted_urls = {}
    files_to_upload = [
        'assets/rivlet-wordmark-navy.png',
        'assets/rivlet-wordmark-white.png',
        'assets/rivlet-wordmark-gold.png',
        'assets/rivlet-wave-navy.png',
        'assets/rivlet-wave-white.png',
        'assets/rivlet-wave-gold.png',
        'assets/rivlet-logo-navy.png',
        'assets/rivlet-logo-white.png',
        'assets/rivlet-logo-gold.png'
    ]
    
    for f in files_to_upload:
        try:
            url = upload_catbox(f)
            hosted_urls[os.path.basename(f)] = url
        except Exception as e:
            print(f'Failed {f}: {e}')
            
    with open('assets/hosted_urls.json', 'w') as f_out:
        json.dump(hosted_urls, f_out, indent=2)
    print('Done saving hosted URLs!')
