import requests

def trivia_fetch(num):
    url = f"https://opentdb.com/api.php?amount={num}"
    response = requests.get(url)
    trivia = response.json()
    trivia["number"] = num
    return trivia

def test_trivia_42():
    assert trivia_fetch(42)['number'] == 42

def test_trivia_1000():
    assert trivia_fetch(1000)['number'] == 1000

def main():
  cantidad= int(input("¿cuantas preguntas quieres? "))
  trivia = trivia_fetch(cantidad)

  for pregunta in trivia["results"]:
      print(pregunta["question"])

if __name__=="__main__":
  main()
  test_trivia_42()
  test_trivia1000()
