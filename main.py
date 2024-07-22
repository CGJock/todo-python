import requests
api_url = ("http://localhost:3000/tasks")

def get_data():
  response = requests.get(api_url)
  data = response.json()
  return data

def post():
  new_task = {}
  

def show_task(data):
  user = input("Digite el nombre del usuario: ")
  print(f"Bienvenido {user},")
  show = input("Deseas ver la lista de tus tareas? (Y),(N): ")
  if show.lower() == "y":
    for e in data:
      print(f"Titulo Tarea: {e["title"]}, Descripcion Tarea: {e["description"]}")
      
    
show_task(get_data())