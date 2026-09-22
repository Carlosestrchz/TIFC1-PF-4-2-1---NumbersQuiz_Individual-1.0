import requests

def trivia_fetch(num):
    url = f"https://opentdb.com/api.php?amount={num}"
    response = requests.get(url)
    trivia = response.json()
    return trivia

def main():
  cantidad= int(input("¿cuantas preguntas quieres? "))
  trivia = trivia_fetch(cantidad)

  for pregunta in trivia["results"]:
      print(pregunta["question"])

if __name__=="__main__":
  main()
