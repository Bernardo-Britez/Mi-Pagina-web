
from flask import Flask, render_template 

 
# Crea una instancia de la aplicación Flask 
app = Flask(__name__) 

 
# Define una ruta para la página de inicio 
@app.route('/') 
def index(): 
    return "<h1> hola curso </p> " 

 
# Define una ruta para una página con un nombre dinámico 
@app.route('/saludar/<nombre>') 
def saluda_alumno(nombre): 
    return f"<h1>¡Hola, {nombre.capitalize()}!</h1><p>Bienvenido a mi página Flask.</p>" 
 
# Define una ruta para una página usando una plan lla HTML 
@app.route('/plantilla') 
def mostrar_plantilla(): 
    # Renderiza un archivo HTML (lo crearemos en el siguiente paso) 
    return render_template('../ejemplo.html', tulo="Mi Página con Html", mensaje="Este contenido viene de Flask.") 
 
# Este bloque asegura que el servidor se ejecute solo cuando el script es ejecutado directamente 
if __name__ == '__main__': 
    app.run(debug=True) # debug=True permite recargar el servidor automá camente al hacer cambios 

 
