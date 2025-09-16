from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import py3Dmol

def getHtml(smiles, width , height, scale):
    mol = Chem.MolFromSmiles(smiles) #ucitavanje smiles
    mol = Chem.AddHs(mol) #dodavanje vodika

    #generiranje 3d kordinata
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())  
    AllChem.UFFOptimizeMolecule(mol) 

    #prikaz
    molblock = Chem.MolToMolBlock(mol)

    view = py3Dmol.view(width=width, height=height)
    view.addModel(molblock, "sdf")
    view.setStyle({'stick': {}, 'sphere': {'scale': scale}})
    view.zoomTo()
    view.spin(True)

    return view._make_html()