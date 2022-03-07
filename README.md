# ✨ Low Light Image Enhancer 🖼 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A simple streamlit based webapp to process and enhance low-light images using Keras MIRNet.

![1](https://user-images.githubusercontent.com/29462447/157028560-02fcb630-dff7-4775-8ea2-0557c5b8b1b4.gif)
![2](https://user-images.githubusercontent.com/29462447/157029029-0ceca57d-1e69-4e06-8397-fee750db467d.gif)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Simply run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading audio files, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```
![1](https://user-images.githubusercontent.com/29462447/157025555-2088b55f-98e0-45ad-839a-e95d240be7ab.png)
![1 1](https://user-images.githubusercontent.com/29462447/157025519-ce182afb-be49-425e-be65-0ed773009002.png)
![1 2](https://user-images.githubusercontent.com/29462447/157025539-42b38c96-b284-4de5-9766-ffce076bbbb5.png)
![2](https://user-images.githubusercontent.com/29462447/157025481-6fd9bfc1-04b9-4bfd-94a9-907f3950caba.png)


## Results:
| **Original Low-Light Image**  | **Enhanced Image**  |
|--------------------------|-------------------------------------|
| ![pic1](uploads/55.png)  | ![pic1](downloads/enhanced_55.png)  |
| ![pic2](uploads/79.png)  | ![pic2](downloads/enhanced_79.png)  |
| ![pic3](uploads/547.png) | ![pic3](downloads/enhanced_547.png) |
| ![pic4](uploads/665.png) | ![pic4](downloads/enhanced_665.png) |
| ![pic4](uploads/778.png) | ![pic4](downloads/enhanced_778.png) |

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
