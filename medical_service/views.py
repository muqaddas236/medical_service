import google.generativeai as genai
import requests
from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import requests
from django.shortcuts import render
from django.http import JsonResponse

import google.generativeai as genai

# Giltińizdi tastıyıqlań
genai.configure(api_key="AIzaSyBFKpXQ9xtNlDbYz6g0xBdzcNQf7J-vZQE")

# Model atamasın mınaday etip ózgertiń (prefiksiz tek atı)
model = genai.GenerativeModel('gemini-2.5-flash')
# Endi modeldi sazlaymız
model = genai.GenerativeModel('gemini-2.5-flash')

def ask_ai(request):
    user_message = request.GET.get('message')
    # ... qalǵan kodlar ózgermeydi ...
# Eski qatar: model = genai.GenerativeModel('gemini-1.5-flash')
# Ornına mınanı jazıń:
model = genai.GenerativeModel('gemini-2.5-flash')
# 2. AI-dan soraw funksiyası
def ask_ai(request):
    user_message = request.GET.get('message')
    if user_message:
        prompt = f"Sen medicinalıq portal kómekshisiseń. Juwaptı qaraqalpaq tilinde ber. Soraw: {user_message}"
        try:
            response = model.generate_content(prompt)
            return JsonResponse({'reply': response.text})
        except Exception as e:
            return JsonResponse({'reply': f"AI-da qáte: {str(e)}"})
    return JsonResponse({'reply': "Xabar bos."})

# 3. Telegram xabar jiberiw funksiyasi
def send_telegram_message(name, phone, message):
    token = "8709975349:AAGuxHKPgDX2lx_8f5Wf3ExnJbH735yHxNE" # Siziń tokenińiz
    chat_id = "1388311960"        # Siziń ID-ńiz
    text = f"📩 Jańa xabar!\n👤 Atı: {name}\n📞 Tel: {phone}\n💬 Sorawı: {message}"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

# 4. Betlerdi kórsetiw
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        send_telegram_message(name, phone, message)
        return render(request, 'index.html', {'success': True})
    return render(request, 'index.html')

def robot_page(request):
    return render(request, 'robot.html')

def mskt_page(request):
    return render(request, 'mskt.html')