import reactpy as rp
import requests

# Función para obtener los datos de un API (en este caso, una lista de usuarios)
def fetch_users():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Componente de ReactPy para mostrar la lista de usuarios
@rp.component
def UserList():
    # Estado que contiene los datos de los usuarios
    users, set_users = rp.hooks.use_state([])

    # Al montar el componente, obtenemos los datos del API
    @rp.hooks.use_effect
    def load_users():
        set_users(fetch_users())

    # Si no hay usuarios, mostramos un mensaje de carga
    if not users:
        return rp.html.p({"style": {"color": "blue"}}, "Cargando...")

    # Retornamos la lista de usuarios
    return rp.html.ul(
        [
            rp.html.li({"key": user["id"]}, f'{user["name"]} - {user["email"]}')
            for user in users
        ]
    )

# Crear un contenedor y montar la aplicación
rp.run(UserList)
