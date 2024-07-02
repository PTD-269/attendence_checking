from deepface import DeepFace
import numpy as np
import cv2
import os
def detect(img):
    nparr = np.frombuffer(img, np.uint8)
    image_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    models = [
        "VGG-Face", 
        "Facenet", 
        "Facenet512", 
        "OpenFace", 
        "DeepFace", 
        "DeepID", 
        "ArcFace", 
        "Dlib", 
        "SFace",
        "GhostFaceNet",
    ]

    #Convert ndarray to image file
    img_path = "temp_img.jpg"
    cv2.imwrite(img_path, image_np)

    dfs = DeepFace.find(
        img_path=img_path,
        db_path= f"/Users/phamdat/Documents/AI/model/database", 
        model_name=models[1],
        threshold=1,
        enforce_detection=False
        )
    df = dfs[0]
    min_distance = df['distance'].min()

    # Filter the DataFrame to get rows with the minimum distance
    result = df[df['distance'] == min_distance]
    # Extract the identity values
    identities:list[str] = result['identity'].tolist()
    name = identities[0].split('/')[-2]
    # print("Identities with lowest distance:")
    # for identity in identities:
    #     print(identity.split('/')[-2])
    
    #Remove temporary image file
    os.remove(img_path)
    
    return {'name':name}


def main():
    import numpy as np

    # Create a simple grayscale image as a NumPy ndarray
    image_height = 100
    image_width = 100
    image = np.zeros((image_height, image_width), dtype=np.uint8)

    # Draw a white rectangle in the center
    rectangle_top_left = (25, 25)
    rectangle_bottom_right = (75, 75)
    image[rectangle_top_left[1]:rectangle_bottom_right[1], rectangle_top_left[0]:rectangle_bottom_right[0]] = 255


    # Now you can use this `image` ndarray in your `detect` function
    detect(image)



if __name__ == "__main__":
    main()
