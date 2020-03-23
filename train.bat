call C:\Users\User\AppData\Local\Programs\Python\Python36\python.exe C:\tensorflow1\models\research\object_detection\images1\transform_image_resolution.py -d C:\tensorflow1\models\research\object_detection\images1\test\ -s 800 600

call chdir /d C:\tensorflow1

call chdir /d C:\tensorflow1\models\research\object_detection

call C:\Users\User\AppData\Local\Programs\Python\Python36\python.exe C:\tensorflow1\models\research\object_detection\xml_to_csv.py

call chdir /d C:\tensorflow1

call C:\Users\User\AppData\Local\Programs\Python\Python36\python.exe C:\tensorflow1\models\research\object_detection\generate_tfrecord.py --csv_input=C:\tensorflow1\models\research\object_detection\images\train_labels.csv --image_dir=C:\tensorflow1\models\research\object_detection\images\train --output_path=C:\tensorflow1\models\research\object_detection\train.record

call C:\Users\User\AppData\Local\Programs\Python\Python36\python.exe C:\tensorflow1\models\research\object_detection\generate_tfrecord.py --csv_input=C:\tensorflow1\models\research\object_detection\images\test_labels.csv --image_dir=C:\tensorflow1\models\research\object_detection\images\test --output_path=C:\tensorflow1\models\research\object_detection\test.record


call C:\Users\User\AppData\Local\Programs\Python\Python36\python.exe C:\tensorflow1\models\research\object_detection\train.py --logtostderr --train_dir=C:\tensorflow1\models\research\object_detection\training\ --pipeline_config_path=C:\tensorflow1\models\research\object_detection\training/faster_rcnn_inception_v2_pets.config
