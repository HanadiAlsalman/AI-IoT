

import boto3
import os

# Ange din AWS-region
region = "eu-north-1"  # Uppdatera med din faktiska region

# Initiera Rekognition-klienten
rekognition_client = boto3.client("rekognition", region_name=region)

def detect_labels(image_path):
    # Kontrollera om filen finns
    if not os.path.exists(image_path):
        print(f"Fel: Bilden '{image_path}' hittades inte.")
        return

    try:
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        response = rekognition_client.detect_labels(
            Image={"Bytes": image_bytes},
            MaxLabels=5,  # Justera vid behov
        )

        print("\n** Upptäckta etiketter **")
        for label in response["Labels"]:
            print(f"Etikett: {label['Name']} (Tillförlitlighet: {label['Confidence']:.2f}%)")

    except Exception as e:
        print(f"Ett fel uppstod: {e}")

# Ange din bildsökväg
image_path = "/path/to/your/image.jpg"  # Uppdatera sökvägen
detect_labels(image_path)
