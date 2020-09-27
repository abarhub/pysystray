Compress-Archive -Path main.py -DestinationPath pysystray-1.0.0-test.zip
Compress-Archive -Path config.yml -Update -DestinationPath pysystray-1.0.0-test.zip
Compress-Archive -Path install.bat -Update -DestinationPath pysystray-1.0.0-test.zip
Compress-Archive -Path requirements.txt -Update -DestinationPath pysystray-1.0.0-test.zip
Compress-Archive -Path run.bat -Update -DestinationPath pysystray-1.0.0-test.zip

