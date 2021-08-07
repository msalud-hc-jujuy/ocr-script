# OCR Script

El presente repositorio es un simple script en python que hace uso de la libreria __ocrmypdf__ para otorgar capacidad de busqueda a documentos pdf escaneados.

## Requerimientos

__In addition to the required Python version (3.6+), OCRmyPDF requires external program installations of Ghostscript, Tesseract OCR, QPDF, and Leptonica. OCRmyPDF is pure Python, but uses CFFI to portably generate library bindings. OCRmyPDF works on pretty much everything: Linux, macOS, Windows and FreeBSD.__ Fuente: [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF)

Opcionalmente, se añade un Dockerfile y docker-compose.yml, por lo que se agregan como requerimiento tener instalado docker y docker-compose.

## Ejecución

```bash
# python

python main.py

# docker

docker build -t custom-ocr:v0.1 .
docker run custom-ocr:v0.1 .

# docker-compose
docker-compose build
docker-compose up
```


## Documentación

La documentación oficial de la libreria __ocrmypdf__ está disponible en el siguiente [link](https://ocrmypdf.readthedocs.io/en/latest/).