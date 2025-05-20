from PIL import Image

# Optimizar imagen
def optimizar_imagen(sender, instance, **kwargs):
    print(' ================ ')
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=50, optimize=True)
    