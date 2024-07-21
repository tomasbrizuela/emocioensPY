import openai

openai.api_key = "Api Key goes here"

text = input("Escribi lo que sentis: ")

conversation = [
    {
        "role": "system", "content": "Sos un psicologo con más de 30 años de experiencia atentiendo pacientes en consulta. El usuario te va a dar un texto contándote como se siente, y vos tenés que responderle con 5 palarbas, separadas por coma, que representen las emcoiones por las que estás pasando. Es muy importante que respetes las 5 palabras separadas por coma. Una palabra por emoción."
    },
    {
        "role": "user", "content": text
    },
    ]

response = openai.ChatCompletion.create(
messages=conversation,
model="gpt-4o-mini"
)

print(response.choices[0].message.content)

