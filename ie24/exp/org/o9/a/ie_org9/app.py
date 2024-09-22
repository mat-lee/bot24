
import os
import base64
import pandas as pd
import streamlit as st
from copyright import CopyRight

#
# Environment Variables
#
work_dir=os.getcwd()
print(work_dir)

work_env=os.path.join(work_dir,'a_','e_env','e_env_a.txt')

from dotenv import dotenv_values, load_dotenv
load_dotenv(dotenv_path=work_env)
print(str(dotenv_values(work_env)))
os.environ['WORK_DAT']=os.path.abspath(os.environ['WORK_DAT'])


st.title("Copyright Name Finder")

sentence = st.text_input("Input Your Text Here :")

#st.set_option('deprecation.showfileUploaderEncoding', False)

data = st.file_uploader("Upload a Dataset", type=["csv","txt"])


def main():

    def download_file(df):
        """
        Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(
            csv.encode()
        ).decode()  # some strings <-> bytes conversions necessary here
        return f'<a href="data:file/csv;base64,{b64}" download="copyright.csv">Download csv file</a>'
    
    if sentence:
        df3 = {'name' : [sentence]}
        df3 = pd.DataFrame(df3)
        df3 = CopyRight(df3)
        st.dataframe(df3)

    if data is not None:
        df = pd.read_csv(data, encoding = 'utf-8')
        st.dataframe(df.head())

        if st.button("Copyright Names"):
            df2 = CopyRight(df)
            st.dataframe(df2)
            st.markdown(download_file(df2), unsafe_allow_html = True)   

if __name__=='__main__':
    main()
