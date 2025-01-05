import openai
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Returns text from OpenAI based off of prompt
def AiGeneration(): 
  # API key
  openai.api_key = "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"
  
  #Model Engine
  model_engine = "gpt-3.5-turbo-instruct"
  prompt = "Generate a very creative and random comment. It can be mean, funny, gross, weird, extreme or scary. The comment would take place in a video game or fantasy world."
  temperature = 1.5
  max_tokens = 150
  
  # Generate comment using the OpenAI API
  response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=temperature,
      max_tokens=max_tokens,
      n=1,
      stop=None,
  )
  # Print comment
  comment = response.choices[0].text.strip()
  return comment

#Stores a functions sent messagea to txt every 30 minutes
def store_responses_periodically(function , filename="CODING/responses.txt", interval=9000):
    
    from_email = "goob.robot@gmail.com"
    to_email = "TO EMAIL"
    subject = "YOU HAVE AN IMPORTANT MESSAGE FROM GOOB BOT!"
    message = ""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "goob.robot@gmail.com"
    password = "PASSWORD"

    #Sends  email upon request
    def send_email(from_email, to_email, subject, message, smtp_server, smtp_port, login, password):
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection
            server.login(login, password)
            server.send_message(msg)
            server.quit()
            print("/////////////////////////////////////////////////////////////////////////////////////////////////////////\nEmail sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    """
    Stores responses from a function call in a text file every `interval` seconds.

    Parameters:
    - function (callable): The function to call for getting responses.
    - filename (str): Name of the file where responses will be saved. Default is 'responses.txt'.
    - interval (int): Time interval between calls in seconds. Default is 300 (5 minutes).

    Returns:
    None
    """
    ticker = 0 
    
    try:
        while True:
            # Call the function to get the response
            response = function()
            
            # Write the response to the file
            with open(filename, "a") as file:  # Append mode to preserve earlier responses
                file.write(response + "\n")
            
            ticker += 1
            message = f"///////////////////////////////////////////////////////////////////////////////////////////////////////// \n*  -  *  - GOOB SAYS -  *  -  *  \n ///////////////////////////////////////////////////////////////////////////////////////////////////////// \n\n {response} \n\n ///////////////////////////////////////////////////////////////////////////////////////////////////////// \n {ticker} RESPONSES GENERATED THIS SESSION.\n/////////////////////////////////////////////////////////////////////////////////////////////////////////"

            send_email(from_email, to_email, subject, message, smtp_server, smtp_port, login, password)
            print(f"///////////////////////////////////////////////////////////////////////////////////////////////////////// \n-                                   *  -  *  - GOOB SAYS -  *  -  *  \n ///////////////////////////////////////////////////////////////////////////////////////////////////////// \n\n {response} \n\n ///////////////////////////////////////////////////////////////////////////////////////////////////////// \n                                  {ticker} RESPONSES GENERATED THIS SESSION.\n/////////////////////////////////////////////////////////////////////////////////////////////////////////")
            # Wait for the specified interval
            time.sleep(interval)
    except KeyboardInterrupt:
        print("                                      GOOB BOT HAS STOPPED")
    except Exception as e:
        print(f"                                      ERROR : {e}")

#Call the function
store_responses_periodically(AiGeneration)

