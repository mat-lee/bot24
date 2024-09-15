
WORK_DIR=`pwd`
source $WORK_DIR/a_/e_env/e_env_a.txt

env_print(){
  echo """
  WORK_DIR $(cd  $WORK_DIR ; pwd )
  WORK_DAT $(cd  $WORK_DAT ; pwd  )
  """
}



#ACD_ENV=`basename $(dirname "$PWD")`  # basename $(dirname $(dirname "$PWD"))
ACD_ENV=`basename $(dirname $(dirname $(dirname "$PWD")))`
ACD_ENV_CLONE=py310


acd() {
  echo """
  ACD_ENV       : ${ACD_ENV}
  ACD_ENV_CLONE : ${ACD_ENV_CLONE}
  """
}
acd_() { echo "conda env list" ; }
acd__() { $(acd_) & }

#
#
#
acd_new() {
  echo """
  ACD_ENV       : ${ACD_ENV}
  ACD_ENV_CLONE : ${ACD_ENV_CLONE}
  """
}
acd_new_() { echo "conda create --name ${ACD_ENV} --clone ${ACD_ENV_CLONE}" ; }
acd_new__() { $(acd_new_) & }


#
#
acd_new__pip() {
  echo """
  WORK_DIR      : ${WORK_DIR}
  ACD_ENV       : ${ACD_ENV}
  ACD_ENV_CLONE : ${ACD_ENV_CLONE}
  """
}
acd_new__pip_a='$(which pip) install -r ${WORK_DIR}/requirements.txt'
acd_new__pip_() { eval "$(conda shell.bash hook)" && conda activate ${ACD_ENV} && echo ${acd_new__pip_a} ; }
acd_new__pip__() {  $(acd_new__pip_) ; }


acd_new__pip__ks(){
  echo """
  pip install kernelspec
  python3 -m ipykernel install --user
  python3 -m pip install ipykernel
  python -m ipykernel install --user --name ${ACD_ENV} --display-name ${ACD_ENV}
  """
}

acd_new__pip__ks_a='$(which pip) install ipykernel'
acd_new__pip__ks_(){ eval "$(conda shell.bash hook)" && conda activate ${ACD_ENV} && echo ${acd_new__pip__ks_a} ; }
acd_new__pip__ks__(){ $(acd_new_pip_ks_) ; }

acd_new__pip__ks___a='$(which python) -m ipykernel install --user --name ${ACD_ENV} --display-name ${ACD_ENV}'
acd_new__pip__ks___(){ eval "$(conda shell.bash hook)" && conda activate ${ACD_ENV} && echo ${acd_new__pip__ks___a} ; }
acd_new__pip__ks____(){ $(acd_new__pip__ks___) ; }


sl(){
  echo """
  WORK_DIR  : ${WORK_DIR}

  acd_new
  acd_new__pip
  acd_new__pip__ks
  streamlit run a/ie_org9/app.py
  """
}

sl_app_e_env="source $WORK_DIR/a_/e_env/e_env_a.txt"
sl_app_cli="$(which streamlit) run a/ie_org9/app.py"
sl_app(){
  eval "$(conda shell.bash hook)" && conda activate ${ACD_ENV} && eval ${sl_app_e_env} && echo """
WORK_DIR: $WORK_DIR
WORK_DAT: $WORK_DAT
  """
}
sl_app_(){ eval "$(conda shell.bash hook)" && conda activate ${ACD_ENV} && eval ${sl_app_e_env} && echo ${sl_app_cli} ; }
sl_app__(){ $(sl_app_) ; }
