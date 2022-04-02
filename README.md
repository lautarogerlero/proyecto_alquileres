![logotipo](MercadoLibre.jpg)

# Buscador de alquileres 

Programa que se utiliza para buscar alquileres en mercadolibre y generar un reporte web. Se puede filtrar por ciudad para especificar la busqueda y obtener un reporte de las propiedades valuadas en dolares y en pesos


# Funcionamiento del sistema

Para empezar el usuario elige un barrio para efectuar la busqueda. El programa toma el barrio elegido, se consumen los datos de la api de MercadoLibre y se crea una base de datos con los departamentos que están en ese barrio. Luego el sistema muestra los datos en una tabla y el usuario puede filtrar la busqueda para que muestre solo las propiedades en pesos o en dolares.

Ademas hay 3 endpoints disponibles que muestran distintos graficos de torta.  
- "/comparativa" muestra la comparacion entre la cantidad de propiedades en pesos y la cantidad de propiedades en dolares.  
- "/comparativa/pesos" muestra la cantidad de propiedades cuyos precios estan dentro de un rango determinado (en pesos).  
- "/comparativa/dolares" muestra la cantidad de propiedades cuyos precios estan dentro de un rango determinado (en dolares).





## Version 1.0

## Autor
Lautaro Gerlero
