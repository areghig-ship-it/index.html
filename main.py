import random
import string
import requests
import time

# 1. تحديد الحروف والرموز اللي نبي نلعب فيها (الميكس الفخم)
# اخترنا حروف حادة وقوية، مع أرقام فرانكو، والرموز المسموحة (_ أو .)
sharp_letters = ['x', 'z', 'v', 'q', 'k', 'j']
franco_numbers = ['3', '7', '9', '4', '2']
symbols = ['_', '.']
all_letters = list(string.ascii_lowercase) # باقي الحروف الصغيرة

def generate_mix_username():
    """دالة لتوليد يوزر رباعي ميكس غريب بناءً على معادلاتنا"""
    format_type = random.choice([1, 2, 3])
    
    if format_type == 1:
        # معادلة: حرف حاد + رمز + رقم + حرف حاد (مثال: x_7z)
        return f"{random.choice(sharp_letters)}{random.choice(symbols)}{random.choice(franco_numbers)}{random.choice(sharp_letters)}"
    elif format_type == 2:
        # معادلة: حرف حاد + حرف عادي + رقمين (مثال: vx47)
        return f"{random.choice(sharp_letters)}{random.choice(all_letters)}{random.choice(franco_numbers)}{random.choice(franco_numbers)}"
    else:
        # معادلة: حرف مكرر بالطرفين وبنصهم رمز ورقم (مثال: z.7z)
        char = random.choice(sharp_letters)
        return f"{char}{random.choice(symbols)}{random.choice(franco_numbers)}{char}"

def check_username(username):
    """دالة تفحص رابط اليوزر على المنصة"""
    # ملاحظة: استخدمنا هنا رابط تجريبي، لإن تيك توك يحتاج بروكسي إذا الفحص سريع جداً
    url = f"https://www.tiktok.com/@{username}"
    
    # نرسل طلب للموقع مع تشبه بمتصفح حقيقي عشان ما يتبند السكربت سريعاً
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        
        # إذا الموقع عطانا 404 يعني الصفحة غير موجودة -> اليوزر متاح!
        if response.status_code == 404:
            return True
        else:
            return False
    except:
        print("⚠️ حدث خطأ في الاتصال، جاري التخطي...")
        return False

# 2. تشغيل البوت لفحص عدد معين من اليوزرات
print("🚀 بدأ بوت صيد اليوزرات الرباعية الميكس...")
print("----------------------------------------")

# الفحص سيتكرر 20 مرة كمثال، تقدرين تزيدين العدد
for i in range(20):
    user = generate_mix_username()
    print(f"👀 جاري فحص: {user} ... ", end="")
    
    is_available = check_username(user)
    
    if is_available:
        print(f"🎉 🎉 مُتـاح!! خذيه بسرعة!")
        # يحفظ اليوزرات المتاحة في ملف نصي برّا عشان ما تضيع عليكِ
        with open("available_users.txt", "a") as file:
            file.write(f"{user}\n")
    else:
        print("❌ محجوز")
    
    # نخليه ينتظر ثانيتين بين كل فحص وفحص عشان حماية المنصة
    time.sleep(2)

print("----------------------------------------")
print("🏁 انتهى الفحص! اليوزرات المتاحة انحفظت في ملف available_users.txt")
