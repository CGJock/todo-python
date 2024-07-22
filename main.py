import requests
api_url = ("http://localhost:3000/tasks")#constante con el valor de la api

def get_data():
  response = requests.get(api_url)#se utiliza request.get para hacer el get
  data = response.json()
  if response.status_code == 201:
    print("Exito al traer las tareas!")#bloque de codigo para manejar los errores
  else:
    print("Error en el servidor 202")
  return data

def post(t_title,t_description):
  new_task = {"title" : t_title, "description" : t_description}#se guardan los valores del input en un dic
  response = requests.post(api_url, json = new_task)
  
  if response.status_code == 201:
    print("Se agrego la tarea con exito!")#bloque de codigo para manejar los errores
  else:
    print("error al agregar la tarea")
    
def show_data(data):
  for e in data:
    #las comillas dentro de comillas deben ser simples para evitar errores de syntaxis
    print(f"Titulo Tarea: {e['title']}")
    print(f"Descripcion: {e['description']}")
  

def show_task():
  data = get_data()
  user = input("Digite el nombre del usuario: ")
  print(f"Bienvenido {user},")
  
  show = input("Deseas ver la lista de tus tareas? (Y),(N): ")
  if show.lower() == "y":
    show_data(data)
      
  if show not in ["y","n"]:
    print(f"Digita una opcion valida: (Y),(N)")
    
  elif show.lower() == "n":
    exit()
    
  task_input = input("Deseas agregar una nueva tarea? (Y),(N):  ")
  if task_input.lower() not in ["y","n"]:
    print(f"Selecciona una opcion correcta: (Y),(N)")
  
  if task_input.lower() == "y":
    t_title = input("Digita el titulo: ")
    t_description = input("Digita la descripcion : ")
    
    post(t_title,t_description)#se hace el post con los parametros
    show_data(data)
    
show_task()