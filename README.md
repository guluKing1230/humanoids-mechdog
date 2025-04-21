# humanoids-mechdog
Integration of modules and development with HiWonder MechDog starter model.
Implemented features including:
  - **Touch Sensor**: Change movements when the dog is touched.
  - **Light Sensor**: Change the LED display according to the light conditions.
  - **Distance Sensing**: Use ultrasonic sensor to detect the distance and use matrix display to show the number.
  - **Obstacle Avoidance and Alarm**: Automatically change directions when there are obstacles too close ahead. Use the buzzer to alarm, where the frequency is determined by the distance to the obstacle.
  - **ESP32-S3 AI Vision Module Integration**: We include the vision module to achieve the following functionalities:
      - Color Detection
      - Color Following (also line following)
      - Face recognition
