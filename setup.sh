mkdir -p ~/.streamlit/
echo [$(date)]: "START"
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment" 
source activate ./env
echo [$(date)]: "installing the dev requirements" 
pip install -r requirements.txt
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
