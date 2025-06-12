import requests

webhook_url = "https://teamroom.nate.com/api/webhook/910f895f/3oQ1GiUSb0Vm4NdyZjI8mWYy"
message = {
    "text": "✅ In-house-Magazine 페이지가 업데이트 되었습니다.\n\n👉 https://agency8group.github.io/In-house-Magazine/\n(인하우스 매거진 사이트가 오픈하였습니다. 편하게 둘러봐주세요_test)"
}

resp = requests.post(webhook_url, json=message)
print("응답코드:", resp.status_code)
print("응답내용:", resp.text)