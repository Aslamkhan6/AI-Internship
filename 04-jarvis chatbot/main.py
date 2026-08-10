import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
apikey = os.getenv("apikey")

chatStr = ""

# Initialize text-to-speech engine
engine = pyttsx3.init()


def say(text):
    engine.say(text)
    engine.runAndWait()


def chat(query):
    global chatStr

    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for line in chatStr.strip().split("\n"):
        if line.startswith("You: "):
            messages.append({"role": "user", "content": line[5:]})
        elif line.startswith("Jarvis: "):
            messages.append({"role": "assistant", "content": line[8:]})

    messages.append({"role": "user", "content": query})


    # try:
    client = openai.OpenAI(apikey)
    response = client.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = response["choices"][0]["message"]["content"].strip()
    say(reply)
    chatStr += f"You: {query}\nJarvis: {reply}\n"
    return reply
    # except Exception as e:
    #     say("Sorry, there was an error processing your request.")
    #     print("Error:", e)
    #     return "Error occurred."


def ai(messages):
    text = f"OpenAI response for Prompt: {messages[1]['content']} \n*************************\n\n"
    # try:
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
         stream=False,
    )
    reply = response.choices[0].message.content
    text += reply



    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    filename = f"Openai/{random.randint(1000,9999)}.txt"
    with open(filename, "w") as f:
        f.write(text)

    say("The response has been saved.")
    # except Exception as e:
    #     say("Failed to get a response from OpenAI.")
    #     print("Error:", e)




def takeCommand():
    try:
        
        if not sr.Microphone.list_microphone_names():
            raise OSError("No Microphone Found")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query
            except Exception as e:
                print("Recognition Error:", e)
                return "Some Error Occurred. Sorry from Jarvis."

    except OSError:
        
        say("Microphone not found. Switching to text input.")
        return input("Type your command: ")




if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Welcome to Jarvis A.I")

    while True:
        query = takeCommand()


        
        sites = [
                  ["youtube", "https://www.youtube.com"],
                  ["wikipedia", "https://www.wikipedia.org"],
                  ["google", "https://www.google.com"],
                  ["whatsapp", "https://web.whatsapp.com"],
                  ["facebook", "https://www.facebook.com"],
                  ["instagram", "https://www.instagram.com"],
                  ["twitter", "https://www.twitter.com"],
                  ["amazon", "https://www.amazon.in"],
                  ["flipkart", "https://www.flipkart.com"],
                  ["gmail", "https://mail.google.com"],
                  ["linkedin", "https://www.linkedin.com"],
                  ["stack overflow", "https://stackoverflow.com"],
                  ["chatgpt", "https://chat.openai.com"],
                  ["github", "https://github.com"],
                  ["netflix", "https://www.netflix.com"],
                  ["spotify", "https://open.spotify.com"],
                  ["reddit", "https://www.reddit.com"]
                ]                
        matched = False

        # 
        for site in sites:
          if f"open {site[0]}" in query.lower ():
            print(f"MATCHED: {site[0] }")
            say(f"Opening {site[0] }")
            webbrowser.open(site[ 1])
            matched = True
            break


        if not matched:

            # if "open youtube" in query.lower():
            #     say("Opening YouTube")
            #     webbrowser.open("https://www.youtube.com")

         if "open wikipedia" in query.lower():
             say("Opening Wikipedia")
             webbrowser.open("https://www.wikipedia.org")

         elif "open youtube" in query.lower():
            video_query = query.lower().replace("open youtube", "").strip()
            if video_query: 
              say(f"Searching YouTube for {video_query}")
              search_url = f"https://www.youtube.com/results?search_query={video_query.replace(' ', '+')}"
              webbrowser.open(search_url)
            else:
              say("Opening YouTube")
              webbrowser.open("https://www.youtube.com")

         elif "open google" in query.lower():
            say("Opening Google")
            webbrowser.open("https://www.google.com")

         elif "open whatsapp" in query.lower():
            say("Opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com")

         elif "open facebook" in query.lower():
            say("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

         elif "open instagram" in query.lower():
            say("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

         elif "open twitter" in query.lower():
            say("Opening Twitter")
            webbrowser.open("https://www.twitter.com")

         elif "open amazon" in query.lower():
            say("Opening Amazon")
            webbrowser.open("https://www.amazon.in")

         elif "open flipkart" in query.lower():
            say("Opening Flipkart")
            webbrowser.open("https://www.flipkart.com")

         elif "open gmail" in query.lower():
            say("Opening Gmail")
            webbrowser.open("https://mail.google.com")

         elif "open linkedin" in query.lower():
            say("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")

         elif "open stack overflow" in query.lower():
           say("Opening Stack Overflow")
           webbrowser.open("https://stackoverflow.com")

         elif "open chatgpt" in query.lower():
            say("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com")

         elif "open github" in query.lower():
            say("Opening GitHub")
            webbrowser.open("https://github.com")

         elif "open netflix" in query.lower():
            say("Opening Netflix")
            webbrowser.open("https://www.netflix.com")

         elif "open spotify" in query.lower():
            say("Opening Spotify")
            webbrowser.open("https://open.spotify.com")

         elif "open reddit" in query.lower():
            say("Opening Reddit")
            webbrowser.open("https://www.reddit.com")

         elif "open music" in query.lower():
            musicPath = "C:\\Users\\Username\\Music\\example.mp3"  # Replace with valid path
            if os.path.exists(musicPath):
                os.startfile(musicPath)
            else:
                say("Music file not found.")

         elif "the time" in query.lower():
            now = datetime.datetime.now()
            say(f"Sir, the time is {now.hour} hours and {now.minute} minutes")

         elif "open notepad" in query.lower():
            os.system("start notepad")

         elif "open calculator" in query.lower():
            os.system("start calc")

         elif "using ai" in query.lower():
             # creating openai messages
             messages = [{"role": "system", "content": "You are a helpful assistant."},
                         {"role": "user", "content": query},]
             
             ai(messages=messages)
             


         elif "jarvis quit" in query.lower():
            say("Goodbye sir.")
            exit()

         elif "reset chat" in query.lower():
            chatStr = ""
            say("Chat history reset.")

         else:
            # print("Chatting...")
            # chat(query)
            pass


        