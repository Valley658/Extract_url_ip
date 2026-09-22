import socket
from urllib.parse import urlparse

def get_ip_from_url(url: str):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    hostname = urlparse(url).hostname
    
    if not hostname:
        return None, "올바르지 않은 URL 형식입니다."

    try:
        ip_address = socket.gethostbyname(hostname)
        return hostname, ip_address
    except socket.gaierror:
        return hostname, "IP 주소를 찾을 수 없습니다 (DNS 조회 실패)."

urls = [
    "https://pastellive.co.kr"
]

for target_url in urls:
    domain, ip = get_ip_from_url(target_url)
    print(f"도메인: {domain} -> IP: {ip}")