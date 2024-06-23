
jl_src(){ echo "source $HOME/d/d4jl/jl.sh" ; }
jl_src_(){ $(jl_src) ; }
jl___(){ $(jl_src) ; }
jl0(){ conda deactivate ; }

#
#
#
jl_loc=$HOME/.jupyter
jl_bash=/opt/homebrew/bin/bash
jl_kode=$HOME/d2/s4/m7/k_/k2
jl_home=$HOME
jl_ver='240608'
jl0='j9'
jl1="j9991_${jl_ver}"
jl2="j9992_${jl_ver}"
jl3="j9993_${jl_ver}"
jl1_loc=$jl_loc/$jl1
jl2_loc=$jl_loc/$jl2
jl3_loc=$jl_loc/$jl3
jl1_ws=$jl1_loc/workspaces
jl2_ws=$jl2_loc/workspaces
jl3_ws=$jl3_loc/workspaces
jl1_usr=$jl1_loc/user-settings
jl2_usr=$jl2_loc/user-settings
jl3_usr=$jl3_loc/user-settings
jl1_port=9991
jl2_port=9992
jl3_port=9993


# ==================================================
# []
# ==================================================

jl_help() {
  uid=${FUNCNAME[0]}

  # echo -n "Executing $uid "
  case $@ in
    ${uid} )
      echo " >>>> ${uid} "
      echo "conda env list"
      echo "conda create -n ${jl1} --clone ${jl0}"
      echo "conda create -n ${jl2} --clone ${jl0}"
      echo "  "
      which conda
      echo "jl_kode : ${jl_kode}"
    ;;
    ${uid}_ )
      echo ${uid}
    ;;
    ${uid}__ )
      echo ${uid}
    ;;
    ${uid}___ )
      echo ${uid}
    ;;
  esac
}


# /opt/homebrew/anaconda3/envs/j8clc1/share/jupyter/kernels/python3
jl_setup(){
	echo "python -m ipykernel install --user --name j8c"
}


jp_path(){ jupyter --path ; }
jp_version(){ jupyter --version ; }
jp_list() { echo 'jupyter server list' ; }
jp_list_() {
  eval "$($(which conda) 'shell.bash' 'hook')" && conda activate $jl1 && jupyter server list
}

jp_ks_help(){ jupyter kernelspec ; }
jp_ks_help_(){ $(jp_ks_help) ; }
jp_ks_list(){	jupyter-kernelspec list ; }
jp_ks_list_(){ $(jp_ks_list) ; }
jp_ks0(){ jupyter kernelspec uinstall kernelName ; }
jp_ks_del(){ echo "jupyter kernelspec uninstall <kernel_name> "; }


jl1(){
	echo "conda activate ${jl1} && \
export SHELL=${jl_bash} && \
export JUPYTERLAB_SETTINGS_DIR=${jl1_usr} && \
export JUPYTERLAB_WORKSPACE_DIR=${jl1_ws} && \
jupyter-lab --port=${jl1_port} --no-browser --notebook-dir=$HOME "
}
#	--ip='*' \
#	--NotebookApp.token='' \
#	--NotebookApp.password='' \
#	--ContentsManager.allow_hidden=True \


jl1_(){
	eval "$($(which conda) 'shell.bash' 'hook')" && conda activate $jl1 && \
export SHELL=$jl_bash && \
export JUPYTERLAB_SETTINGS_DIR=$jl1_usr && \
export JUPYTERLAB_WORKSPACE_DIR=$jl1_ws && \
jupyter-lab --port=$jl1_port --no-browser --notebook-dir=$HOME 
}

jl1__(){
	eval "$($(which conda) 'shell.bash' 'hook')"
	$(jl1) ;
}

jl1_acd_env(){ eval "$($(which conda) 'shell.bash' 'hook')" && conda activate ${jl1} ; }

jl1_del(){	echo "conda env remove --name ${jl1} " ; }
jl1_del_(){ $(jl_del) ; }
jl1_del_new(){ echo " conda create --name ${jl1} --clone ${jl0}  " ; }
jl1_del_new_(){	$(jl1_new) ; }
jl1_del_new_pip(){ echo "pip install jupyter ipykernel" ; }
jl1_del_new_pip_(){
	conda deactivate
	conda activate ${jl1}
	eval "$($(which conda) 'shell.bash' 'hook')"
	$(jl1_del_new_pip)
}



#
# []
#
jl2(){
	echo "conda activate $jl2 && \
export SHELL=$jl_bash && \
export JUPYTERLAB_SETTINGS_DIR=$jl2_usr && \
export JUPYTERLAB_WORKSPACE_DIR=$jl2_ws && \
jupyter-lab --port=$jl2_port --no-browser --notebook-dir=$HOME "
}
#	--ip='*' \
#	--NotebookApp.token='' \
#	--NotebookApp.password='' \
#	--ContentsManager.allow_hidden=True \

jl2_(){
	eval "$($(which conda) 'shell.bash' 'hook')"
	conda activate $jl2 && \
export SHELL=$jl_bash && \
export JUPYTERLAB_SETTINGS_DIR=$jl2_usr && \
export JUPYTERLAB_WORKSPACE_DIR=$jl2_ws && \
jupyter-lab --port=$jl2_port --no-browser --notebook-dir=$HOME 
}
#	--ip='*' \
#	--NotebookApp.token='' \
#	--NotebookApp.password='' \
#	--ContentsManager.allow_hidden=True \

jl2_del(){	echo "conda remove --name ${jl2} " ; }

jl2_del_(){ 
	which conda
	conda deactivate
	$(jl2_del)
} 

jl2_del_new(){ echo " conda create --name ${jl2} --clone ${jl0} " ; }

jl2_del_new_(){ $(jl2_del_new) ; }

jl2_del_new_pip(){ echo "pip install jupyter ipykernel" ; }

jl2_del_new_pip_(){
	conda deactivate
	conda activate ${jl2}
	eval "$($(which conda) 'shell.bash' 'hook')"
	$(jl1_del_new_pip)
}

jl3(){
	echo "conda activate $jl3 ; "
	echo " export SHELL=${jl_bash} && \
export JUPYTERLAB_SETTINGS_DIR=$jl3_usr && \
export JUPYTERLAB_WORKSPACE_DIR=$jl3_ws && \
jupyter-lab --port=$jl3_port --no-browser --notebook-dir=$HOME "
}

jl3_(){
	conda activate $jl3
	eval "$($(which conda) 'shell.bash' 'hook')"
	export SHELL=/opt/homebrew/bin/bash && \
	export JUPYTERLAB_SETTINGS_DIR=${jl3_lst[1]} && \
	export JUPYTERLAB_WORKSPACE_DIR=${jl3_lst[0]} && \
	jupyter-lab --port=$jl2_port --no-browser --notebook-dir=$HOME
}



jl3_del(){	echo "conda remove --name ${jl3} " ; }

jl3_del_(){ 
	which conda
	conda deactivate
	$(jl3_del)
} 

jl3_del_new(){ echo " conda create --name ${jl3} --clone ${jl0} " ; }

jl3_del_new_(){ $(jl3_del_new) ; }

jl3_del_new_pip(){ echo "pip install jupyter ipykernel" ; }

jl3_del_new_pip_(){
	conda deactivate
	conda activate ${jl3}
	eval "$($(which conda) 'shell.bash' 'hook')"
	$(jl1_del_new_pip)
}

jl3_ks_lst(){ 	echo "hi" ; }
jl3_ks_del(){	jupyter kernelspec uninstall j8a ; }





jl1_on(){
    uid=${FUNCNAME[0]}
    # echo " >>>> $uid  "

    case $@ in
        ${uid} )
        echo ${jl1}
        JUPYTERLAB_SETTINGS_DIR=${jl1_usr}
        JUPYTERLAB_WORKSPACE_DIR=${jl1_ws}
        echo notebook-dir : ${jl1}
        echo port         : ${jl1_port}
        echo notebook-dir : ${jl_kode}
        ;;
        ${uid}_ )
        eval "$($(which conda) 'shell.bash' 'hook')" && conda activate ${jl1} && \
export SHELL=${jl_bash} && \
export JUPYTERLAB_SETTINGS_DIR=${jl1_usr} && \
export JUPYTERLAB_WORKSPACE_DIR=${jl1_ws} && \
jupyter --port=${jl1_port} --NotebookApp.allow_origin='https://colab.research.google.com' --NotebookApp.port_retries=0
# jupyter --port=${jl1_port} --no-browser --notebook-dir=${jl_kode} --NotebookApp.allow_origin='https://colab.research.google.com' --NotebookApp.port_retries=0

        ;;
    esac

}

#
jl_template() {
    uid=${FUNCNAME[0]}
    echo -n " >>>> $uid : "

    case $@ in
        ${uid} )
          echo ${uid}
        ;;
        ${uid}_ )
          echo ${uid}
        ;;
    esac
}


# ==================================================
# []
# source $HOME/d/d4jl/jl0_.sh && jl1
# eval "$($(which conda) 'shell.bash' 'hook')"
# ==================================================
main(){
  jl_help "$@"
  jl1_on "$@"
}
main $@



#
# [] Journey
#

### 24-06

#
# https://docs.vultr.com/how-to-set-up-a-jupyterlab-environment-on-ubuntu-22-04
#


### 12

# https://agent-jay.github.io/2018/03/jupyterserver/
# jupyter notebook --generate-config
# $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mycert.pem -out mycert.pem
# 
# Set options for certfile, ip, password, and toggle off
# browser auto-opening
# c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
# c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mycert.pem'
# Set ip to '*' to bind on all interfaces (ips) for the public server
# c.NotebookApp.ip = '*'
# c.NotebookApp.password = u'sha1:bcd259ccf...<your hashed password here>'
# c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
# c.NotebookApp.port = 9999

#
# https://discourse.jupyter.org/t/multiple-conda-environments/22530
#   sudo /opt/tljh/user/bin/conda create -n env-name python=3.10 
#   ipykernel jupyter
#   conda create -n env-name python=3.10 ipykernel
#   sudo /opt/tljh/user/envs/env-name/bin/python3 -m ipykernel install --name "env-name" --display-name "Env Name in UI" --prefix /opt/tljh/user
#

####

# https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/

####

# http://echrislynch.com/2019/02/01/adding-an-environment-to-jupyter-notebooks/

#### 26

# https://www.youtube.com/watch?v=K7NLegbvbNE
# conda install -c conda-forge nb_conda_kernels
# conda_env
# conda install
# jupyter kernelspec list
# /path/to/kernel/env/bin/python -m ipykernel install \
#  --prefix /path/to/jupyter/env \
#  --name python-my-env \
#  --display-name "Python 3 (other-env)"

# conda install -c anaconda ipykernel
# python -m ipykernel install --user --name=test
# https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook
# conda activate myenv
# pip install ipykernel
# python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
# # python -m ipykernel install --prefix=/cloudclusters/Anaconda3/ --name "python-new-venv"


#### 25

# https://stackoverflow.com/questions/68935932/install-python2-on-mac-with-m1-chip


#### 2024

# https://github.com/JSchoonmaker/PDF-Text-Extraction/blob/main/PDF_benchmark.ipynb