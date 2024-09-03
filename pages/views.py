from django.shortcuts import render
from django.http import JsonResponse as jr
import spacy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
import json

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})
def about(request):
    return render(request, "pages/about.html", {})

bot = spacy.load('en_core_web_sm')
bot_name = "AcespireBot"

def manage_request(request:HttpRequest):
    if request.method == "POST":
        text = request.POST.get("prompt",1)
        if isinstance(text,str):
            return True
        else:
            return False
    return True

@csrf_exempt
def get_bot_response(request: HttpRequest):
    if request.method == "POST":
        page_data = json.loads(request.body)
        prompt = page_data.get("message", "")
        if not prompt:
            return jr({"response": "No prompt provided."})
        response = bot(prompt)
        result = ""
        if any([token.lemma_.lower() in ["hello", "hi", "hey", "how are you", "who are you", "introduce yourself", "yourself", "how are you?", "who are you?", "who?", "why?"] for token in response]):
            result += f"Hello! I'm {bot_name.capitalize()}, your assistant for Acespire Product. How can I help you today?"
        elif any([token.lemma_.lower() in ["thanks", "thank"] for token in response]):
            result += "Hope I could help! If you have any more questions, feel free to ask."
        elif any([token.lemma_.lower() in ["company", "about", "name", "vision","acepire","mission","goal","provide","feature","features","benefit"] for token in response]):
            result += '''Acespire Consulting transforms businesses by modernizing IT, optimizing digital infrastructure, and ensuring scalability and security. We offer innovative solutions for data-driven decision-making and supply chain modernization.
            You can contact us through:<br />
            - Email: kaushik.nikkam@acespireconsulting.com<br />
            - Call us:<br />
            \tIndia: +91 94161-15310<br />
            \tUSA: +1 972-672-9843<br /><br />
            - Our Addresses are:<br />
            \t(India) 91080 WORKSPACE PVT LTD #951, 24th Main road, 2nd Floor, J.P. Nagar 2nd phase, Bengaluru, Karnataka 560078<br />
            \t(USA) 6135 Frisco Square Blvd, Suite 400, #283 Frisco, TX 75034
            '''
        elif any([token.lemma_.lower() in ["career", "job", "work", "opportunity","positions","hire","hiring","apply","team","employee"] for token in response]):
            result += """We are innovators with a strong reputation, always seeking talented professionals. Available positions include:<br />
            I) Software Developers:<ul>
            <li>Experience in Java, Python, or C#.</li>
            <li>1-2 years in related fields.</li></ul><br />
            II) Senior Data Integration Architect:<br /><ul>
            <li>Expertise in SSIS and ETL.</li>
            <li>Supply chain software experience preferred.</li></ul><br />"""
        elif any([token.lemma_.lower() in ["contact", "support", "reach", "address", 'talk','email','phone',"mobile","information","details","assistance","queries","doubt","query","doubt"] for token in response]):
            result += '''Here are some methods to contact is:<br />
            - Email: info@acespireconsulting.com<br />
            - Call us:<br />
            \tIndia: +91 94161-15310<br />
            \tUSA: +1 972-672-9843<br /><br />
            - Our Addresses are:<br />
            \t(India) 91080 WORKSPACE PVT LTD #951, 24th Main road, 2nd Floor, J.P. Nagar 2nd phase, Bengaluru, Karnataka 560078<br />
            \t(USA) 6135 Frisco Square Blvd, Suite 400, #283 Frisco, TX 75034'''
        elif any([token.lemma_.lower() in ["feedback","testimonial","review","experience","opinion","happy","satisfaction","bad"] for token in response]):
            result += 'We would love to get your valuable feedback, please visit the "contact us" section of the site for more details on how you can send us your invaluable feedback! Thanks!'
        elif any([token.lemma_.lower() in ["counterfeitproducts","koushik","testimonial","review","experience","opinion","happy","satisfaction","bad"] for token in response]):
            result += 'We would love to get your valuable feedback, please visit the "contact us" section of the site for more details on how you can send us your invaluable feedback! Thanks!'
        
        else:
            result += "I'm not sure how to respond to that. Can you please rephrase?"

        return jr({"response": (result:=(result+"<br /><br />Please note that the responses I make might not be accurate or close to what information you seek. This is because I am still under development! Thanks for understanding!"))})
    else:
        return jr({"response": "Invalid request method."}, status=405)