import random
def gen_emoji():
    emojis = [
     "\U0001f600", # 😀 Carita sonriente 
     "\U0001f602", # 😂 Carita llorando de risa 
     "\U0001f604", # 😄 Sonrisa grande con ojos felices 
     "\U0001f609", # 😉 Guiño "\U0001f60D", # 😍 Carita con ojos de corazón 
     "\U0001f618", # 😘 Lanzando un beso "\U0001f622", # 😢 Cara llorando 
     "\U0001f62D", # 😭 Llanto fuerte "\U0001f621", # 😡 Cara muy enfadada "\U0001f631", # 😱 Cara gritando de miedo 
     "\U0001f642", # 🙂 Carita sonriente con ojos relajados 
     "\U0001f923", # 🤣 Carcajada 
     "\U0001f92A", # 🤪 Cara loca 
     "\U0001f634", # 😴 Cara dormida 
     "\U0001f970", # 🥰 Carita sonriente con corazones 
          ]
    emoji = random.choice(emojis)
    
    return emoji

print(gen_emoji())
