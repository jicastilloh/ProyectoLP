# autor: Junior Castillo - jicastilloh@unah.hn
# version: 0.0.4

rm -r ./HTML_Descargadas/*
rm ./solverP.pl

archivo_de_urls="./$1" # Guardamos la ruta del archivo

count=1 # Creamos un contador que servirá para los nombres de los archivos '.html' que descargaremos

# Recorremos cada línea del archivo que contiene las URLs
while read url; do
    curl -o ./HTML_Descargadas/url$count.html "$url" # Con el comando 'curl' y el parámetro '-o' especificamos la ruta donde queremos descargar el archivo junto con su nombre y también especificamos la url del archivo a descargar
    count=$(($count+1)) # Incrementamos el contador
done < "$archivo_de_urls"

curl -o ./HTML_Descargadas/url$count.html "$url" #Hacemos lo mismo que hicimos dentro del ciclo para la última URL

# python3 ./Código/Proyecto/process.py ./Código/Proyecto/Enlaces/URLs.txt
python3 ./process.py $archivo_de_urls