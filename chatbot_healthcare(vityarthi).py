import random 

health_responses = {"headache": ["for headches , I recommend :\n1. Rest in a quiet, dark room\n2.stay hydrated\n3.try over-the-counter pain relievers\nIF persistent , please consult a doctor"," Heaches canbe caused by stress , dehydration,or eye strain. try  taking a break and drinking water."]
                    "fever":["for fever management :\n1. take temperature regularly\n2.stay hydrated\n3.rest\n4. consider acetaminophen is high\n seek medical attention if fever persists over 103degree F,make sure to rest and drink plenty of water . monitor your temperature regularly."],
                    "cold":["for cold relief:\n1.get plenty of rest\n2.stay hydrated\n3.try over the counter medications\n4.use a humidifier ","rest ,hydration and vitamin C can help with cold symptoms"],
                    "emergency":["please call emergency services-911 immediately or go to nearest emergency room, this sounds serious-please seek immediate medical attention"]}

def get_response (user_input):
    user_input=user_input.lower()

    emergency_keywords=["chest pain","breathing","unconscious","severe bleeding","stroke"]
    for keyword in emergency_keywords:
        if keyword in user_input:
            return random.choice(health_responses["emergency"])
        
    for keyword in health_responses:
        if keyword in user_input:
            return random.choice (health_responses[keyword])
    return"I'm sorry , I don't understand. Pleasecdescribe your symptoms clearly or ask about specific conditions like fever,headache or cold. for serious medical concerns, please concern a healthcare professional."

def main():
    print("healthcare chatbot: hello! I'm here to help with basic health questions.")
    print("type 'quit' to exit)" 
          
    while True:
        user_input= input("you:")
        if user_input.lower()=='quit':
            print("healthcare chatbot: take care ! remeber to consult healthcare professional for medical advice")
            break
            
        response=get_response(user_input)
        print("healthcare chatbot:",response)

if __name__=="__main__":
    main()

    
    
