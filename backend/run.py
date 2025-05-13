#! /usr/bin/env python
from app import app, Config, Mqtt
from csvCrops import insertCrop, deleteCrop
import os



if __name__ == "__main__":   

    # START MQTT CLIENT 
    file_size = os.path.getsize("Crop_recommendation.csv")
    if file_size == 0:
        print("The file is empty. Please check the file.")
    else:
        print("The file is not empty. Proceeding with the next steps.")

    # Check if the file size has changed
    flag_file_path = "crop_inserted.flag"
    if os.path.exists(flag_file_path):
        with open(flag_file_path, "r") as flag_file:
            previous_size = int(flag_file.read().strip())
        if previous_size != file_size:
            print("File size has changed. Re-running insertCrop.")
            deleteCrop()
            insertCrop()
            with open(flag_file_path, "w") as flag_file:
                flag_file.write(str(file_size))
    else:
        with open(flag_file_path, "w") as flag_file:
            flag_file.write(str(file_size))
            insertCrop()
    
    Mqtt.client.loop_start()

    # RUN FLASK APP
    app.run(debug=Config.FLASK_DEBUG, host=Config.FLASK_RUN_HOST, port=Config.FLASK_RUN_PORT)
    