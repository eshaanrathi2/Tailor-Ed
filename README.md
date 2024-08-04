# Tailor-Ed
https://tailored.education/


Dependencies:
- ```pip install -r requirements.txt``` (recommended to create and activate a python virtual env before running this step)
- ollama (https://ollama.com/download)
- after installing ollama, language models such as phi3 can be installed as ```ollama install phi3```

Steps:
- RAG: retrieve relavant information for each query and add it to ```secondary_data.json``` file.
- Use a language model such as phi3 to extract very specific information from the above retrieved text.


<!-- Environment setup instructions can be found in llama-cpp-python docs:
```
https://github.com/abetlen/llama-cpp-python/blob/main/docs/install/macos.md
``` -->

<!-- Create conda environment
```
conda create --name env
```

Activate venv
```
conda activate env
``` -->

<!-- Install requirements -->
<!-- pip install package_name -->
<!-- pip install --upgrade --quiet  -->
<!-- ```
pip install -r requirements.txt
``` -->

<!-- Download Llama2 on local machine (llama-2-7b.Q4_K_S.gguf from Huggingface):
```
huggingface-cli download TheBloke/Llama-2-7B-GGUF llama-2-7b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
``` -->