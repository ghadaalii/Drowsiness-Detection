import pyttsx3

# MediaPipe configurations
STATIC_IMAGE = False
MAX_NO_FACES = 2
DETECTION_CONFIDENCE = 0.6
TRACKING_CONFIDENCE = 0.5

# Colors
COLOR_RED = (0, 0, 255)
COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# Landmark indices
LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95,
        185, 40, 39, 37, 0, 267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]

RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]

LEFT_EYE_TOP_BOTTOM = [386, 374]
LEFT_EYE_LEFT_RIGHT = [263, 362]

RIGHT_EYE_TOP_BOTTOM = [159, 145]
RIGHT_EYE_LEFT_RIGHT = [133, 33]

UPPER_LOWER_LIPS = [13, 14]
LEFT_RIGHT_LIPS = [78, 308]

FACE = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400,
        377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]

# Thresholds
MIN_FRAME = 6
MIN_TOLERANCE = 4.0

# Pyttsx3 initialization
speech_engine = pyttsx3.init()

