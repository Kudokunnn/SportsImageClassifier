import numpy as np
import tensorflow as tf

classes = [
    "air hockey",
    "ampute football",
    "archery",
    "arm wrestling",
    "axe throwing",
    "balance beam",
    "barell racing",
    "baseball",
    "basketball",
    "baton twirling",
    "bike polo",
    "billiards",
    "bmx",
    "bobsled",
    "bowling",
    "boxing",
    "bull riding",
    "bungee jumping",
    "canoe slamon",
    "cheerleading",
    "chess",    
    "chuckwagon racing",
    "cricket",
    "croquet",
    "curling",
    "dance sports",
    "disc golf",
    "esport",
    "fencing",
    "field hockey",
    "figure skating men",
    "figure skating pairs",
    "figure skating women",
    "fly fishing",
    "football (US)",
    "formula 1 racing",
    "frisbee",
    "gaga",
    "giant slalom",
    "golf",
    "hammer throw",
    "hang gliding",
    "harness racing",
    "high jump",
    "hockey",
    "horse jumping",
    "horse racing",
    "horseshoe pitching",
    "hurdles",
    "hydroplane racing",
    "ice climbing",
    "ice yachting",
    "jai alai",
    "javelin",
    "jousting",
    "judo",
    "kayaking",
    "lacrosse",
    "log rolling",
    "luge",
    "motorcycle racing",
    "mushing",
    "nascar racing",
    "olympic wrestling",
    "paintball",
    "parallel bar",
    "parkour",
    "poker",
    "pole climbing",
    "pole dancing",
    "pole vault",
    "polo",
    "pommel horse",
    "rings",
    "rock climbing",
    "roller derby",
    "rollerblade racing",
    "rowing",
    "rugby",
    "sailboat racing",
    "sandboarding",
    "scuba diving",
    "shot put",
    "shuffleboard",
    "sidecar racing",
    "ski jumping",
    "sky surfing",
    "skydiving",
    "snow boarding",
    "snowmobile racing",
    "soccer",   
    "speed skating",
    "steer wrestling",
    "sumo wrestling",
    "surfing",
    "swimming",
    "table tennis",
    "tennis",
    "track bicycle",
    "trapeze",
    "tug of war",
    "ultimate",
    "uneven bars",
    "volleyball",
    "water cycling",
    "water polo",
    "weightlifting",
    "wheelchair basketball",
    "wheelchair racing",
    "wingsuit flying",
]


def predict_label(img, model, classes):
    try:
        # Resize the image to (224, 224)
        resized_img = tf.image.resize(img, (224, 224))
        exp_img = np.expand_dims(resized_img, axis=0)

        # Predict with the model
        y_prob = model.predict(exp_img)
        max_prob = np.max(y_prob)  # Get the maximum probability

        if max_prob < 0.5:
            return "Cannot predict. Please input an appropriate image.", None  # No label, just a message
        else:
            y_classes = y_prob.argmax(axis=-1)
            label = classes[y_classes[0]]

            # Convert max_prob to a percentage and round to 2 decimal places
            accuracy_percentage = round(max_prob * 100, 2)

            # After rounding, convert to string and append the '%' symbol
            accuracy_percentage_str = f"{accuracy_percentage}%"
            return label.capitalize(), accuracy_percentage_str  # Return both label and accuracy percentage string

    except Exception as e:
        return f"An error occurred: {e}", None











