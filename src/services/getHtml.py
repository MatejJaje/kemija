from rdkit import Chem
from rdkit.Chem import AllChem

def getHtml(smiles, title, notes, sphere=0.3, stick = 0.2,):
    mol = Chem.MolFromSmiles(smiles) #ucitavanje smiles
    mol = Chem.AddHs(mol) #dodavanje vodika

    #generiranje 3d kordinata
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())  
    AllChem.UFFOptimizeMolecule(mol) 

    #prikaz
    molblock = Chem.MolToMolBlock(mol)
    rawMolblock=""
    for i in molblock:
        if i == "\n":
            rawMolblock+="\\n"
        else:
            rawMolblock+=i
    
    html=open("src/components/template.html","r").read()
    for var,name in [[title,"title"],[notes,"notes"],[sphere,"sphere"],[stick,"stick"],[rawMolblock,"molblock"]]:
        html = html.replace(f"{{{name}}}",str(var))
    return html

