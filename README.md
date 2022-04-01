![logotipo](MercadoLibre.jpg)

# Buscador de alquileres 

Programa que se utiliza para buscar alquileres en mercadolibre y generar un reporte web. Se puede filtrar por barrio para especificar la busqueda y obtener un reporte de las propiedades valuadas en dolares y en pesos


# Funcionamiento del sistema
Se consumen los datos de la api de MercadoLibre, pasandole un barrio como parametro al url a traves de un formulario de HTML. Luego el sistema carga los datos a una base de datos y los muestra en una tabla.
De ahi el usuario puede filtrar la busqueda para que muestre solo las propiedades en pesos o en dolares.

Ademas hay 3 endpoints disponibles que muestran distintos graficos de torta. 
- "/alquileres/comparativa" muestra la comparacion entre la cantidad de propiedades en pesos y la cantidad de propiedades en dolares
- "/alquileres/comparativa/pesos" muestra la cantidad de propiedades cuyos precios estan dentro de un rango determinado (en pesos)
- "/alquileres/comparativa/dolares" muestra la cantidad de propiedades cuyos precios estan dentro de un rango determinado (en dolares)





## Version 1.1

## Autor
Lautaro Gerlero
