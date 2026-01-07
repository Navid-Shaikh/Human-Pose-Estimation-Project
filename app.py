import cv2
import mediapipe as mp

# MediaPipe setup
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# Screen and window settings
SCREEN_WIDTH = 1920   # Your screen width
SCREEN_HEIGHT = 945   # Your screen height
WINDOW_NAME = 'Human Pose Estimation - MediaPipe (Press ESC to quit | F to toggle fullscreen)'

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set higher webcam resolution for better accuracy
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Create resizable window
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

# Start with full screen
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Pose estimation with high accuracy settings
with mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,                    # Highest accuracy model (more precise landmarks)
    smooth_landmarks=True,                # Reduces jitter and improves stability
    min_detection_confidence=0.7,         # Higher threshold = fewer false detections
    min_tracking_confidence=0.7           # Better tracking across frames
) as pose:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Resize image to fill your screen (improves visual quality)
        image = cv2.resize(image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Flip horizontally for selfie view
        image = cv2.flip(image, 1)

        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the frame
        results = pose.process(image_rgb)

        # Draw pose landmarks if detected
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )

        # Display the result
        cv2.imshow(WINDOW_NAME, image)

        # Key controls
        key = cv2.waitKey(5) & 0xFF
        if key == 27:  # ESC key to quit
            break
        elif key == ord('f') or key == ord('F'):  # Toggle fullscreen
            current = cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
            new_mode = cv2.WINDOW_NORMAL if current == cv2.WINDOW_FULLSCREEN else cv2.WINDOW_FULLSCREEN
            cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, new_mode)

# Cleanup
cap.release()
cv2.destroyAllWindows()
