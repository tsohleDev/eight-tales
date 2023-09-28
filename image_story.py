from transformers import pipeline

def image_to_text(url):
    image_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    return image_pipeline(url)[0]['generated_text']

print(image_to_text('man.jpg'))
