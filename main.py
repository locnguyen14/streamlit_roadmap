import streamlit as st
import graphviz
import json
import os

main_file_dir = os.getcwd()
json_file_dir = os.path.join(main_file_dir,"roadmaps")

def setupPage() -> None:
  st.set_page_config(layout="wide")
  st.markdown("# Main page 🎈")
  
def setupSelectBox() -> None:
  '''
  A function setup the select box for streamlit app
  '''
  option = st.selectbox("Select A RoadMap", 
                        ("Machine Learning Engineer", "Data Scientist", "Digital Marketing"),
                        index=None,
                        placeholder="...")
  match option:
    case "Machine Learning Engineer": setupGraph(os.path.join(json_file_dir, "ml_curriculumn.json"))
    case "Data Scientist": setupGraph(os.path.join(json_file_dir, "ds_curriculumn.json"))
    case "Digital Marketing": setupGraph(os.path.join(json_file_dir, "dm_curriculumn.json"))      
    case _:
      st.write(f'Road map for {option} has not been generated yet!')

def setupGraph(path: str) -> None:
  '''
  A function load the json file from the path and generate the graph viz object
  '''
  with open(path, "r") as file:
     curriculum = json.load(file)
  file.close()
  
  graph = graphviz.Digraph()
  for index, (target, sources) in enumerate(curriculum.items()):
    for source in sources:
      graph.edge(source, target)
  st.graphviz_chart(graph)
  graphviz.Digraph()
        
def main():
   setupPage()
   setupSelectBox()

if __name__ == "__main__":
    main()






